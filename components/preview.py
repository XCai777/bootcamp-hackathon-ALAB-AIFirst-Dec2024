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
            padding: 20px;
            background: white;
            border-radius: 5px;
        }}
        .resume-preview h1, .resume-preview h2 {{
            color: {st.session_state.theme_color};
            margin-bottom: 10px;
        }}
        .contact-info {{
            margin-bottom: 20px;
        }}
    </style>
    """, unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="resume-preview">', unsafe_allow_html=True)
        
        # Personal Information
        if 'full_name' in st.session_state:
            st.markdown(f"<h1>{st.session_state.full_name}</h1>", unsafe_allow_html=True)
            
            # Contact information
            contact_info = []
            if 'email' in st.session_state:
                contact_info.append(st.session_state.email)
            if 'phone' in st.session_state:
                contact_info.append(st.session_state.phone)
            if 'location' in st.session_state:
                contact_info.append(st.session_state.location)
            
            if contact_info:
                st.markdown(f"<div class='contact-info'>{' | '.join(contact_info)}</div>", unsafe_allow_html=True)
            
            if 'website_linkedin' in st.session_state and st.session_state.website_linkedin:
                st.markdown(f"Website/LinkedIn: {st.session_state.website_linkedin}")
        
        # Objective
        if st.session_state.get('professional_summary'):
            st.markdown("<h2>Objective</h2>", unsafe_allow_html=True)
            st.markdown(st.session_state.professional_summary)
        
        # Work Experience
        if st.session_state.get('work_experience'):
            st.markdown("<h2>Work Experience</h2>", unsafe_allow_html=True)
            for exp in st.session_state.work_experience:
                st.markdown(f"**{exp.get('company', '')}** at {exp.get('position', '')}")
                st.markdown(f"{exp.get('start_date', '')} - {exp.get('end_date', '')}")
                st.markdown(exp.get('description', ''))
                if exp.get('technologies'):
                    st.markdown(f"Technologies: {exp.get('technologies', '')}")
                if exp.get('team_size') and exp.get('location'):
                    st.markdown(f"Team Size: {exp.get('team_size', '')} | Work Type: {exp.get('location', '')}")
                st.markdown("---")
        
        # Education
        if st.session_state.get('education'):
            st.markdown("<h2>Education</h2>", unsafe_allow_html=True)
            for edu in st.session_state.education:
                st.markdown(f"**{edu.get('school', '')}** in {edu.get('degree', '')}")
                st.markdown(f"{edu.get('start_date', '')} - {edu.get('end_date', '')}")
                if edu.get('gpa'):
                    st.markdown(f"GPA: {edu.get('gpa', '')}")
                if edu.get('honors'):
                    st.markdown(f"Honors: {edu.get('honors', '')}")
                if edu.get('coursework'):
                    st.markdown(f"Relevant Coursework: {edu.get('coursework', '')}")
                st.markdown("---")
        
        # Projects
        if st.session_state.get('projects'):
            st.markdown("<h2>Projects</h2>", unsafe_allow_html=True)
            for project in st.session_state.projects:
                st.markdown(f"**{project.get('name', '')}**")
                st.markdown(f"{project.get('start_date', '')} - {project.get('end_date', '')}")
                st.markdown(project.get('description', ''))
                if project.get('url'):
                    st.markdown(f"URL: {project.get('url', '')}")
                st.markdown("---")
        
        # Skills
        if st.session_state.skills:
            st.markdown("<h2>Skills</h2>", unsafe_allow_html=True)
            for skill in st.session_state.skills:
                st.markdown(f"**{skill['name']}**: {skill['proficiency']}")
        
        st.markdown('</div>', unsafe_allow_html=True)
