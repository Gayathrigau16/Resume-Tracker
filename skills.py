def find_skills(resume_text):
    skills = [
        "Python",
        "Pandas",
        "NumPy",
        "machine learning",
        "deep learning",
        "SQL",
        "HTML",
        "CSS",
        "Natural Language Processing",
        "computer vision",
        "data visualization",
        "Power BI",
        "Tableau",
        "Excel",
        "TensorFlow",
        "Scikit-learn",
        ]
    
    found_skills = []

    resume_text = resume_text.lower()

    for skill in skills:
        if skill.lower() in resume_text:
            found_skills.append(skill)

    return found_skills