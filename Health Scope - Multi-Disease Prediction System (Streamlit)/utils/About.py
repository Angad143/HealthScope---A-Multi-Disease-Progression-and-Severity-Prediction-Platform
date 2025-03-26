import streamlit as st
def show_about_page():
        
        # About section header
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
                <h1 class="title-text">📖 About Health Scope 📖</h1>
            </div>
            """,
            unsafe_allow_html=True
        )
        # Input fields section with color
        st.markdown("<h2 style='color: #128DAC;'>🧠 About Health Scope</h2>", unsafe_allow_html=True)

        # **About Section**
        st.markdown("""
        <div class="about-section">
            <p>
                HealthScope is a smart healthcare platform that leverages machine learning to assess the risk of chronic diseases. 
                By analyzing your health data and symptoms, it provides personalized insights to help you stay ahead of potential health issues.
            </p>
            <h3>📌 Key Features:</h3>
            <ul>
                <li><strong>Risk Assessment:</strong> Check your risk for diabetes, heart disease, and kidney disease in one place.</li>
                <li><strong>Early Detection:</strong> Identify potential health issues before they become serious.</li>
                <li><strong>Easy to Use:</strong> A simple and intuitive design for all users.</li>
                <li><strong>Secure Data:</strong> Your health information remains private and protected.</li>
            </ul>
            <h3>🔄 How It Works:</h3>
            <ol>
                <li>Select a health condition to assess.</li>
                <li>Enter your symptoms and medical details.</li>
                <li>Receive an instant risk analysis with clear results.</li>
                <li>Consult a doctor for expert advice.</li>
            </ol>
            <h4>⚠️ Important Disclaimer:</h4>
            <p>
                HealthScope provides only risk assessments and does not replace medical advice. 
                Always consult a healthcare professional for diagnosis and treatment.
            </p>
        </div>
        """, unsafe_allow_html=True)

        # **Footer**
        st.markdown("""
        <div class="footer">
            <p>© 2025 HealthScope | Developed with ❤️ by Medical AI Team | Version 2.0.0</p>
            <p style="font-size: 0.8rem; margin-top: 0.5rem;">For research and educational purposes only</p>
        </div>
        """, unsafe_allow_html=True)
