import streamlit as st

def render_projects():
    """Render projects section"""
    
    st.subheader("Projects")
    
    # Initialize projects list in session state if it doesn't exist
    if 'projects' not in st.session_state:
        st.session_state.projects = []
    
    # Add new project
    st.subheader("Add Project", divider='gray')
    with st.form(key="project_form"):
        name = st.text_input("Project Name")
        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date")
        description = st.text_area("Description")
        technologies = st.text_input("Technologies Used")
        url = st.text_input("Project URL")
        
        if st.form_submit_button("Add Project"):
            if name:  # Only add if required fields are filled
                new_project = {
                    "name": name,
                    "start_date": start_date,
                    "end_date": end_date,
                    "description": description,
                    "technologies": technologies,
                    "url": url
                }
                st.session_state.projects.append(new_project)
                st.rerun()  # Rerun to refresh the page after adding
            else:
                st.error("Please fill in the Project Name.")
    
    # Display and edit existing projects
    if st.session_state.projects:
        st.subheader("Edit Projects", divider='gray')
        
        # Create a list to track projects to be deleted
        projects_to_delete = []
        
        for idx, project in enumerate(st.session_state.projects):
            st.markdown(f"### {project.get('name', 'Untitled Project')}")
            
            # Create delete button outside the form
            if st.button("Delete", key=f"delete_proj_{idx}"):
                projects_to_delete.append(idx)
                st.rerun()
            
            with st.form(key=f"edit_project_{idx}"):
                name = st.text_input("Project Name", value=project.get("name", ""))
                start_date = st.date_input("Start Date", value=project.get("start_date"))
                end_date = st.date_input("End Date", value=project.get("end_date"))
                description = st.text_area("Description", value=project.get("description", ""))
                technologies = st.text_input("Technologies Used", value=project.get("technologies", ""))
                url = st.text_input("Project URL", value=project.get("url", ""))
                
                if st.form_submit_button("Update"):
                    if name:  # Validate required fields
                        st.session_state.projects[idx] = {
                            "name": name,
                            "start_date": start_date,
                            "end_date": end_date,
                            "description": description,
                            "technologies": technologies,
                            "url": url
                        }
                        st.success("Project updated successfully!")
                        st.rerun()
                    else:
                        st.error("Please fill in the Project Name.")
            
            st.divider()
        
        # Remove projects marked for deletion
        for idx in sorted(projects_to_delete, reverse=True):
            st.session_state.projects.pop(idx)
