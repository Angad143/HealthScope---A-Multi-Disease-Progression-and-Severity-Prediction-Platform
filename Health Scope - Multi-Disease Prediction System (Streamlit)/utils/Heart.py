import streamlit as st
import pandas as pd
import joblib

def show_heart_page():
    # Load the model and scaler
    svm_loaded = joblib.load("Models/Heart/best_model.pkl")
    scaler_loaded = joblib.load("Models/Heart/scaler.pkl")

    # Define numerical columns
    numerical_cols = ['Age', 'Resting Blood Pressure', 'Cholesterol', 'Max Heart Rate', 'ST Depression']

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
            <h1 class="title-text">❤️ Heart Disease Risk Prediction App ❤️</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Input fields section with color
    st.markdown("<h2 style='color: #128DAC;'>📝 Please Provide Your Health Information about Heart Disease:</h2>", unsafe_allow_html=True)

    # Create a two-column layout
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("📅 What is your age?", min_value=20, max_value=100, value=50)
        sex = st.radio("⚤ Select your biological sex:", ["Female", "Male"])
        max_hr = st.number_input("🏃‍♂️ What is the maximum heart rate achieved during exercise?", 
                               min_value=60, max_value=220, value=140)
        rest_bp = st.number_input("💓 What is your resting blood pressure? (mm Hg)", 
                                min_value=80, max_value=200, value=120)
        cholesterol = st.number_input("🩸 What is your cholesterol level? (mg/dl)", 
                                    min_value=100, max_value=600, value=200)
        st_depression = st.number_input("📉 How much ST depression was induced by exercise? (mm)", 
                                      min_value=0.0, max_value=5.0, value=1.0, step=0.1)

    with col2:
        fasting_bs = st.radio("🍚 Is your fasting blood sugar greater than 120 mg/dl?", ["No", "Yes"])
        exercise_angina = st.radio("🚶‍♂️ Do you experience chest pain (angina) during exercise?", ["No", "Yes"])
        major_vessels = st.slider("🫀 How many major blood vessels are visible in your angiogram? (0-3)", 0, 3, 1)
        
        # Chest Pain Type
        chest_pain = st.selectbox("❤️ What type of chest pain do you experience?", 
                                ["Typical Angina", "Atypical Angina", 
                                 "Non-anginal Pain", "Asymptomatic"])
        
        # Resting ECG
        rest_ecg = st.selectbox("📊 Resting ECG results:", 
                              ["Normal", "ST-T wave abnormality", 
                               "Left ventricular hypertrophy"])
        
        # Slope of ST Segment
        slope = st.selectbox("📈 What is the slope of your ST segment?", 
                           ["Upsloping", "Flat", "Downsloping"])
        
    # Thalassemia
    thal = st.selectbox("🧬 What type of thalassemia do you have?", 
                          ["Normal", "Fixed Defect", "Reversible Defect"])

    # Convert categorical inputs to numerical values
    sex = 1 if sex == "Male" else 0
    fasting_bs = 1 if fasting_bs == "Yes" else 0
    exercise_angina = 1 if exercise_angina == "Yes" else 0

    # Encoding categorical features manually
    chest_pain_mapping = {"Typical Angina": 0, "Atypical Angina": 1, 
                         "Non-anginal Pain": 2, "Asymptomatic": 3}
    rest_ecg_mapping = {"Normal": 0, "ST-T wave abnormality": 1, 
                       "Left ventricular hypertrophy": 2}
    slope_mapping = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
    thal_mapping = {"Normal": 0, "Fixed Defect": 1, "Reversible Defect": 2}

    # Convert categorical variables to numerical values
    chest_pain = chest_pain_mapping[chest_pain]
    rest_ecg = rest_ecg_mapping[rest_ecg]
    slope = slope_mapping[slope]
    thal = thal_mapping[thal]

    # Create DataFrame for prediction
    input_data = pd.DataFrame([{
        'Age': age,
        'Sex': sex,
        'Chest Pain Type': chest_pain,
        'Resting Blood Pressure': rest_bp,
        'Cholesterol': cholesterol,
        'Fasting Blood Sugar': fasting_bs,
        'Resting ECG': rest_ecg,
        'Max Heart Rate': max_hr,
        'Exercise Induced Angina': exercise_angina,
        'ST Depression': st_depression,
        'Slope of ST Segment': slope,
        'Number of Major Vessels': major_vessels,
        'Thalassemia': thal
    }])

    # Apply scaling only to numerical columns
    input_data_scaled = input_data.copy()
    input_data_scaled[numerical_cols] = scaler_loaded.transform(input_data[numerical_cols])

    # Predict button
    if st.button("Predict"):
        # Make prediction
        prediction = svm_loaded.predict(input_data_scaled)

        # Display the result
        if prediction[0] == 1:
            st.error("⚠️ The patient is at risk of heart disease.")
            col1, col2, col3 = st.columns([1, 2, 1])  # Centering
            with col2:
                st.image("Images/heart_risk.jpg", caption="⚠️ Please consult a cardiologist. 🏥", width=350)
        else:
            st.success("✅ The patient is not at risk of heart disease.")
            col1, col2, col3 = st.columns([1, 2, 1])  # Centering
            with col2:
                st.image("Images/heart_safe.jpg", caption="✅ Keep your heart healthy! 😊", width=350)

    # Back button to navigate back to Home
    if st.button("Back to Main Page"):
        st.session_state.current_page = "Home"  # Update session state for navigation