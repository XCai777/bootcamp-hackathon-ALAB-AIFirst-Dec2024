import openai
import streamlit as st

class AIAssistant:
    def __init__(self):
        openai.api_key = st.session_state.api_key
    
    def generate_objective(self, experience_data):
        prompt = f"Generate a professional objective based on the following work experience:\n\n{experience_data}"
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional resume writer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=100
        )
        
        return response.choices[0].message.content.strip()
    
    def suggest_skills(self, experience):
        prompt = f"Suggest relevant skills based on the following work experience:\n\n{experience}"
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a technical recruiter."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=150
        )
        
        return response.choices[0].message.content.strip()
    
    def enhance_description(self, description):
        prompt = f"Enhance this job description with action verbs and quantifiable achievements:\n\n{description}"
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Enhance job descriptions with action verbs and metrics."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6,
            max_tokens=200
        )
        
        return response.choices[0].message.content.strip()
