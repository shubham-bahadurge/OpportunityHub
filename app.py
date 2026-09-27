from flask import Flask, render_template, request, jsonify

from opportunities import opportunities
from matching import calculate_match


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", opportunities=opportunities)
@app.route("/opportunities")
def opportunities_page():
    return render_template("opportunities.html")


@app.route("/applications")
def applications_page():
    return render_template("applications.html", opportunities=opportunities)


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
@app.route("/saved")
def saved():
    return render_template("saved.html")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)