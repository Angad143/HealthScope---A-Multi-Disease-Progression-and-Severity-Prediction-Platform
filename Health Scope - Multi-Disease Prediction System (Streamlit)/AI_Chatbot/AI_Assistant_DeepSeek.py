import streamlit as st
from openai import OpenAI
from datetime import datetime

def show_ai_assistant_deepseek_page():
    # Streamlit app title with gradient background
    st.markdown(
        """
        <style>
            .title-container {
                background: linear-gradient(90deg, rgba(18,141,172,0.1), rgba(50,200,100,0.1), rgba(255,50,50,0.1));
                padding: 15px;
                border-radius: 10px;
                text-align: center;
            }
            .title-text {
                color: #128DAC;
                font-size: 36px;
                font-weight: bold;
            }
        </style>
        <div class="title-container">
            <h1 class="title-text">🤖 Your AI-Powered Health Companion 🤖</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Read API key
    try:
        with open("AI_Chatbot/KEYS/deepseek.txt") as f:
            api_key = f.read().strip()
            if not api_key:
                st.error("API key is empty. Please check your deepseek.txt file.")
                st.stop()
    except FileNotFoundError:
        st.error("API key file not found. Please ensure the path is correct.")
        st.stop()
    except Exception as e:
        st.error(f"Error reading API key: {str(e)}")
        st.stop()

    # Initialize OpenAI client with OpenRouter
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    # Model configuration
    model_name = "deepseek/deepseek-chat-v3-0324:free"
    
    # Initialize chat history with welcome message if empty
    if "chat_history" not in st.session_state:
        welcome_msg = """
        Hello! I'm your AI Health Companion. I can help with:
        - Symptom analysis
        - General medical information
        - Health recommendations
        - Medication guidance

        Please note: I'm not a substitute for professional medical advice. 
        For emergencies, contact local emergency services immediately.
        """
        st.session_state.chat_history = [
            {"role": "assistant", "content": welcome_msg, "timestamp": datetime.now().isoformat()}
        ]
        st.session_state.trigger_response = False

    # Process button clicks first
    if "trigger_response" not in st.session_state:
        st.session_state.trigger_response = False
    
    # Quick Health Tools section with blue buttons
    st.markdown("<h2 style='color: #128DAC;'>🛠️ Quick Health Tools</h2>", unsafe_allow_html=True)
    col1, col2, col3, col4= st.columns(4)
    
    with col1:
        if st.button("💊 Medication Info", key="med_button"):
            st.session_state.chat_history.append({
                "role": "user",
                "content": "Please provide information about a medication.",
                "timestamp": datetime.now().isoformat()
            })
            st.session_state.trigger_response = True
            st.rerun()
    
    with col2:
        if st.button("🤒 Symptom Checker", key="symp_button"):
            st.session_state.chat_history.append({
                "role": "user",
                "content": "I'd like to check some symptoms. Can you help?",
                "timestamp": datetime.now().isoformat()
            })
            st.session_state.trigger_response = True
            st.rerun()
    
    with col3:
        if st.button("🍏 Health Tips", key="health_button"):
            st.session_state.chat_history.append({
                "role": "user",
                "content": "Please provide some general health tips.",
                "timestamp": datetime.now().isoformat()
            })
            st.session_state.trigger_response = True
            st.rerun()

    with col4:
        if st.button("🏥 Find Doctors", key="doctor_button"):
            st.session_state.chat_history.append({
                "role": "user",
                "content": "How can I find a specialist doctor for [condition]?",
                "timestamp": datetime.now().isoformat()
            })
            st.session_state.trigger_response = True
            st.rerun()

    # Apply blue button style to all buttons
    st.markdown("""
    <style>
        div[data-testid="stButton"] > button {
            background-color: #3a7bd5 !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 0.5rem 1rem !important;
            font-weight: 600 !important;
            width: 100% !important;
            transition: all 0.3s ease !important;
        }
        div[data-testid="stButton"] > button:hover {
            background-color: #2a6bc5 !important;
            transform: scale(1.02) !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # Show chat history
    for message in st.session_state.chat_history:
        st.chat_message(message["role"]).write(message["content"])
    
    # Generate AI response if triggered by button
    if st.session_state.trigger_response:
        last_message = st.session_state.chat_history[-1]
        if last_message["role"] == "user":
            try:
                with st.spinner("Generating response..."):
                    messages = [
                        {
                            "role": "system",
                            "content": """You are a medical AI assistant that provides:
                            - Only health-related information
                            - Responses in clean paragraphs
                            - Direct answers to medical questions
                            - Polite declines for non-health topics"""
                        }
                    ]
                    messages.extend([
                        {"role": msg["role"], "content": msg["content"]} 
                        for msg in st.session_state.chat_history[-6:] 
                        if msg["role"] != "system"
                    ])
                    
                    response = client.chat.completions.create(
                        model=model_name,
                        messages=messages,
                        temperature=0.7,
                        extra_headers={
                            "HTTP-Referer": "https://your-health-app.com",
                            "X-Title": "Health Companion"
                        }
                    )
                    
                    ai_response = response.choices[0].message.content
                    
                    st.session_state.chat_history.append({
                        "role": "assistant", 
                        "content": ai_response,
                        "timestamp": datetime.now().isoformat()
                    })
                    st.session_state.trigger_response = False
                    st.rerun()
                    
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": "Sorry, I'm having trouble responding. Please try again.",
                    "timestamp": datetime.now().isoformat()
                })
                st.session_state.trigger_response = False
                st.rerun()

    # Regular user input
    user_input = st.chat_input("Type your health question here...")
    
    if user_input:
        st.session_state.chat_history.append({
            "role": "user", 
            "content": user_input,
            "timestamp": datetime.now().isoformat()
        })
        st.session_state.trigger_response = True
        st.rerun()

if __name__ == "__main__":
    show_ai_assistant_deepseek_page()