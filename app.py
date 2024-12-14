import streamlit as st
from components.sidebar import render_sidebar
from components.preview import render_preview
from components.ai_assistant import AIAssistant
from utils.session_state import initialize_session_state
from utils.pdf_generator import generate_pdf
import json
from openai import OpenAI

st.set_page_config(
    page_title="AI Resume Builder",
    page_icon="📄",
    layout="wide"
)

def check_api_key(api_key):
    if not api_key:
        st.warning('Please enter your OpenAI API key!')
        return False
    
    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=5
        )
        return True
    except Exception as e:
        st.error('Invalid API key or API error occurred')
        return False

def main():
    # Initialize session state
    initialize_session_state()
    
    # API Key input in sidebar
    with st.sidebar:
        st.markdown("### OpenAI API Key")
        api_key = st.text_input("Enter your OpenAI API key:", type="password")
        if st.button("Validate API Key"):
            if check_api_key(api_key):
                st.session_state.api_key = api_key
                st.session_state.api_key_valid = True
                st.success("API key is valid!")
            else:
                st.session_state.api_key_valid = False
    
    # Page title
    st.title("AI Resume Builder")
    
    # Only show the main content if API key is valid
    if not st.session_state.get('api_key_valid', False):
        st.warning("Please enter a valid OpenAI API key in the sidebar to continue.")
        return
    
    # Create two columns for the layout
    left_col, right_col = st.columns([1, 1])
    
    # Add CSS to make left column scrollable
    st.markdown("""
        <style>
            .scrollable-column {
                height: calc(100vh - 200px);
                overflow-y: auto;
                padding-right: 20px;
                margin-bottom: 20px;
            }
            .action-buttons {
                margin-bottom: 20px;
            }
        </style>
    """, unsafe_allow_html=True)
    
    with left_col:
        # Create a div with scrollable class for the form inputs
        st.markdown('<div class="scrollable-column">', unsafe_allow_html=True)
        render_sidebar()  # This contains all the form inputs
        st.markdown('</div>', unsafe_allow_html=True)
    
    with right_col:
        # Action buttons at the top of the preview
        st.markdown('<div class="action-buttons">', unsafe_allow_html=True)
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
                saved_data = json.dumps(st.session_state.to_dict())
                st.session_state.saved_data = saved_data
                st.success("Resume data saved!")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Render the preview
        render_preview()

if __name__ == "__main__":
    main()
