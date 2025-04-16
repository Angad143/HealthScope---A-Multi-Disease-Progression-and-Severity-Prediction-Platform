import os
import re
from openai import OpenAI

class AIVoiceHealthAssistant:
    def __init__(self):
        self.api_key_path = "AI_Powered_Medical_Insights/KEYS/deepseek.txt"
        self.model_name = "nvidia/llama-3.1-nemotron-ultra-253b-v1:free"

    def get_api_key(self):
        try:
            if not os.path.exists(self.api_key_path):
                raise FileNotFoundError(f"API key not found at {self.api_key_path}")
            with open(self.api_key_path, 'r') as f:
                key = f.read().strip()
                if not key:
                    raise ValueError("API key is empty")
                return key
        except Exception as e:
            raise Exception(f"Error loading API key: {str(e)}")

    def clean_text(self, text):
        text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
        return text.replace('*', '').replace('_', '')

    def process_query(self, user_input):
        try:
            api_key = self.get_api_key()
            client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=api_key
            )

            messages = [
                {
                    "role": "system",
                    "content": """You are a helpful medical assistant.
            You only give health-related information.
            You do not answer non-medical questions.
            You always reply in plain text.
            You give short and simple answers."""
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]

            response = client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                temperature=0.7,
                extra_headers={
                    "HTTP-Referer": "https://your-health-app.com",
                    "X-Title": "Health Companion"
                }
            )

            return self.clean_text(response.choices[0].message.content)
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"
