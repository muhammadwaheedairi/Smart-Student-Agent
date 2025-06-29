import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "HTTP-Referer": "http://localhost:8501",
    "X-Title": "SmartStudentAgent",
    "Content-Type": "application/json"
}

MODEL = "mistralai/mistral-7b-instruct"  # You can swap model here

def call_openrouter(prompt):
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=HEADERS, json=data)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"❌ Error: {response.status_code} - {response.text}"


def ask_academic_question(prompt):
    return call_openrouter(f"Answer this academic question in a clear and concise way: {prompt}")


def get_study_tips(topic):
    return call_openrouter(f"Give 5 study tips to master this topic: {topic}")


def summarize_text(text):
    return call_openrouter(f"Summarize the following text in simple bullet points:\n\n{text}")
