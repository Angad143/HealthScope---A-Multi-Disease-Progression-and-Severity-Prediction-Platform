import base64
import requests
from PIL import Image
from io import BytesIO
import re

# Load API Key securely from a file
with open("AI_Powered_Medical_Insights/KEYS/deepseek.txt", "r") as f:
    OPENROUTER_API_KEY = f.read().strip()

# OpenRouter endpoint
ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"

def clean_ai_response(text):
    """
    Cleans the AI response by removing markdown characters and normalizing spacing.
    """
    text = re.sub(r"[*#\-]+", "", text)
    text = re.sub(r"\n\s*\n", "\n\n", text.strip())
    text = re.sub(r"\n\s*", "\n", text)
    return text.strip()

def diagnose_image(image_file):
    """
    Analyzes the medical image and returns a clean diagnostic report or a fallback message.
    """
    try:
        # Convert image to base64
        image = Image.open(image_file)
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        # Diagnostic prompt
        prompt_text = """
        You are an AI healthcare assistant. Analyze the uploaded medical image, which may include visible signs of diseases or conditions related to the skin, eyes, leg, wounds, infections, injuries, inflammation, x-rays, or any external body part of a patient.

        Your goal is to assist in generating a clear, educational, and medically relevant diagnostic report suitable for educational or research purposes.

        Structure your response in clean, easy-to-read English using the following format:

        1. Diagnosis  
        2. Possible Causes  
        3. Recommended Treatments  
        4. Precautionary Measures  
        5. Medical Advice  
        6. Educational Note  

        Important Instructions:
        - Do not use any markdown symbols such as asterisks (*), dashes (-), or hashtags (#).  
        - Keep the response professional, simple, and readable for a general audience.
        - If the image does not appear to be a medical image of a patient (e.g., unrelated objects, documents, cartoons, random scenery, etc.), respond with:  
        "Sorry, I can only assist with human medical images such as skin conditions, wounds, infections, x-rays, or other visible health issues. Please upload a valid patient-related medical image."
        """

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        }

        data = {
            "model": "qwen/qwen2.5-vl-3b-instruct:free",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{img_str}"
                            },
                        },
                        {
                            "type": "text",
                            "text": prompt_text.strip()
                        },
                    ]
                }
            ]
        }

        # Send request
        response = requests.post(ENDPOINT, headers=headers, json=data)

        if response.status_code == 200:
            result = response.json()
            raw_reply = result["choices"][0]["message"]["content"]

            # Handle non-medical image response
            if "sorry" in raw_reply.lower():
                return "Sorry, I can only assist with medical images such as skin, eye, wound, x-ray etc. Please upload a valid medical image for diagnosis."

            return clean_ai_response(raw_reply)
        else:
            return f"Error: {response.status_code} - {response.text}"

    except Exception as e:
        return f"An error occurred: {str(e)}"
