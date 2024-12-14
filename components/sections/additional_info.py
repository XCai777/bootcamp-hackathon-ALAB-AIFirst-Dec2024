import streamlit as st

def render_additional_info():
    """Render the additional information section of the resume form."""
    st.subheader("Additional Information")
    
    # Helper function to safely convert values to string
    def safe_str_conversion(value):
        if value is None:
            return ""
        return str(value)
    
    # Languages
    languages_value = safe_str_conversion(st.session_state.get("languages", ""))
    st.text_area(
        "Languages",
        value=languages_value,
        key="languages",
        help="List languages and proficiency levels"
    )
    
    # Skills
    skills_value = safe_str_conversion(st.session_state.get("skills", ""))
    st.text_area(
        "Skills",
        value=skills_value,
        key="skills",
        help="List your technical and soft skills"
    )
    
    # Certifications
    cert_value = safe_str_conversion(st.session_state.get("certifications", ""))
    st.text_area(
        "Certifications",
        value=cert_value,
        key="certifications",
        help="List relevant certifications"
    )
    
    # Interests
    interests_value = safe_str_conversion(st.session_state.get("interests", ""))
    st.text_area(
        "Interests",
        value=interests_value,
        key="interests",
        help="List your relevant interests and hobbies"
    )
