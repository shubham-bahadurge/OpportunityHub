def calculate_match(student, opportunity):

    score = 0

    matched_skills = []
    matched_interests = []
    category_match = False
    education_match = False


    # --------------------------------
    # 1. SKILL MATCH - 40 POINTS
    # --------------------------------

    student_skills = [
        skill.lower()
        for skill in (student.get("skills") or [])
        if isinstance(skill, str)
    ]

    opportunity_skills = [
        skill.lower()
        for skill in (opportunity.get("skills") or [])
        if isinstance(skill, str)
    ]


    for skill in opportunity_skills:

        if skill in student_skills:

            matched_skills.append(skill)

    
    if opportunity_skills:

        skill_score = (
            len(matched_skills)
            / len(opportunity_skills)
        ) * 40

        score += skill_score


    # --------------------------------
    # 2. INTEREST MATCH - 30 POINTS
    # --------------------------------

    student_interests = [
        interest.lower()
        for interest in (student.get("interests") or [])
        if isinstance(interest, str)
    ]

    opportunity_interests = [
        interest.lower()
        for interest in (opportunity.get("interests") or [])
        if isinstance(interest, str)
    ]


    for interest in opportunity_interests:

        if interest in student_interests:

            matched_interests.append(interest)


    if opportunity_interests:

        interest_score = (
            len(matched_interests)
            / len(opportunity_interests)
        ) * 30

        score += interest_score


    # --------------------------------
    # 3. CATEGORY MATCH - 20 POINTS
    # --------------------------------

    preferred_categories = [
        category.lower()
        for category in (student.get("categories") or [])
        if isinstance(category, str)
    ]


    if opportunity.get("category", "").lower() in preferred_categories:

        score += 20

        category_match = True


    # --------------------------------
    # 4. EDUCATION MATCH - 10 POINTS
    # --------------------------------

    student_education = (
        (student.get("education") or "")
        .lower()
    )


    opportunity_education = [
        education.lower()
        for education in (opportunity.get("education") or [])
        if isinstance(education, str)
    ]


    if student_education in opportunity_education:

        score += 10

        education_match = True


    # --------------------------------
    # FINAL RESULT
    # --------------------------------

    return {

        "score": round(score),

        "matched_skills": matched_skills,

        "matched_interests": matched_interests,

        "category_match": category_match,

        "education_match": education_match

    }