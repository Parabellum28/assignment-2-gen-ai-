import os
import requests
from dotenv import load_dotenv

load_dotenv()

ollama_api_key = os.getenv("OLLAMA_API_KEY")

def query_api(prompt):
    try:
        headers = {}
        if ollama_api_key:
            headers["Authorization"] = f"Bearer {ollama_api_key}"

        response = requests.post(
            "http://localhost:11434/api/generate",
            headers=headers,
            json={
                "model": "phi3",
                "prompt": prompt,
                "stream": False
            },
            timeout=30
        )

        if response.status_code >= 400:
            return f"Error {response.status_code}: {response.text}"

        data = response.json()
        if "response" in data:
            return data["response"]
        elif "results" in data and isinstance(data["results"], list) and len(data["results"]) > 0:
            return data["results"][0].get("text", "No text field")
        else:
            return str(data)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    user_prompt = input("Enter prompt: ")
    print(query_api(user_prompt))