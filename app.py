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
    return render_template("dashboard.html")
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


@app.route("/api/recommendations", methods=["POST"])
def recommendations():

    student = request.get_json(silent=True) or {}

    results = []

    for opportunity in opportunities:

        match = calculate_match(
            student,
            opportunity
        )

        opportunity_copy = opportunity.copy()

        opportunity_copy["score"] = match.get("score", 0)

        opportunity_copy["matched_skills"] = match.get("matched_skills", [])

        opportunity_copy["matched_interests"] = match.get("matched_interests", [])

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