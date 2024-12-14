import streamlit as st

def render_preview():
    """Render real-time preview of the resume"""
    
    st.subheader("Resume Preview")
    
    # Apply custom CSS for preview
    st.markdown(f"""
    <style>
        .resume-preview {{
            font-family: {st.session_state.get('font_family', 'Arial')}, sans-serif;
            font-size: {st.session_state.get('font_size', '14')}px;
            color: #333;
            line-height: 1.5;
        }}
        .resume-preview h1, .resume-preview h2 {{
            color: {st.session_state.get('theme_color', '#000000')};
        }}
    </style>
    """, unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="resume-preview">', unsafe_allow_html=True)
        
        # Personal Information
        st.markdown(f"<h1>{st.session_state.get('name', '')}</h1>", unsafe_allow_html=True)
        contact_info = []
        if st.session_state.get('email'):
            contact_info.append(st.session_state.get('email'))
        if st.session_state.get('phone'):
            contact_info.append(st.session_state.get('phone'))
        if st.session_state.get('location'):
            contact_info.append(st.session_state.get('location'))
        
        if contact_info:
            st.markdown(" | ".join(contact_info))
            
        if st.session_state.get('website'):
            st.markdown(f"Website: {st.session_state.get('website')}")
        
        # Objective
        if st.session_state.get('objective'):
            st.markdown("<h2>Objective</h2>", unsafe_allow_html=True)
            st.markdown(st.session_state.get('objective'))
        
        # Work Experience
        if st.session_state.get('experiences'):
            st.markdown("<h2>Work Experience</h2>", unsafe_allow_html=True)
            for exp in st.session_state.get('experiences', []):
                st.markdown(f"**{exp.get('position', '')}** at {exp.get('company', '')}")
                st.markdown(f"{exp.get('start_date', '')} - {exp.get('end_date', '')}")
                st.markdown(exp.get('description', ''))
                if exp.get('technologies'):
                    st.markdown(f"Technologies: {exp.get('technologies')}")
                if exp.get('team_size') and exp.get('location'):
                    st.markdown(f"Team Size: {exp.get('team_size')} | Work Type: {exp.get('location')}")
                st.markdown("---")
        
        # Education
        if st.session_state.get('education'):
            st.markdown("<h2>Education</h2>", unsafe_allow_html=True)
            for edu in st.session_state.get('education', []):
                st.markdown(f"**{edu.get('degree', '')}** in {edu.get('major', '')}")
                st.markdown(f"{edu.get('school', '')} | Graduated: {edu.get('graduation_date', '')}")
                if edu.get('gpa'):
                    st.markdown(f"GPA: {edu.get('gpa')}")
                if edu.get('honors'):
                    st.markdown(f"Honors: {edu.get('honors')}")
                if edu.get('coursework'):
                    st.markdown(f"Relevant Coursework: {edu.get('coursework')}")
                st.markdown("---")
        
        # Projects
        if st.session_state.get('projects'):
            st.markdown("<h2>Projects</h2>", unsafe_allow_html=True)
            for project in st.session_state.get('projects', []):
                st.markdown(f"**{project.get('name', '')}**")
                st.markdown(f"{project.get('start_date', '')} - {project.get('end_date', '')}")
                st.markdown(project.get('description', ''))
                if project.get('technologies'):
                    st.markdown(f"Technologies: {project.get('technologies')}")
                if project.get('url'):
                    st.markdown(f"URL: {project.get('url')}")
                st.markdown("---")
        
        # Skills
        if st.session_state.get('skills'):
            st.markdown("<h2>Skills</h2>", unsafe_allow_html=True)
            for skill in st.session_state.get('skills', []):
                st.markdown(f"**{skill.get('name', '')}**: {skill.get('proficiency', '')}")
        
        st.markdown('</div>', unsafe_allow_html=True)
