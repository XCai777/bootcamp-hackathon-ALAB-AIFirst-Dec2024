import streamlit as st
from typing import List, Dict
from .sections.personal_info import render_personal_info
from .sections.objective import render_objective
from .sections.experience import render_experience
from .sections.education import render_education
from .sections.projects import render_projects
from .sections.skills import render_skills
from .sections.additional_info import render_additional_info
from .sections.resume_settings import render_resume_settings

def render_sidebar():
    """Render the sidebar with all input sections"""
    
    with st.expander("📝 Resume Settings", expanded=True):
        render_resume_settings()
    
    with st.expander("👤 Personal Information", expanded=True):
        render_personal_info()
    
    with st.expander("🎯 Objective", expanded=True):
        render_objective()
    
    with st.expander("💼 Work Experience", expanded=True):
        render_experience()
    
    with st.expander("🎓 Education", expanded=True):
        render_education()
    
    with st.expander("🚀 Projects", expanded=True):
        render_projects()
    
    with st.expander("🔧 Skills", expanded=True):
        render_skills()
    
    with st.expander("ℹ️ Additional Information", expanded=True):
        render_additional_info()