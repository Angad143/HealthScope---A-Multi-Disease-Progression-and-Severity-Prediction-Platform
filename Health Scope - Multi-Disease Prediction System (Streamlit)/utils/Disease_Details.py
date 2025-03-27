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
            .disease-card {
                background: rgba(86, 74, 74, 0.76);
                border-radius: 10px;
                margin-bottom: 10px;
            }
            .disease-title {
                color: #128DAC;
                font-size: 30px;
                margin-bottom: 10px;
                Text-align: center;
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
        "1.Diabetes": {
            "image": "Images/diabetes.jpg",

            "Description": """
            Diabetes is a condition where the body struggles to process sugar (glucose) from food. 
            Normally, insulin helps move sugar from the blood into cells for energy. In diabetes, 
            either the body doesn't produce enough insulin or can't use it effectively, leading to 
            high blood sugar levels. There are two main types: Type 1 diabetes (where the body doesn't 
            produce insulin) and Type 2 diabetes (where the body doesn't use insulin properly). 
            Over time, high blood sugar can lead to serious problems with our heart, eyes, kidneys, 
            nerves, and more.
            """,
            "Symptoms": [
                "Frequent urination (especially at night)",
                "Increased thirst and hunger",
                "Unexplained weight loss",
                "Fatigue and irritability",
                "Blurred vision",
            ],
            "Causes": [
                "Family history (genetics)",
                "Being overweight or obese",
                "Physical inactivity",
                "Unhealthy eating habits",
                "Age (risk increases as you get older)",
                "High blood pressure"
            ],
            "Prevention": [
                "Maintain a healthy weight through diet and exercise",
                "Eat balanced meals with plenty of fruits and vegetables",
                "Limit sugary foods and drinks",
                "Exercise regularly (at least 30 minutes daily)",
                "Get regular health checkups",
            ],
            "Treatment": [
                "Regular blood sugar monitoring",
                "Insulin therapy (for Type 1 diabetes)",
                "Oral medications (for Type 2 diabetes)",
                "Healthy diet and exercise plan",
                "Regular doctor visits to monitor complications"
            ]
        },
        "2.Heart Disease": {
            "image": "Images/heart.jpg",
            "Description": """
            Heart disease includes various conditions that affect the heart, with coronary artery disease 
            being the most common. It happens when arteries supplying blood to the heart narrow due to 
            plaque buildup (atherosclerosis), reducing oxygen and nutrients. This can cause chest pain, 
            heart attacks, or worse. However, many forms of heart disease can be prevented or managed 
            with healthy lifestyle choices.
            """,
            "Symptoms": [
                "Chest pain, tightness, or discomfort (angina)",
                "Shortness of breath",
                "Pain in neck, jaw, throat, upper abdomen or back",
                "Nausea, fatigue, or lightheadedness",
                "Irregular heartbeat",
                "Swelling in legs, ankles or feet"
            ],
            "Causes": [
                "High blood pressure",
                "High cholesterol levels",
                "Smoking and tobacco use",
                "Diabetes",
                "Unhealthy diet",
                "Excessive alcohol use",
            ],
            "Prevention": [
                "Don't smoke or use tobacco",
                "Exercise for at least 30 minutes most days",
                "Eat a heart-healthy diet (fruits, vegetables, whole grains)",
                "Maintain a healthy weight",
                "Get regular health screenings"
            ],
            "Treatment": [
                "Lifestyle changes (diet, exercise, quitting smoking)",
                "Medications to control blood pressure, cholesterol, etc.",
                "Medical procedures like angioplasty or bypass surgery",
                "Regular monitoring by a cardiologist"
            ]
        },
        "3.Kidney Disease": {
            "image": "Images/kidney.jpg",
            "Description": """
            Kidney disease occurs when your kidneys are damaged and can't filter blood effectively. 
            These bean-shaped organs remove waste, balance minerals, make urine, and regulate blood pressure.
            Chronic kidney disease (CKD) means lasting damage that can get worse over time. If the damage is 
            very bad, your kidneys may stop working completely. This is called kidney failure, and you would 
            need dialysis or a kidney transplant to survive. Many people don't realize they have kidney disease 
            until it's advanced because symptoms often don't appear until the kidneys are badly damaged.
            """,
            "Symptoms": [
                "Fatigue and weakness",
                "Shortness of breath",
                "Blood in urine (may appear pink or cola-colored)",
                "Puffy eyes, especially in the morning",
                "Dry, itchy skin",
            ],
            "Causes": [
                "Diabetes (leading cause of kidney disease)",
                "High blood pressure",
                "Glomerulonephritis (inflammation of kidney filters)",
                "Polycystic kidney disease (inherited condition)",
                "Prolonged urinary tract obstruction",
            ],
            "Prevention": [
                "Manage high blood pressure",
                "Eat a balanced, low-salt diet",
                "Stay hydrated by drinking enough water",
                "Don't smoke or use tobacco products",
                "Get regular exercise"
            ],
            "Treatment": [
                "Medications to control underlying causes",
                "Dietary changes to reduce kidney workload",
                "Treatment for complications like anemia or weak bones",
                "Regular monitoring of kidney function"
            ]
        }
    }
    
    for disease, details in disease_info.items():
        st.markdown(f"<div class='disease-card my-text'><h1 class='disease-title'>{disease}</h1></div>", unsafe_allow_html=True)
        
        # Display disease image
        st.image(details["image"], width=770)
        st.markdown(f"<div><h3>Description:</h3></div>", unsafe_allow_html=True)

        st.write(f"**Description:** {details['Description']}")
        
        st.write("**Symptoms:**")
        st.markdown("\n".join([f"- {symptom}" for symptom in details["Symptoms"]]))
        
        st.write("**Main Causes:**")
        st.markdown("\n".join([f"- {cause}" for cause in details["Causes"]]))
        
        st.write("**Prevention Tips:**")
        st.markdown("\n".join([f"- {prevention}" for prevention in details["Prevention"]]))
        
        st.write("**Treatment Options:**")
        st.markdown("\n".join([f"- {treatment}" for treatment in details["Treatment"]]))
        
        st.write("-----")

    # Footer
    st.markdown("""
    <div class="footer">
        <p>© 2025 HealthScope | Developed with ❤️ by Medical AI Team | Version 2.0.0</p>
        <p style="font-size: 0.8rem; margin-top: 0.5rem;">For research and educational purposes only</p>
    </div>
    """, unsafe_allow_html=True)