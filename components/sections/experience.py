import streamlit as st
from datetime import datetime
from components.ai_assistant import AIAssistant

def render_experience():
    """Render work experience section"""
    
    st.subheader("Experience")
    
    # Initialize experience list in session state if it doesn't exist
    if 'experiences' not in st.session_state:
        st.session_state.experiences = []
    
    # Add new experience
    with st.expander("Add Experience"):
        with st.form(key="experience_form"):
            company = st.text_input("Company Name")
            position = st.text_input("Position")
            start_date = st.date_input("Start Date")
            end_date = st.date_input("End Date")
            description = st.text_area("Description")
            
            if st.form_submit_button("Add Experience"):
                new_experience = {
                    "company": company,
                    "position": position,
                    "start_date": start_date.strftime("%B %Y"),
                    "end_date": end_date.strftime("%B %Y"),
                    "description": description
                }
                st.session_state.experiences.append(new_experience)
                st.success("Experience added successfully!")
    
    # Display and edit existing experiences
    for idx, experience in enumerate(st.session_state.experiences):
        with st.expander(f"{experience['position']} at {experience['company']}"):
            with st.form(key=f"edit_experience_{idx}"):
                company = st.text_input("Company Name", value=experience['company'])
                position = st.text_input("Position", value=experience['position'])
                start_date = st.date_input("Start Date", value=datetime.strptime(experience['start_date'], "%B %Y"))
                end_date = st.date_input("End Date", value=datetime.strptime(experience['end_date'], "%B %Y"))
                description = st.text_area("Description", value=experience['description'])
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.form_submit_button("Update"):
                        st.session_state.experiences[idx] = {
                            "company": company,
                            "position": position,
                            "start_date": start_date.strftime("%B %Y"),
                            "end_date": end_date.strftime("%B %Y"),
                            "description": description
                        }
                        st.success("Experience updated successfully!")
                
                with col2:
                    if st.form_submit_button("Delete"):
                        st.session_state.experiences.pop(idx)
                        st.success("Experience deleted successfully!")
