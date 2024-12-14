import streamlit as st
from components.ai_assistant import AIAssistant

def render_objective():
    """Render objective section with AI generation option"""
    
    st.subheader("Objective")
    
    objective = st.text_area(
        "Career Objective",
        value=st.session_state.get("objective", ""),
        height=100
    )
    st.session_state.objective = objective
    
    if st.button("Generate AI Objective"):
        ai_assistant = AIAssistant()
        experience_data = st.session_state.get("experiences", [])
        generated_objective = ai_assistant.generate_objective(experience_data)
        st.session_state.objective = generated_objective
        st.rerun()
