import streamlit as st

def render_additional_info():
    """Render the additional information section of the resume form."""
    st.subheader("Additional Information")
    
    # Languages (should be handled in personal_info.py instead)
    # This section might be redundant since languages are already handled in personal_info.py
    
    # Skills
    skills = st.session_state.get("skills", [])
    skills_text = "\n".join([f"{skill.get('name', '')}: {skill.get('proficiency', '')}" for skill in skills])
    st.text_area(
        "Skills",
        value=skills_text,
        key="skills_display",
        help="List your technical and soft skills",
        disabled=True
    )
    
    # Certifications
    cert_value = st.session_state.get("certifications", "")
    st.text_area(
        "Certifications",
        value=cert_value,
        key="certifications",
        help="List relevant certifications"
    )
    
    # Interests
    interests = st.session_state.get("additional_info", {}).get("interests", [])
    interests_text = "\n".join(interests) if isinstance(interests, list) else interests
    st.text_area(
        "Interests",
        value=interests_text,
        key="interests",
        help="List your relevant interests and hobbies"
    )
