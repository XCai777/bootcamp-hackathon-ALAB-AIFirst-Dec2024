import streamlit as st

def initialize_session_state():
    """Initialize session state variables with default values"""
    
    defaults = {
        # Resume Settings
        "theme_color": "#FF4800",
        "font_family": "Roboto",
        "font_size": 11,
        "size_preset": "Standard",
        "doc_format": "Letter (US, Canada)",
        
        # Personal Information
        "name": "",
        "email": "",
        "phone": "",
        "location": "",
        "website": "",
        "profile_picture": None,
        "github": "",
        "twitter": "",
        "languages": [{"language": "", "proficiency": ""}],
        
        # Sections
        "objective": "",
        "experiences": [],
        "education": [],
        "projects": [],
        "skills": [],
        "additional_info": {
            "volunteer_work": [],
            "interests": [],
            "publications": [],
            "awards": []
        }
    }
    
    # Initialize all default values in session state
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value