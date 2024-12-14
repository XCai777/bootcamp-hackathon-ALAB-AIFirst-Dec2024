import streamlit as st
from datetime import datetime

def render_education():
    """Render education section"""
    
    st.subheader("Education")
    
    # Initialize education list in session state if it doesn't exist
    if 'education' not in st.session_state:
        st.session_state.education = []
    
    # Add new education
    st.subheader("Add Education", divider='gray')
    with st.form(key="education_form"):
        school = st.text_input("School/University")
        degree = st.text_input("Degree")
        major = st.text_input("Major")
        graduation_date = st.date_input("Graduation Date")
        gpa = st.number_input("GPA", min_value=0.0, max_value=4.0, step=0.1)
        honors = st.text_area("Honors/Awards", height=50)
        coursework = st.text_area("Relevant Coursework", height=50)
        
        if st.form_submit_button("Add Education"):
            if school and degree:  # Only add if required fields are filled
                new_education = {
                    "school": school,
                    "degree": degree,
                    "major": major,
                    "graduation_date": graduation_date,
                    "gpa": gpa,
                    "honors": honors,
                    "coursework": coursework
                }
                st.session_state.education.append(new_education)
                st.rerun()
            else:
                st.error("Please fill in both School and Degree.")
    
    # Display and edit existing education entries
    if st.session_state.education:
        st.subheader("Edit Education", divider='gray')
        
        # Create a list to track education entries to be deleted
        education_to_delete = []
        
        for idx, edu in enumerate(st.session_state.education):
            # Get values with defaults
            school = edu.get('school', 'No School')
            degree = edu.get('degree', 'No Degree')
            
            st.markdown(f"### {degree} at {school}")
            
            # Create delete button outside the form
            if st.button("Delete", key=f"delete_edu_{idx}"):
                education_to_delete.append(idx)
                st.rerun()
            
            with st.form(key=f"edit_education_{idx}"):
                school = st.text_input("School/University", value=edu.get('school', ''))
                degree = st.text_input("Degree", value=edu.get('degree', ''))
                major = st.text_input("Major", value=edu.get('major', ''))
                graduation_date = st.date_input("Graduation Date", value=edu.get('graduation_date'))
                gpa = st.number_input("GPA", value=edu.get('gpa', 0.0), min_value=0.0, max_value=4.0, step=0.1)
                honors = st.text_area("Honors/Awards", value=edu.get('honors', ''), height=50)
                coursework = st.text_area("Relevant Coursework", value=edu.get('coursework', ''), height=50)
                
                if st.form_submit_button("Update"):
                    if school and degree:  # Validate required fields
                        st.session_state.education[idx] = {
                            "school": school,
                            "degree": degree,
                            "major": major,
                            "graduation_date": graduation_date,
                            "gpa": gpa,
                            "honors": honors,
                            "coursework": coursework
                        }
                        st.success("Education updated successfully!")
                        st.rerun()
                    else:
                        st.error("Please fill in both School and Degree.")
            
            st.divider()
        
        # Remove education entries marked for deletion
        for idx in sorted(education_to_delete, reverse=True):
            st.session_state.education.pop(idx)
