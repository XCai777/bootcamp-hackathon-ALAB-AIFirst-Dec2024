import streamlit as st

def render_education():
    """Render education section"""
    
    st.subheader("Education")
    
    education = st.session_state.get("education", [])
    
    for i, edu in enumerate(education):
        with st.expander(f"Education {i+1}", expanded=True):
            col1, col2 = st.columns(2)
            
            with col1:
                edu["school"] = st.text_input("School/University", value=edu.get("school", ""), key=f"school_{i}")
                edu["degree"] = st.text_input("Degree", value=edu.get("degree", ""), key=f"degree_{i}")
            
            with col2:
                edu["major"] = st.text_input("Major", value=edu.get("major", ""), key=f"major_{i}")
                edu["graduation_date"] = st.date_input("Graduation Date", value=edu.get("graduation_date"), key=f"grad_date_{i}")
            
            edu["gpa"] = st.number_input("GPA", value=edu.get("gpa", 0.0), min_value=0.0, max_value=4.0, step=0.1, key=f"gpa_{i}")
            
            edu["honors"] = st.text_area("Honors/Awards", value=edu.get("honors", ""), key=f"honors_{i}", height=50)
            edu["coursework"] = st.text_area("Relevant Coursework", value=edu.get("coursework", ""), key=f"coursework_{i}", height=50)
            
            if st.button("Remove Education", key=f"remove_edu_{i}"):
                education.pop(i)
                st.rerun()
    
    if st.button("Add Education"):
        education.append({})
        st.rerun()
    
    st.session_state.education = education
