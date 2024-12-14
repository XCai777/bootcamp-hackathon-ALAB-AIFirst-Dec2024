import streamlit as st

def render_resume_settings():
    """Render resume settings section"""
    
    # Theme Color
    st.subheader("Theme Color")
    colors = {
        "Orange": "#FF4800",
        "Blue": "#0066FF",
        "Green": "#00CC66",
        "Purple": "#6600FF",
        "Red": "#FF0066"
    }
    
    selected_color = st.color_picker(
        "Select theme color",
        value=st.session_state.get("theme_color", "#FF4800")
    )
    st.session_state.theme_color = selected_color
    
    # Font Settings
    st.subheader("Typography")
    
    # Font Family
    font_families = [
        "Roboto",
        "Lato",
        "Montserrat",
        "Open Sans",
        "Raleway",
        "Noto Serif",
        "Lora",
        "Roboto Slab",
        "Playfair Display",
        "Merriweather"
    ]
    
    selected_font = st.selectbox(
        "Font Family",
        options=font_families,
        index=font_families.index(st.session_state.get("font_family", "Roboto"))
    )
    st.session_state.font_family = selected_font
    
    # Font Size
    col1, col2 = st.columns(2)
    
    with col1:
        font_size = st.number_input(
            "Font Size (pt)",
            min_value=8,
            max_value=14,
            value=st.session_state.get("font_size", 11)
        )
        st.session_state.font_size = font_size
    
    with col2:
        size_preset = st.radio(
            "Size Preset",
            options=["Compact", "Standard", "Large"],
            index=1
        )
        st.session_state.size_preset = size_preset
    
    # Document Format
    st.subheader("Document Format")
    doc_format = st.radio(
        "Paper Size",
        options=[
            "Letter (US, Canada)",
            "A4 (other countries)"
        ],
        index=0
    )
    st.session_state.doc_format = doc_format