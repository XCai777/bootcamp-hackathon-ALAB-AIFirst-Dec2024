import openai
import requests
from bs4 import BeautifulSoup


class LinkedInProfileScraper:
    """
    A scraper to fetch LinkedIn profiles based on a job description.
    """

    def __init__(self, openai_api_key: str):
        """
        Initialize the scraper with the OpenAI API key.
        """
        self.openai_api_key = openai_api_key

    def extract_keywords(self, job_description: str) -> str:
        """
        Extract keywords or a summary using OpenAI API.

        Args:
            job_description (str): The job description to process.

        Returns:
            str: Extracted keywords or summary.
        """
        openai.api_key = self.openai_api_key
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"Extract key skills, roles, and company names from this job description:\n{job_description}",
                },
            ],
            max_tokens=100,
            temperature=0.5,
        )
        return response["choices"][0]["message"]["content"].strip()

    def search_profiles(self, keywords: str) -> list:
        """
        Search LinkedIn profiles using BeautifulSoup to scrape Google search results.

        Args:
            keywords (str): Keywords to search for.

        Returns:
            list: List of profile URLs (limited to 5).
        """
        # Encode the search query
        query = f"site:linkedin.com {keywords}".replace(" ", "+")
        url = f"https://www.google.com/search?q={query}"

        # Send the GET request
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)

        # Check for successful response
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return []

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.find_all("a")

        # Extract LinkedIn profile URLs
        profiles = []
        for link in results:
            href = link.get("href")
            if href and "linkedin.com" in href:
                # Clean the URL
                if "/url?q=" in href:
                    href = href.split("/url?q=")[1].split("&")[0]
                profiles.append(href)

            # Stop when we have 5 profiles
            if len(profiles) >= 5:
                break

        return profiles

    def get_profiles(self, job_description: str) -> list:
        """
        Fetch LinkedIn profiles based on the job description.

        Args:
            job_description (str): The job description to process.

        Returns:
            list: List of LinkedIn profile URLs (limited to 5).
        """
        keywords = self.extract_keywords(job_description)
        profiles = self.search_profiles(keywords)
        return profiles


# Example Usage
if __name__ == "__main__":
    # Replace with your OpenAI API key
    OPENAI_API_KEY = "your_openai_api_key"

    scraper = LinkedInProfileScraper(openai_api_key=OPENAI_API_KEY)

    # Example Job Description
    job_description = """
    We are looking for a Software Engineer with experience in Python, web development, 
    and cloud infrastructure (AWS or Azure). Proficiency in APIs and microservices is a must.
    """

    # Fetch profiles
    profiles = scraper.get_profiles(job_description)

    # Display the results
    print("Relevant LinkedIn Profiles:")
    for profile in profiles:
        print(profile)
