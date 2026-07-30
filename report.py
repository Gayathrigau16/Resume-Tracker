def generate_report(skills,ats_score,missing_skills,match_score):
    report = f"""
=================================
    RESUME ANALYSIS REPORT
=================================
    ATS Score :{ats_score}%"
    Job Description Match : {match_score}%
=================================
    Skills Found
=================================
    """
    for skill in skills:
        report += f"\n✅ {skill}"
        report += "\n\n=================================\n"
        report += "Missing skills\n"
        report += "=================================\n"
        
        if missing_skills:
            for skill in missing_skills:
                report += f"\n❌ {skill}"
        else:
            report += "\nNo missing skills"
            
        report += "\n\n=================================\nSuggestions\n=================================\n"
        
        if ats_score <80:
            report += "\n Add more relevent skills."
            report += "\n Improve porject description"
            report += "\n Add Github profile"
            report += "\n Add certifications"
        else:
            report += "\n Excellent Resume"
            
        return report
        
    