import streamlit as st
from datetime import datetime

def render_experience():
    """Render work experience section"""
    
    st.subheader("Experience")
    
    # Initialize experience list in session state if it doesn't exist
    if 'experiences' not in st.session_state:
        st.session_state.experiences = []
    
    # Add new experience
    st.subheader("Add Experience", divider='gray')
    with st.form(key="experience_form"):
        company = st.text_input("Company Name")
        position = st.text_input("Position")
        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date")
        description = st.text_area("Description")
        
        if st.form_submit_button("Add Experience"):
            if company and position:  # Only add if required fields are filled
                new_experience = {
                    "company": company,
                    "position": position,
                    "start_date": start_date.strftime("%B %Y"),
                    "end_date": end_date.strftime("%B %Y"),
                    "description": description
                }
                st.session_state.experiences.append(new_experience)
                st.success("Experience added successfully!")
            else:
                st.error("Please fill in both Company Name and Position.")
    
    # Display and edit existing experiences
    if st.session_state.experiences:
        st.subheader("Edit Experiences", divider='gray')
        
    for idx, experience in enumerate(st.session_state.experiences):
        # Get values with defaults in case they're missing
        company = experience.get('company', 'No Company')
        position = experience.get('position', 'No Position')
        start_date = experience.get('start_date', datetime.now().strftime("%B %Y"))
        end_date = experience.get('end_date', datetime.now().strftime("%B %Y"))
        description = experience.get('description', '')

        st.markdown(f"### {position} at {company}")
        with st.form(key=f"edit_experience_{idx}"):
            company = st.text_input("Company Name", value=company)
            position = st.text_input("Position", value=position)
            try:
                start_date_obj = datetime.strptime(start_date, "%B %Y")
            except ValueError:
                start_date_obj = datetime.now()
            
            try:
                end_date_obj = datetime.strptime(end_date, "%B %Y")
            except ValueError:
                end_date_obj = datetime.now()
                
            start_date = st.date_input("Start Date", value=start_date_obj)
            end_date = st.date_input("End Date", value=end_date_obj)
            description = st.text_area("Description", value=description)
            
            col1, col2 = st.columns(2)
            with col1:
                if st.form_submit_button("Update"):
                    if company and position:  # Validate required fields
                        st.session_state.experiences[idx] = {
                            "company": company,
                            "position": position,
                            "start_date": start_date.strftime("%B %Y"),
                            "end_date": end_date.strftime("%B %Y"),
                            "description": description
                        }
                        st.success("Experience updated successfully!")
                    else:
                        st.error("Please fill in both Company Name and Position.")
            
            with col2:
                if st.form_submit_button("Delete"):
                    st.session_state.experiences.pop(idx)
                    st.success("Experience deleted successfully!")
        
        st.divider()
