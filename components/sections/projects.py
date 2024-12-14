import streamlit as st

def render_projects():
    """Render projects section"""
    
    st.subheader("Projects")
    
    projects = st.session_state.get("projects", [])
    
    for i, project in enumerate(projects):
        with st.expander(f"Project {i+1}", expanded=True):
            project["name"] = st.text_input("Project Name", value=project.get("name", ""), key=f"proj_name_{i}")
            
            col1, col2 = st.columns(2)
            with col1:
                project["start_date"] = st.date_input("Start Date", value=project.get("start_date"), key=f"proj_start_{i}")
            with col2:
                project["end_date"] = st.date_input("End Date", value=project.get("end_date"), key=f"proj_end_{i}")
            
            project["description"] = st.text_area("Description", value=project.get("description", ""), key=f"proj_desc_{i}", height=100)
            project["technologies"] = st.text_input("Technologies Used", value=project.get("technologies", ""), key=f"proj_tech_{i}")
            project["url"] = st.text_input("Project URL", value=project.get("url", ""), key=f"proj_url_{i}")
            
            if st.button("Remove Project", key=f"remove_proj_{i}"):
                projects.pop(i)
                st.experimental_rerun()
    
    if st.button("Add Project"):
        projects.append({})
        st.experimental_rerun()
    
    st.session_state.projects = projects