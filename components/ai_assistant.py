from openai import OpenAI
import streamlit as st

class AIAssistant:
    def __init__(self):
        self.client = OpenAI(api_key=st.session_state.api_key)

    def generate_objective(self, experience_data):
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional resume writer. Create a concise and impactful career objective."
                },
                {
                    "role": "user",
                    "content": f"Create a professional career objective based on this experience: {experience_data}"
                }
            ],
            max_tokens=100,
            temperature=0.7
        )
        return response.choices[0].message.content

    def enhance_text(self, text, context=""):
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional resume writer. Enhance the given text to be more professional and impactful."
                },
                {
                    "role": "user",
                    "content": f"Enhance this text for a resume {context}: {text}"
                }
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content

    def generate_summary(self, experience_data):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional resume writer. Create a concise and impactful professional summary."
                },
                {
                    "role": "user",
                    "content": f"Create a professional summary based on this experience: {experience_data}"
                }
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content
