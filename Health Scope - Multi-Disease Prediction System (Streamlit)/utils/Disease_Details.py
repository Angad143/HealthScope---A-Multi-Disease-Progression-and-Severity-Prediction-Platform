import streamlit as st
def show_disease_details_page():
        # Disease Details header
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
                    <h1 class="title-text">🏥 Explore Disease Details - Health Scope 🏥</h1>
                </div>
                """,
                unsafe_allow_html=True
        )
        # Disease details with color
        st.markdown("<h2 style='color: #128DAC;'>🔍 Health Scope - Your Guide to Disease Insights</h2>", unsafe_allow_html=True)
        st.write("Explore detailed information about various health conditions and their potential risks.")
        
        disease_info = {
            "Diabetes": {
                "Description": "A chronic disease that affects how your body turns food into energy.",
                "Symptoms": ["Frequent urination", "Increased thirst", "Unexplained weight loss", "Fatigue"],
                "Causes": ["Genetics", "Obesity", "Lack of exercise", "Unhealthy diet"],
                "Prevention": ["Regular exercise", "Healthy diet", "Weight management", "Regular checkups"]
            },
            "Heart Disease": {
                "Description": "A range of conditions that affect the heart, including coronary artery disease and heart attacks.",
                "Symptoms": ["Chest pain", "Shortness of breath", "Fatigue", "Irregular heartbeat"],
                "Causes": ["High blood pressure", "Smoking", "High cholesterol", "Diabetes"],
                "Prevention": ["Regular exercise", "Healthy diet", "Avoid smoking", "Manage stress"]
            },
            "Kidney Disease": {
                "Description": "A condition where the kidneys lose their ability to function properly.",
                "Symptoms": ["Swelling in legs", "Fatigue", "Shortness of breath", "Blood in urine"],
                "Causes": ["Diabetes", "High blood pressure", "Chronic infections", "Genetic factors"],
                "Prevention": ["Control blood sugar", "Monitor blood pressure", "Healthy diet", "Stay hydrated"]
            }
        }
        
        for disease, details in disease_info.items():
            st.subheader(disease)
            st.write(f"**Description:** {details['Description']}")
            
            st.write("**Symptoms:**")
            st.markdown("\n".join([f"- {symptom}" for symptom in details["Symptoms"]]))
            
            st.write("**Causes:**")
            st.markdown("\n".join([f"- {cause}" for cause in details["Causes"]]))
            
            st.write("**Prevention:**")
            st.markdown("\n".join([f"- {prevention}" for prevention in details["Prevention"]]))
            
            st.write("---")

                # **Footer**
        st.markdown("""
        <div class="footer">
            <p>© 2025 HealthScope | Developed with ❤️ by Medical AI Team | Version 2.0.0</p>
            <p style="font-size: 0.8rem; margin-top: 0.5rem;">For research and educational purposes only</p>
        </div>
        """, unsafe_allow_html=True)
