import streamlit as st # pyright: ignore[reportMissingImports]
from parser import extract_text
from skills import find_skills
from ats import calculate_ats
from jd_match import match_resume
from missing_skills import find_missing_skills
from charts import plot_skills
from report import generate_report

st.set_page_config(page_title="Resume Tracker")
st.title("Resume Tracker")

uploaded_file = st.file_uploader("Upload Resume",type=["pdf"])

if uploaded_file is not None:
    st.success("Resume Uploaded Successfully!")

    resume_text = extract_text(uploaded_file)

    st.subheader("Resume Text")
    st.text_area("Extract Text",resume_text,height=300)

    skills = find_skills(resume_text)
    st.subheader("Detected skills")
    if skills:
        st.write("✅",skills)
    else:
        st.write("No skills detected")

    ats_score = calculate_ats(skills)
    st.subheader("ATS Score")
    st.progress(int(ats_score))
    st.success(f"Your ATS Score is:{ats_score}%")

    if ats_score>=80:
        st.success("Excellent Resume")
    elif ats_score>=60:
        st.warning("Good resume. Add some relevant skills")
    else:
        st.error("Low ATS Score.Improve your resume")

    st.subheader("Job Description Match")
    job_description = st.text_area("Paste job description here")
    if job_description:
        match_score = match_resume(resume_text,job_description)
        st.subheader("Resume match score")
        st.progress(int(match_score))
        st.success(f"Match Score is: {match_score}%")
        
    missing = find_missing_skills(resume_text,job_description)
    st.header("Missing skills")
    if missing:
        for skill in missing:
            st.write("❌",skill)
        else:
            st.write("No missing Skills")

    st.markdown("---")
    st.header("📊Dashboard")
    
    col1, col2, col3,col4 = st.columns(4)
    
    with col1:
        st.metric("Skills Found",len(skills))
        
    with col2:
        st.metric("ATS Score",f"{ats_score}%")
        
    with col3:
        if job_description:
            st.metric("JD Score",f"{match_score}%")
        else:
            st.metric("JD Score", "0%")
    
    with col4:
        if job_description:
            st.metric("Missing Skills",len(missing))
        else:
            st.metric("Missing skills", "0")
            
    st.markdown("---")
    st.header("Skills Analysis Chart")
    if job_description:
        fig =  plot_skills(skills,missing)
        st.pyplot(fig)
        
    report = generate_report(skills,ats_score,missing,match_score)
    st.download_button(label = "📩Download Report", data = report ,file_name = "Resume_Report.txt", mime="text/plain")
    
    
    
    
          
            
        