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
    
    # Create the form for adding new education
    with st.form(key="add_education_form"):
        school = st.text_input("School/University")
        degree = st.text_input("Degree")
        major = st.text_input("Major")
        graduation_date = st.date_input("Graduation Date")
        gpa = st.number_input("GPA", min_value=0.0, max_value=4.0, step=0.1)
        honors = st.text_area("Honors/Awards")
        coursework = st.text_area("Relevant Coursework")
        
        if st.form_submit_button("Add Education"):
            if school and degree:  # Only add if required fields are filled
                new_education = {
                    "school": school,
                    "degree": degree,
                    "major": major,
                    "graduation_date": graduation_date.strftime("%B %Y"),
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
            
            with st.form(key=f"edit_education_form_{idx}"):
                school = st.text_input("School/University", value=edu.get('school', ''), key=f"school_{idx}")
                degree = st.text_input("Degree", value=edu.get('degree', ''), key=f"degree_{idx}")
                major = st.text_input("Major", value=edu.get('major', ''), key=f"major_{idx}")
                
                try:
                    grad_date_obj = datetime.strptime(edu.get('graduation_date'), "%B %Y")
                except (ValueError, TypeError):
                    grad_date_obj = datetime.now()
                    
                graduation_date = st.date_input("Graduation Date", value=grad_date_obj, key=f"grad_date_{idx}")
                gpa = st.number_input("GPA", value=edu.get('gpa', 0.0), min_value=0.0, max_value=4.0, step=0.1, key=f"gpa_{idx}")
                honors = st.text_area("Honors/Awards", value=edu.get('honors', ''), key=f"honors_{idx}")
                coursework = st.text_area("Relevant Coursework", value=edu.get('coursework', ''), key=f"coursework_{idx}")
                
                if st.form_submit_button("Update"):
                    if school and degree:  # Validate required fields
                        st.session_state.education[idx] = {
                            "school": school,
                            "degree": degree,
                            "major": major,
                            "graduation_date": graduation_date.strftime("%B %Y"),
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
