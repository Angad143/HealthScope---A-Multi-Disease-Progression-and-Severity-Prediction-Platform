import streamlit as st
from utils.Diabetes import show_diabetes_page
from utils.Heart import show_heart_page
from utils.Kidney import show_kidney_page
from utils.About import show_about_page
from utils.Disease_Details import show_disease_details_page
# from AI_Chatbot.AI_Assistant_Gemini import show_ai_assistant_gemini_page
from AI_Chatbot.AI_Assistant_DeepSeek import show_ai_assistant_deepseek_page
# from AI_Chatbot.AI_Assistant_Gemini_02 import show_ai_assistant_gemini_02_page

# Set page config
st.set_page_config(
    page_title="HealthScope",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for navigation
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# Define function to update session state
def set_page(page_name):
    st.session_state.current_page = page_name


# Custom CSS for styling
st.markdown("""
<style>
    /* Project title in sidebar */
    .sidebar-title {
        color: #128DAC;
        font-size: 1.8rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
        padding: 1rem;
        background: linear-gradient(90deg, rgba(18,141,172,0.1), rgba(255,50,50,0.1));
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    /* Main title styling */
    .title {
        color: #128DAC;
        background: linear-gradient(90deg, rgba(18,141,172,0.1), rgba(50,200,100,0.1), rgba(255,50,50,0.1));
        text-align: center;
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        padding: 0.5rem;
    }
    
    /* Subheader styling */
    .subheader {
        color: #128DAC;
        text-align: center;
        font-size: 1.8rem;
        font-weight: 500;
        margin-bottom: 2.5rem;
        background: linear-gradient(90deg, rgba(18,141,172,0.1), rgba(255,50,50,0.1));
    }
    
    /* Feature icons */
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        color: #227A90;
    }
    
    /* About section */
    .about-section {
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 1.5rem;
        color: #128DAC;
        font-size: 0.9rem;
        margin-top: 2rem;
        border-top: 1px solid #E9ECEF;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .title {
            font-size: 2.5rem;
        }
        .subheader {
            font-size: 1.3rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Sidebar with project title
# Sidebar Navigation
with st.sidebar:
    st.markdown("""
    <div class="sidebar-title">
        HealthScope<br>
        <span style="font-size: 1.2rem; font-weight: 200;">
        A Multi-Disease Progression<br>
        and Severity Prediction Platform
        </span>
    </div>
    """, unsafe_allow_html=True)

    # Navigation buttons using session state
    if st.button("🏠 Home", key="home", help="Return to main page", use_container_width=True):
        set_page("Home") # navigate_to("Home")

    if st.button("ℹ️ About", key="about", help="Return to about section of Project", use_container_width=True):
        set_page("About")  # navigate_to("About")

    if st.button("📌 Disease Details", key="sidebar_disease_details", help="Click to view detailed information about Diabetes, Heart and Kidney Disease.", use_container_width=True):
        set_page("Disease_Details")  # navigate_to("Disease_Details")

    if st.button("🩺 Diabetes Prediction", key="sidebar_diabetes", help="Predict risk of diabetes", use_container_width=True):
        set_page("Diabetes") # navigate_to("Diabetes")

    if st.button("💓 Heart Disease Prediction", key="sidebar_heart", help="Predict risk of heart disease", use_container_width=True):
        set_page("Heart") # navigate_to("Heart")

    if st.button("🧬 Kidney Disease Prediction", key="sidebar_kidney", help="Predict risk of kidney disease", use_container_width=True):
        set_page("Kidney") # navigate_to("Kidney")

    # if st.button("🤖 AI Health Assistant", key="sidebar_ai_assistant", help="Ask me anything about diseases, I am your AI Assistant chatbot.", use_container_width=True):
    #     set_page("AI_Assistant_Gemini")  # Navigate to AI Assistant page

    if st.button("🤖 AI Health Assistant", key="sidebar_ai_assistant", help="Ask me anything about diseases, I am your AI Assistant chatbot.", use_container_width=True):
        set_page("AI_Assistant_DeepSeek")  # Navigate to AI Assistant page

    # if st.button("🤖 AI Health Assistant", key="sidebar_ai_assistant", help="Ask me anything about diseases, I am your AI Assistant chatbot.", use_container_width=True):
    #     set_page("AI_Assistant_Gemini_02")  # Navigate to AI Assistant page


    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; margin-top: 2rem;">
        <p style="font-size: 0.9rem; color: #128DAC;">Version 2.0.0</p>
        <p style="font-size: 0.8rem; color: #128DAC;">© 2025 HealthScope</p>
        <p style="font-size: 0.8rem; color: #128DAC;">Developed with ❤️ by Medical AI Team</p>

    </div>
    """, unsafe_allow_html=True)

# Display selected page
if st.session_state.current_page == "Home":

            # Main content
            st.markdown('<div class="title">🫀🩸HealthScope🩸🫀</div>', unsafe_allow_html=True)
            st.markdown('<div class="subheader">Advanced Multi-Disease Progression and Severity Prediction Platform</div>', unsafe_allow_html=True)

            # Hero image
            st.image("https://wallpaperaccess.com/full/136949.jpg", 
                    use_column_width=True, 
                    caption="Your Health, Our Priority")

            # Navigation buttons with icons
            col1, col2, col3 = st.columns(3)

            with col1:
                    if st.button("🩺 Diabetes Prediction", key="diabetes", help="Predict risk of diabetes"):
                        set_page("Diabetes")

            with col2:
                    if st.button("💓 Heart Disease Prediction", key="heart", help="Predict risk of heart disease"):
                        set_page("Heart")

            with col3:
                    if st.button("🧬 Kidney Disease Prediction", key="kidney", help="Predict risk of kidney disease"):
                        set_page("Kidney")


            # Features section
            st.markdown("## 🚀 Key Features")
            features = st.columns(3)

            with features[0]:
                st.markdown("""
                <div style="text-align: center; padding: 1.5rem; border-radius: 10px; background: #0F78A5; margin: 0.5rem;">
                    <div class="feature-icon">🔍</div>
                    <h3>Comprehensive Analysis</h3>
                    <p>Detailed risk assessment using advanced machine learning models</p>
                </div>
                """, unsafe_allow_html=True)

            with features[1]:
                st.markdown("""
                <div style="text-align: center; padding: 1.5rem; border-radius: 10px; background: #0F78A5; margin: 0.5rem;">
                    <div class="feature-icon">⚡</div>
                    <h3>Quick Results</h3>
                    <p>Get instant predictions with just a few clicks</p>
                </div>
                """, unsafe_allow_html=True)

            with features[2]:
                st.markdown("""
                <div style="text-align: center; padding: 1.5rem; border-radius: 10px; background: #0F78A5; margin: 0.5rem;">
                    <div class="feature-icon">🔒</div>
                    <h3>Data Privacy</h3>
                    <p>Your health data remains confidential and secure</p>
                </div>
                """, unsafe_allow_html=True)

            # About section
            st.markdown("""
            <div class="about-section">
                <h2>🧠 About Health Scope</h2>
                <p>HealthScope is a smart healthcare platform that uses machine learning to assess your risk for chronic diseases. It analyzes your health data and symptoms to give you personalized insights.</p>
                <h3>📌 Key Features:</h3>
                <ul>
                    <li><strong>Risk Assessment:</strong> Check your risk for diabetes, heart disease, and kidney disease in one place.</li>
                    <li><strong>Early Detection:</strong> Identify potential health issues before they get serious.</li>
                    <li><strong>Easy to Use:</strong> A simple and intuitive design for everyone.</li>
                    <li><strong>Secure Data:</strong> Your health information stays private and protected.</li>
                </ul>
                <h3>🔄 How It Works:</h3>
                <ol>
                    <li>Select a health condition to assess.</li>
                    <li>Enter your symptoms and medical details.</li>
                    <li>Get instant risk analysis with clear results.</li>
                    <li>Consult a doctor for expert advice.</li>
                </ol>
                <h4>⚠️ Important Disclaimer:</h4>
                <p>HealthScope provides only risk assessments and does not replace medical advice. Always consult a doctor for health concerns.</p>
            </div>
            """, unsafe_allow_html=True)

            # Footer
            st.markdown("""
            <div class="footer">
                <p>© 2025 HealthScope | Developed with ❤️ by Medical AI Team | Version 2.0.0</p>
                <p style="font-size: 0.8rem; margin-top: 0.5rem;">For research and educational purposes only</p>
            </div>
            """, unsafe_allow_html=True)

elif st.session_state.current_page == "About":
    show_about_page()

elif st.session_state.current_page == "Disease_Details":
    show_disease_details_page()

elif st.session_state.current_page == "Diabetes":
    show_diabetes_page()

elif st.session_state["current_page"] == "Heart":
    show_heart_page()

elif st.session_state["current_page"] == "Kidney":
    show_kidney_page()

# elif st.session_state["current_page"] == "AI_Assistant_Gemini":
#     show_ai_assistant_gemini_page()

elif st.session_state["current_page"] == "AI_Assistant_DeepSeek":
    show_ai_assistant_deepseek_page()

# elif st.session_state["current_page"] == "AI_Assistant_Gemini_02":
#     show_ai_assistant_gemini_02_page()
