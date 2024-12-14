import streamlit as st
from components.ai_assistant import AIAssistant

def render_skills():
    """Render skills section with AI suggestions"""
    
    st.subheader("Skills")
    
    skills = st.session_state.get("skills", [])
    
    for i, skill in enumerate(skills):
        col1, col2, col3 = st.columns([3, 2, 1])
        
        with col1:
            skill["name"] = st.text_input("Skill", value=skill.get("name", ""), key=f"skill_{i}")
        
        with col2:
            skill["proficiency"] = st.select_slider(
                "Proficiency",
                options=["Beginner", "Intermediate", "Advanced", "Expert"],
                value=skill.get("proficiency", "Intermediate"),
                key=f"skill_prof_{i}"
            )
        
        with col3:
            if st.button("Remove", key=f"remove_skill_{i}"):
                skills.pop(i)
                st.experimental_rerun()
    
    if st.button("Add Skill"):
        skills.append({})
        st.experimental_rerun()
    
    st.session_state.skills = skills
    
    if st.button("Suggest Skills"):
        ai_assistant = AIAssistant()
        experience_data = st.session_state.get("experiences", [])
        suggested_skills = ai_assistant.suggest_skills(experience_data)
        st.write("Suggested Skills:")
        st.write(suggested_skills)