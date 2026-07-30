def match_resume(resume_text, job_description):
    resume_word = set(resume_text.lower().split())
    job_word = set(job_description.lower().split())
    matched_word = resume_word.intersection(job_word)
    score = (len(matched_word) / len(job_word) * 100) if len(job_word) > 0 else 0
    return round(score , 2)