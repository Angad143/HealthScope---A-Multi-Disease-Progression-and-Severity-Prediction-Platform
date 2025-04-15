import os
import re
from openai import OpenAI
from datetime import datetime

class AIHealthAssistant:
    def __init__(self):
        self.api_key_path = "AI_Powered_Medical_Insights/KEYS/deepseek.txt"
        self.model_name = "nvidia/llama-3.1-nemotron-ultra-253b-v1:free"
        self.welcome_message = """
        Hello! I'm your AI Health Companion. I can help with:
        - Symptom analysis
        - General medical information
        - Health recommendations
        - Medication guidance

        Please note: I'm not a substitute for professional medical advice. 
        For emergencies, contact local emergency services immediately.
        """
    
    def initialize_chat_history(self, session):
        """Initialize chat history in session if not exists"""
        if 'chat_history' not in session:
            session['chat_history'] = [
                {
                    "role": "assistant", 
                    "content": self.welcome_message,
                    "timestamp": datetime.now().isoformat()
                }
            ]
        return session['chat_history']
    
    def get_api_key(self):
        """Read API key from file"""
        try:
            if not os.path.exists(self.api_key_path):
                raise FileNotFoundError(f"API key file not found at {self.api_key_path}")
            
            with open(self.api_key_path) as f:
                api_key = f.read().strip()
                if not api_key:
                    raise ValueError("API key is empty")
                return api_key
                
        except Exception as e:
            raise Exception(f"Error reading API key: {str(e)}")
    
    def create_openai_client(self, api_key):
        """Create OpenAI client with OpenRouter"""
        return OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key
        )
    
    def clean_response(self, text):
        """Remove markdown formatting from response"""
        # Remove **bold** markers
        text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
        # Remove other markdown if needed
        text = text.replace('*', '').replace('_', '')
        return text
    
    def generate_ai_response(self, chat_history):
        """Generate AI response using model"""
        try:
            # First add "Generating response..." message
            generating_msg = {
                "role": "assistant",
                "content": "Generating response...",
                "timestamp": datetime.now().isoformat(),
                "temporary": True  # Mark as temporary message
            }
            chat_history.append(generating_msg)
            
            api_key = self.get_api_key()
            client = self.create_openai_client(api_key)
            
            messages = [
                {
                    "role": "system",
                    "content": """You are a medical AI assistant that provides:
                    - Only health-related information
                    - Responses in clean paragraphs without markdown formatting
                    - Direct answers to medical questions
                    - Polite declines for non-health topics"""
                }
            ]
            
            # Add last 6 messages (excluding system and temporary messages)
            messages.extend([
                {"role": msg["role"], "content": msg["content"]} 
                for msg in chat_history[-6:] 
                if msg["role"] != "system" and not msg.get("temporary")
            ])
            
            response = client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                temperature=0.7,
                extra_headers={
                    "HTTP-Referer": "https://your-health-app.com",
                    "X-Title": "Health Companion"
                }
            )
            
            # Remove the temporary "Generating..." message
            if chat_history and chat_history[-1].get("temporary"):
                chat_history.pop()
            
            # Clean the response
            cleaned_response = self.clean_response(response.choices[0].message.content)
            return cleaned_response
            
        except Exception as e:
            # Remove the temporary "Generating..." message if error occurs
            if chat_history and chat_history[-1].get("temporary"):
                chat_history.pop()
            return f"Sorry, I'm having trouble responding. Error: {str(e)}"
    
    def handle_user_input(self, session, user_input=None, button_clicked=None):
        """Process user input and generate response"""
        chat_history = session.get('chat_history', [])
        
        # Handle button clicks
        button_messages = {
            'med_button': "Please provide information about a medication.",
            'symp_button': "I'd like to check some symptoms. Can you help?",
            'health_button': "Please provide some general health tips.",
            'doctor_button': "How can I find a specialist doctor for [condition]?"
        }
        
        if button_clicked and button_clicked in button_messages:
            chat_history.append({
                "role": "user",
                "content": button_messages[button_clicked],
                "timestamp": datetime.now().isoformat()
            })
        elif user_input:
            chat_history.append({
                "role": "user", 
                "content": user_input,
                "timestamp": datetime.now().isoformat()
            })
        
        # Generate AI response if there's new user input
        if button_clicked or user_input:
            ai_response = self.generate_ai_response(chat_history)
            chat_history.append({
                "role": "assistant", 
                "content": ai_response,
                "timestamp": datetime.now().isoformat()
            })
        
        session['chat_history'] = chat_history
        return chat_history