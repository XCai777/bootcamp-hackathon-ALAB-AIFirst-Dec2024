import streamlit as st

def render_additional_info():
    """Render the additional information section of the resume form."""
    st.subheader("Additional Information")
    
    # Languages
    languages_value = st.session_state.get("languages", "")
    if not isinstance(languages_value, str):
        languages_value = str(languages_value) if languages_value is not None else ""
    
    st.text_area(
        "Languages",
        value=languages_value,
        key="languages",
        help="List languages and proficiency levels"
    )
    
    # Skills
    skills_value = st.session_state.get("skills", "")
    if not isinstance(skills_value, str):
        skills_value = str(skills_value) if skills_value is not None else ""
    
    st.text_area(
        "Skills",
        value=skills_value,
        key="skills",
        help="List your technical and soft skills"
    )
    
    # Certifications
    cert_value = st.session_state.get("certifications", "")
    if not isinstance(cert_value, str):
        cert_value = str(cert_value) if cert_value is not None else ""
    
    st.text_area(
        "Certifications",
        value=cert_value,
        key="certifications",
        help="List relevant certifications"
    )
    
    # Interests
    interests_value = st.session_state.get("interests", "")
    if not isinstance(interests_value, str):
        interests_value = str(interests_value) if interests_value is not None else ""
    
    st.text_area(
        "Interests",
        value=interests_value,
        key="interests",
        help="List your relevant interests and hobbies"
    )
