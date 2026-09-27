from opportunities import opportunities
from matching import calculate_match


student = {

    "education": "Diploma",

    "skills": [
        "Python",
        "Machine Learning"
    ],

    "interests": [
        "Artificial Intelligence"
    ],

    "categories": [
        "Internship"
    ]

}


for opportunity in opportunities:

    result = calculate_match(
        student,
        opportunity
    )

    print(
        opportunity["title"],
        "->",
        result["score"],
        "%"
    )