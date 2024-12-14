import streamlit as st
from components.sidebar import render_sidebar
from components.preview import render_preview
from components.ai_assistant import AIAssistant
from utils.session_state import initialize_session_state
from utils.pdf_generator import generate_pdf
import json

st.set_page_config(
    page_title="AI Resume Builder",
    page_icon="📄",
    layout="wide"
)

def main():
    # Initialize session state
    initialize_session_state()
    
    # Page title
    st.title("AI Resume Builder")
    
    # Create two columns for the layout
    left_col, right_col = st.columns([1, 1])
    
    with left_col:
        # Render the input form
        render_sidebar()
        
        # Add download and save buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Download Resume", type="primary"):
                pdf_file = generate_pdf(st.session_state)
                st.download_button(
                    label="Download PDF",
                    data=pdf_file,
                    file_name="resume.pdf",
                    mime="application/pdf"
                )
        with col2:
            if st.button("Save", type="secondary"):
                # Save to session state
                saved_data = json.dumps(st.session_state.to_dict())
                st.session_state.saved_data = saved_data
                st.success("Resume data saved!")
    
    with right_col:
        # Render the preview
        render_preview()

if __name__ == "__main__":
    main()