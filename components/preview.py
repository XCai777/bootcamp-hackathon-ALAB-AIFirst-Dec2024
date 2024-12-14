import streamlit as st

def render_preview():
    """Render real-time preview of the resume"""
    
    st.subheader("Resume Preview")
    
    # Apply custom CSS for preview
    st.markdown(f"""
    <style>
        .resume-preview {{
            font-family: {st.session_state.font_family}, sans-serif;
            font-size: {st.session_state.font_size}px;
            color: #333;
            line-height: 1.5;
        }}
        .resume-preview h1, .resume-preview h2 {{
            color: {st.session_state.theme_color};
        }}
    </style>
    """, unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="resume-preview">', unsafe_allow_html=True)
        
        # Personal Information
        if st.session_state.get('personal_info'):
            personal_info = st.session_state.personal_info
            st.markdown(f"# {personal_info.get('name', '')}")
            st.markdown(f"{personal_info.get('email', '')} | {personal_info.get('phone', '')} | {personal_info.get('location', '')}")
        
        # Professional Summary
        if st.session_state.get('professional_summary'):
            st.markdown("## Professional Summary")
            st.markdown(st.session_state.professional_summary)
        
        # Work Experience
        if st.session_state.get('work_experience'):
            st.markdown("## Work Experience")
            for experience in st.session_state.work_experience:
                st.markdown(f"**{experience.get('company', '')}** - {experience.get('position', '')}")
                st.markdown(f"{experience.get('start_date', '')} - {experience.get('end_date', '')}")
                st.markdown(experience.get('description', ''))
        
        # Education
        if st.session_state.get('education'):
            st.markdown("## Education")
            for edu in st.session_state.education:
                st.markdown(f"**{edu.get('school', '')}** - {edu.get('degree', '')}")
                st.markdown(f"{edu.get('start_date', '')} - {edu.get('end_date', '')}")
                st.markdown(edu.get('description', ''))
        
        # Projects
        if st.session_state.get('projects'):
            st.markdown("## Projects")
            for project in st.session_state.projects:
                st.markdown(f"**{project.get('name', '')}**")
                st.markdown(project.get('description', ''))
        
        st.markdown('</div>', unsafe_allow_html=True)
