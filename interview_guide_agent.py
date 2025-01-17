import os
from swarm import Swarm, Agent
from openai import OpenAI
from typing import Dict, List

# Initialize OpenAI client with API key
api = OpenAI(api_key="")

# Initialize Swarm client
client = Swarm(api)

def process_guidelines(raw_response: str) -> Dict[str, List[str]]:
    """Helper function to process the raw response into structured sections"""
    sections = {
        "technical_skills": [],
        "common_questions": [],
        "projects": [],
        "key_concepts": [],
        "behavioral_questions": [],
        "questions_to_ask": [],
        "research_topics": [],
        "preparation_timeline": []
    }

    current_section = None
    for line in raw_response.split('\n'):
        line = line.strip()
        if not line:
            continue

        # Check for section headers
        if "Technical Skills Required" in line:
            current_section = "technical_skills"
        elif "Common Interview Questions" in line:
            current_section = "common_questions"
        elif "Projects to Prepare" in line:
            current_section = "projects"
        elif "Key Concepts" in line:
            current_section = "key_concepts"
        elif "Behavioral Questions" in line:
            current_section = "behavioral_questions"
        elif "Questions to Ask" in line:
            current_section = "questions_to_ask"
        elif "Research Topics" in line:
            current_section = "research_topics"
        elif "Preparation Timeline" in line:
            current_section = "preparation_timeline"
        elif current_section and (line[0] in ['-', '•', '*'] or line[0].isdigit()):
            sections[current_section].append(line.lstrip('- •*1234567890. '))
    
    return sections

def generate_guidelines(job_title: str) -> Dict[str, List[str]]:
    """Function that will be called by the agent to generate guidelines"""
    prompt = f"""Generate a comprehensive interview preparation guide for a {job_title} position.
    Include the following sections:
    1. Technical Skills Required
    2. Common Interview Questions
    3. Projects to Prepare
    4. Key Concepts to Review
    5. Behavioral Questions to Expect
    6. Questions to Ask the Interviewer
    7. Research Topics
    8. Preparation Timeline
    
    Make each section detailed and specific to the role."""

    return prompt

# Create the Interview Guide Agent
interview_guide_agent = Agent(
    name="Interview Guide Agent",
    instructions="You are an expert career counselor and technical interviewer. Generate detailed interview guidelines based on the job description provided.",
    model="gpt-4",
    functions=[generate_guidelines]
)

def main():
    # Example usage
    job_description = "An AI Engineer designs, develops, and implements artificial intelligence systems and applications that can simulate human intelligence processes through the creation and validation of algorithms, neural networks, and other machine learning techniques."
    
    # Get the prompt from the agent
    prompt = generate_guidelines(job_description)
    
    # Use the prompt to get response from OpenAI
    response = api.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert career counselor and technical interviewer with deep knowledge of industry requirements and interview processes."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=2000
    )

    # Process the response
    result = process_guidelines(response.choices[0].message.content)
    
    # Print the results
    if result:
        print(f"\nInterview Preparation Guide for {job_description}\n")
        print("=" * 50)
        
        for section, items in result.items():
            if items:  # Only print sections that have items
                print(f"\n{section.replace('_', ' ').title()}:")
                print("-" * 30)
                for item in items:
                    print(f"• {item}")
                print()

if __name__ == "__main__":
    main() 