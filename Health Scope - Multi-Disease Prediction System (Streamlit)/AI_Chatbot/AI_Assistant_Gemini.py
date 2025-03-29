import streamlit as st
import google.generativeai as genai

def show_ai_assistant_gemini_page():
    
    # Streamlit app title with gradient background and color
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
            .subtitle-text {
                color: #128DAC;
                font-size: 24px;
                font-weight: bold;
            }
        </style>
        <div class="title-container">
            <h1 class="title-text">🤖 Your AI-Powered Health Companion 🤖</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # read api keys
    f = open("AI_Chatbot/KEYS/gemini.txt")
    key = f.read()

    # configure api key
    genai.configure(api_key= key)

    # call model
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction="You are an AI health assistant. You provide answers only to questions related to health, diseases, and medical concerns. If a user asks about unrelated topics, politely inform them that you specialize in health-related inquiries.")

    # main app
    st.markdown("<h2 style='color: #128DAC;'>💬 Ask anything about diseases, symptoms, healthcare, and medical guidance instantly!</h2>", unsafe_allow_html=True)

    # st.chat_message("ai").write("Hi! I'm your AI-powered Health Guide. How can I assist you with medical concerns, diseases, or healthcare tips today?")  

    # # if there is no chat history then
    # if "chat_history" not in st.session_state:
    #     st.session_state["chat_history"] = []
    
    # # finitialize the chat models
    # chat = model.start_chat(history= st.session_state["chat_history"])

    # for msg in chat.history:
    #     st.chat_message(msg.role).write(msg.parts[0].text)

    # human_prompt = st.chat_input("Ask me about health, diseases, symptoms, or medical advice...")

    # if human_prompt:
    #     st.chat_message("user").write(human_prompt)
    #     response = chat.send_message(human_prompt)
    #     st.chat_message("ai").write(response.text)
    #     st.session_state["chat_history"] = chat.history

    # Initialize chat history if not exists
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
        # Display initial greeting (not part of the API history)
        st.chat_message("assistant").write("Hi! I'm your AI-powered Health Guide. How can I assist you with medical concerns, diseases, or healthcare tips today?")

    # Function to convert between formats
    def get_gemini_history():
        gemini_history = []
        for msg in st.session_state["chat_history"]:
            # Convert our format to Gemini's format
            if msg["role"] == "user":
                gemini_history.append({
                    "role": "user",
                    "parts": [{"text": msg["parts"][0]["text"]}]
                })
            else:  # assistant/ai messages
                gemini_history.append({
                    "role": "model",
                    "parts": [{"text": msg["parts"][0]["text"]}]
                })
        return gemini_history

    # Initialize chat with properly formatted history
    chat = model.start_chat(history=get_gemini_history())

    # Display existing chat history
    for msg in st.session_state["chat_history"]:
        role = "assistant" if msg["role"] != "user" else "user"
        st.chat_message(role).write(msg["parts"][0]["text"])

    human_prompt = st.chat_input("Ask me about health, diseases, symptoms, or medical advice...")

    if human_prompt:
        # Display user message
        st.chat_message("user").write(human_prompt)
        
        # Get AI response
        response = chat.send_message(human_prompt)
        
        # Display AI response
        st.chat_message("assistant").write(response.text)
        
        # Update history in consistent format
        st.session_state["chat_history"].extend([
            {
                "role": "user",
                "parts": [{"text": human_prompt}]
            },
            {
                "role": "ai",
                "parts": [{"text": response.text}]
            }
        ])
    
