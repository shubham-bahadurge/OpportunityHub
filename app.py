from functools import wraps
import os
from flask import (
    Flask,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from matching import calculate_match
from opportunities import opportunities

app = Flask(__name__)
app.secret_key = os.environ.get(
    "SECRET_KEY", "opportunityhub-hackathon-secret-key-2026"
)

# Demo accounts for Hackathon MVP Prototype
DEMO_USERS = {
    "admin@opportunityhub.com": {
        "password": "admin123",
        "role": "admin",
        "name": "Administrator",
    },
    "student@opportunityhub.com": {
        "password": "student123",
        "role": "student",
        "name": "Student",
    },
}

USER_ALIASES = {
    "admin": "admin@opportunityhub.com",
    "student": "student@opportunityhub.com",
}


def login_required(role=None):
    """Route decorator to enforce session authentication and role access."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user = session.get("user")
            if not user:
                return redirect(url_for("login", next=request.path))
            user_role = user.get("role")
            if role:
                if user_role != role:
                    if user_role == "student" and role == "admin":
                        # Student attempting to access admin portal
                        return redirect(url_for("student_panel"))
                    elif user_role == "admin" and role == "student":
                        # Admin attempting to access student portal
                        return redirect(url_for("admin_panel"))
                    return redirect(url_for("login"))
            else:
                if user_role == "admin":
                    return redirect(url_for("admin_panel"))
            return f(*args, **kwargs)
        return decorated_function
    return decorator


@app.context_processor
def inject_user():
    return {"current_user": session.get("user")}


# =====================================================================
# AUTHENTICATION ROUTES
# =====================================================================

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.get_json(silent=True) or request.form
        raw_user = (data.get("email") or data.get("username") or "").strip().lower()
        raw_password = (data.get("password") or "").strip()
        remember = data.get("remember")

        email = USER_ALIASES.get(raw_user, raw_user)
        user_record = DEMO_USERS.get(email)

        if user_record and user_record["password"] == raw_password:
            session["user"] = {
                "email": email,
                "role": user_record["role"],
                "name": user_record["name"],
            }
            if remember:
                session.permanent = True

            next_url = request.args.get("next")
            if not next_url or not next_url.startswith("/") or next_url.startswith("//"):
                next_url = url_for("admin_panel") if user_record["role"] == "admin" else url_for("student_panel")
            else:
                if user_record["role"] == "student" and next_url.startswith("/admin"):
                    next_url = url_for("student_panel")
                elif user_record["role"] == "admin" and (next_url.startswith("/student") or next_url.startswith("/dashboard") or next_url.startswith("/applications") or next_url.startswith("/saved") or next_url.startswith("/profile")):
                    next_url = url_for("admin_panel")

            if request.is_json:
                return jsonify({"success": True, "redirect": next_url, "user": session["user"]})
            return redirect(next_url)

        error_msg = "Invalid email or password. Please verify demo credentials."
        if request.is_json:
            return jsonify({"success": False, "error": error_msg}), 401
        return render_template("login.html", error=error_msg), 401

    # GET request
    user = session.get("user")
    if user:
        if user.get("role") == "admin":
            return redirect(url_for("admin_panel"))
        return redirect(url_for("student_panel"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# =====================================================================
# PUBLIC OPPORTUNITY ROUTES
# =====================================================================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/opportunities")
def opportunities_page():
    return render_template("opportunities.html")


@app.route("/opportunity/<int:opportunity_id>")
def opportunity_details(opportunity_id):
    opportunity = next(
        (
            item
            for item in opportunities
            if item["id"] == opportunity_id
        ),
        None
    )

    if opportunity is None:
        return "Opportunity not found", 404

    return render_template(
        "opportunity_details.html",
        opportunity=opportunity
    )


# =====================================================================
# PROTECTED STUDENT ROUTES
# =====================================================================

@app.route("/student")
@login_required(role="student")
def student_panel():
    return render_template("dashboard.html", opportunities=opportunities)


@app.route("/dashboard")
@login_required(role="student")
def dashboard():
    return render_template("dashboard.html", opportunities=opportunities)


@app.route("/applications")
@login_required(role="student")
def applications_page():
    return render_template("applications.html", opportunities=opportunities)


@app.route("/saved")
@login_required(role="student")
def saved():
    return render_template("saved.html")


@app.route("/profile")
@login_required(role="student")
def profile():
    return render_template("profile.html")


# =====================================================================
# PROTECTED ADMIN ROUTE
# =====================================================================

@app.route("/admin")
@login_required(role="admin")
def admin_panel():
    return render_template("admin.html", opportunities=opportunities)


# =====================================================================
# RECOMMENDATION API
# =====================================================================

@app.route("/api/recommendations", methods=["POST"])
def recommendations():
    student = request.get_json(silent=True) or {}
    student_skills = [
        s.lower() for s in (student.get("skills") or [])
        if isinstance(s, str)
    ]

    results = []

    for opportunity in opportunities:
        match = calculate_match(
            student,
            opportunity
        )

        opportunity_copy = opportunity.copy()
        opportunity_copy["score"] = match.get("score", 0)

        opp_skills_map = {s.lower(): s for s in (opportunity.get("skills") or []) if isinstance(s, str)}
        opp_interests_map = {i.lower(): i for i in (opportunity.get("interests") or []) if isinstance(i, str)}

        opportunity_copy["matched_skills"] = [
            opp_skills_map.get(s.lower(), s.title())
            for s in match.get("matched_skills", [])
        ]

        opportunity_copy["matched_interests"] = [
            opp_interests_map.get(i.lower(), i.title())
            for i in match.get("matched_interests", [])
        ]

        opportunity_copy["category_match"] = match.get("category_match", False)
        opportunity_copy["education_match"] = match.get("education_match", False)

        # Skill gap analysis
        opp_skills = [s for s in (opportunity.get("skills") or []) if isinstance(s, str)]
        missing_skills = [s for s in opp_skills if s.lower() not in student_skills]
        opportunity_copy["missing_skills"] = missing_skills

        results.append(opportunity_copy)

    # Sort highest match first
    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return jsonify(results)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)