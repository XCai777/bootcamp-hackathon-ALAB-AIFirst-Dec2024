import streamlit as st

def render_personal_info():
    """Render personal information section"""
    
    # Basic Information
    st.session_state.name = st.text_input(
        "Full Name",
        value=st.session_state.get("name", "")
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.session_state.email = st.text_input(
            "Email",
            value=st.session_state.get("email", "")
        )
        
        st.session_state.location = st.text_input(
            "Location",
            value=st.session_state.get("location", "")
        )
    
    with col2:
        st.session_state.phone = st.text_input(
            "Phone",
            value=st.session_state.get("phone", "")
        )
        
        st.session_state.website = st.text_input(
            "Website/LinkedIn",
            value=st.session_state.get("website", "")
        )
    
    # Profile Picture
    st.subheader("Profile Picture")
    uploaded_file = st.file_uploader("Upload a profile picture", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        st.session_state.profile_picture = uploaded_file
        st.image(uploaded_file, width=100)
    
    # Social Media
    st.subheader("Social Media")
    col1, col2 = st.columns(2)
    
    with col1:
        st.session_state.github = st.text_input(
            "GitHub",
            value=st.session_state.get("github", "")
        )
    
    with col2:
        st.session_state.twitter = st.text_input(
            "Twitter",
            value=st.session_state.get("twitter", "")
        )
    
    # Languages
    st.subheader("Languages")
    languages = st.session_state.get("languages", [{"language": "", "proficiency": ""}])
    
    for i, lang in enumerate(languages):
        col1, col2, col3 = st.columns([2, 2, 1])
        
        with col1:
            lang["language"] = st.text_input(
                "Language",
                value=lang["language"],
                key=f"lang_{i}"
            )
        
        with col2:
            lang["proficiency"] = st.selectbox(
                "Proficiency",
                options=["Native", "Fluent", "Advanced", "Intermediate", "Basic"],
                index=0 if lang["proficiency"] == "" else ["Native", "Fluent", "Advanced", "Intermediate", "Basic"].index(lang["proficiency"]),
                key=f"prof_{i}"
            )
        
        with col3:
            if st.button("Remove", key=f"remove_lang_{i}"):
                languages.pop(i)
                st.experimental_rerun()
    
    if st.button("Add Language"):
        languages.append({"language": "", "proficiency": ""})
        st.experimental_rerun()
    
    st.session_state.languages = languages