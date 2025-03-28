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

    st.chat_message("ai").write("Hi there! I am helpful AI assistant. How can I help you today?")

    # if there is no chat history then
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
    
    # finitialize the chat models
    chat = model.start_chat(history= st.session_state["chat_history"])

    for msg in chat.history:
        st.chat_message(msg.role).write(msg.parts[0].text)

    human_prompt = st.chat_input("Say something...")

    if human_prompt:
        st.chat_message("user").write(human_prompt)
        response = chat.send_message(human_prompt)
        st.chat_message("ai").write(response.text)
        st.session_state["chat_history"] = chat.history
