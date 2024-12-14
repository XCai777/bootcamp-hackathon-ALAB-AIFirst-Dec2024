import streamlit as st
from components.ai_assistant import AIAssistant

def render_experience():
    """Render work experience section"""
    
    st.subheader("Work Experience")
    
    experiences = st.session_state.get("experiences", [])
    
    for i, exp in enumerate(experiences):
        with st.expander(f"Experience {i+1}", expanded=True):
            col1, col2 = st.columns(2)
            
            with col1:
                exp["company"] = st.text_input("Company", value=exp.get("company", ""), key=f"company_{i}")
                exp["position"] = st.text_input("Position", value=exp.get("position", ""), key=f"position_{i}")
            
            with col2:
                exp["start_date"] = st.date_input("Start Date", value=exp.get("start_date"), key=f"start_date_{i}")
                exp["end_date"] = st.date_input("End Date", value=exp.get("end_date"), key=f"end_date_{i}")
            
            exp["description"] = st.text_area("Description", value=exp.get("description", ""), key=f"description_{i}", height=100)
            
            exp["technologies"] = st.text_input("Technologies/Tools Used", value=exp.get("technologies", ""), key=f"technologies_{i}")
            
            col1, col2 = st.columns(2)
            with col1:
                exp["team_size"] = st.number_input("Team Size", value=exp.get("team_size", 1), min_value=1, key=f"team_size_{i}")
            with col2:
                exp["location"] = st.selectbox("Work Type", options=["On-site", "Remote", "Hybrid"], index=0, key=f"location_{i}")
            
            if st.button("Remove Experience", key=f"remove_exp_{i}"):
                experiences.pop(i)
                st.experimental_rerun()
            
            if st.button("Enhance Description", key=f"enhance_desc_{i}"):
                ai_assistant = AIAssistant()
                enhanced_description = ai_assistant.enhance_description(exp["description"])
                exp["description"] = enhanced_description
                st.experimental_rerun()
    
    if st.button("Add Experience"):
        experiences.append({})
        st.experimental_rerun()
    
    st.session_state.experiences = experiences