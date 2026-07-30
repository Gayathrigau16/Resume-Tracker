def find_missing_skills(resume_text,job_description):
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
    
    missing = []
    resume_text = resume_text.lower()
    job_description = job_description.lower()
    
    for skill in skills:
        if skill in job_description and skill not in resume_text:
            missing.append(skill)
            
    return missing