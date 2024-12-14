import streamlit as st

def render_additional_info():
    """Render the additional information section of the resume form."""
    st.subheader("Additional Information")
    
    # Languages
    st.text_area(
        "Languages",
        value=st.session_state.get("languages", ""),
        key="languages",
        help="List languages and proficiency levels"
    )
    
    # Skills
    st.text_area(
        "Skills",
        value=st.session_state.get("skills", ""),
        key="skills",
        help="List your technical and soft skills"
    )
    
    # Certifications
    st.text_area(
        "Certifications",
        value=st.session_state.get("certifications", ""),
        key="certifications",
        help="List relevant certifications"
    )
    
    # Interests
    st.text_area(
        "Interests",
        value=st.session_state.get("interests", ""),
        key="interests",
        help="List your relevant interests and hobbies"
    )
