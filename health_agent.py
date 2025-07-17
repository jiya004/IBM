import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env and API key
load_dotenv()
API_key = os.getenv('API_KEY')
genai.configure(api_key=API_key)

# Gemini model
model = genai.GenerativeModel('models/gemini-1.5-flash')

# Function to generate health prediction + recommendations
def generate_health_advice(age, bmi, bp, glucose):
    prompt = f"""
You are a healthcare AI assistant. A patient has entered the following details:
- Age: {age}
- BMI: {bmi}
- Blood Pressure: {bp}
- Glucose Level: {glucose}

Your task:
1. Predict the likelihood of developing chronic diseases such as diabetes, heart disease, or cancer.
2. Mention the risk level (Low / Moderate / High) and explain briefly why.
3. Provide 3 personalized health recommendations to improve the patient’s lifestyle and reduce their risk.
Make your answer easy to understand and user-friendly.
    """

    response = model.generate_content(prompt)
    return response.text.strip()
