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
        st.markdown(f"<h1>{st.session_state.name}</h1>", unsafe_allow_html=True)
        st.markdown(f"{st.session_state.email} | {st.session_state.phone} | {st.session_state.location}")
        if st.session_state.website:
            st.markdown(f"Website: {st.session_state.website}")
        
        # Objective
        if st.session_state.objective:
            st.markdown("<h2>Objective</h2>", unsafe_allow_html=True)
            st.markdown(st.session_state.objective)
        
        # Work Experience
        if st.session_state.experiences:
            st.markdown("<h2>Work Experience</h2>", unsafe_allow_html=True)
            for exp in st.session_state.experiences:
                st.markdown(f"**{exp['position']}** at {exp['company']}")
                st.markdown(f"{exp['start_date']} - {exp['end_date']}")
                st.markdown(exp['description'])
                st.markdown(f"Technologies: {exp['technologies']}")
                st.markdown(f"Team Size: {exp['team_size']} | Work Type: {exp['location']}")
                st.markdown("---")
        
        # Education
        if st.session_state.education:
            st.markdown("<h2>Education</h2>", unsafe_allow_html=True)
            for edu in st.session_state.education:
                st.markdown(f"**{edu['degree']}** in {edu['major']}")
                st.markdown(f"{edu['school']} | Graduated: {edu['graduation_date']}")
                if edu['gpa']:
                    st.markdown(f"GPA: {edu['gpa']}")
                if edu['honors']:
                    st.markdown(f"Honors: {edu['honors']}")
                if edu['coursework']:
                    st.markdown(f"Relevant Coursework: {edu['coursework']}")
                st.markdown("---")
        
        # Projects
        if st.session_state.projects:
            st.markdown("<h2>Projects</h2>", unsafe_allow_html=True)
            for project in st.session_state.projects:
                st.markdown(f"**{project['name']}**")
                st.markdown(f"{project['start_date']} - {project['end_date']}")
                st.markdown(project['description'])
                st.markdown(f"Technologies: {project['technologies']}")
                if project['url']:
                    st.markdown(f"URL: {project['url']}")
                st.markdown("---")
        
        # Skills
        if st.session_state.skills:
            st.markdown("<h2>Skills</h2>", unsafe_allow_html=True)
            for skill in st.session_state.skills:
                st.markdown(f"**{skill['name']}**: {skill['proficiency']}")
        
        st.markdown('</div>', unsafe_allow_html=True)