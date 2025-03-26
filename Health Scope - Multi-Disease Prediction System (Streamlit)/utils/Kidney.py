import streamlit as st
import pandas as pd
import joblib

def show_kidney_page():
    # Load saved model and scaler
    loaded_model = joblib.load('Models/Kidney/best_model.pkl')
    loaded_scaler = joblib.load('Models/Kidney/scaler.pkl')

    # Streamlit app title with gradient background and color
    st.markdown(
        """
        <style>
            .title-container {
                background: linear-gradient(90deg, rgba(18,141,172,0.1), rgba(50,100,200,0.1), rgba(100,50,200,0.1));
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
            <h1 class="title-text">🧪 Kidney Disease Risk Prediction App 🧪</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Input fields section with color
    st.markdown("<h2 style='color: #128DAC;'>📝 Please Provide Your Health Details for a Personalized Assessment:</h2>", unsafe_allow_html=True)

    # Create a two-column layout (6 rows x 2 columns)
    col1, col2 = st.columns(2)

    with col1:
        blood_pressure = st.slider(
            "🩸 What is your Blood Pressure (mmHg)", 
            min_value=50, max_value=200, value=120,
            help="Normal range: 90-120 mmHg. High BP may indicate kidney issues."
        )
        
        specific_gravity = st.selectbox(
            "🔬 What is your Specific Gravity (Urine Concentration)?", 
            [1.005, 1.010, 1.015, 1.020, 1.025, 1.030], index=3,
            help="Normal range: 1.005 - 1.030. Higher values may indicate dehydration or kidney problems."
        )
        
        albumin = st.slider(
            "💧 What is your Albumin level (Protein in Urine)?", 
            min_value=0, max_value=5, value=2,
            help="Normal: 0-1. High albumin in urine can be a sign of kidney disease."
        )
        
        sugar = st.slider(
            "🍬 What is your Sugar Level (0-5)?", 
            min_value=0, max_value=5, value=1,
            help="Normal: 0. High sugar levels in urine may indicate diabetes or kidney issues."
        )
        
        blood_urea = st.number_input(
            "🧪 Enter your Blood Urea level (mg/dL)?", 
            min_value=0, max_value=300, value=35,
            help="Normal range: 7-25 mg/dL. High levels may indicate kidney dysfunction."
        )
        
        serum_creatinine = st.number_input(
            "🧪 What is your Serum Creatinine level (mg/dL)?", 
            min_value=0.1, max_value=20.0, value=1.2, step=0.1,
            help="Normal: 0.7-1.3 mg/dL (males) & 0.6-1.1 mg/dL (females). High levels indicate kidney issues."
        )

    with col2:
        sodium = st.number_input(
            "🧂 What is your Sodium level (mEq/L)?", 
            min_value=100, max_value=200, value=140,
            help="Normal range: 135-145 mEq/L. Low sodium may indicate kidney problems."
        )
        
        potassium = st.number_input(
            "🍌 What is your Potassium level (mEq/L)?", 
            min_value=1.0, max_value=10.0, value=4.5, step=0.1,
            help="Normal range: 3.5-5.0 mEq/L. High levels may suggest kidney disease."
        )
        
        hemoglobin = st.number_input(
            "🩸 What is your Hemoglobin level (g/dL)?", 
            min_value=5.0, max_value=20.0, value=13.5, step=0.1,
            help="Normal: 12-16 g/dL (females) & 13.5-17.5 g/dL (males). Low levels indicate anemia."
        )
        
        wbc_count = st.number_input(
            "🦠 What is your White Blood Cell Count (cells/cmm)?", 
            min_value=2000, max_value=15000, value=7800,
            help="Normal: 4,000-11,000 cells/cmm. High WBC may indicate infection."
        )
        
        rbc_count = st.number_input(
            "🩸 What is your Red Blood Cell Count (millions/cmm)", 
            min_value=2.0, max_value=7.0, value=5.2, step=0.1,
            help="Normal: 4.7-6.1 million/cmm (males) & 4.2-5.4 million/cmm (females). Low count may indicate kidney disease."
        )
        
        red_blood_cells = st.radio(
            "🔴 Is your Red Blood Cell Condition Normal or Abnormal?", 
            options=[0, 1], index=1,
            format_func=lambda x: "Normal" if x == 0 else "Abnormal",
            help="Abnormal RBC count can indicate kidney issues."
        )
        
    hypertension = st.radio(
        "⚠️ Do you have Hypertension (High Blood Pressure)?", 
        options=[0, 1], index=0,
        format_func=lambda x: "No" if x == 0 else "Yes",
        help="High BP is a major risk factor for kidney disease."
    )

    # Prepare input data
    input_data = pd.DataFrame([{
        'Blood Pressure': blood_pressure,
        'Specific Gravity': specific_gravity,
        'Albumin': albumin,
        'Sugar': sugar,
        'Blood Urea': blood_urea,
        'Serum Creatinine': serum_creatinine,
        'Sodium': sodium,
        'Potassium': potassium,
        'Hemoglobin': hemoglobin,
        'White Blood Cell Count': wbc_count,
        'Red Blood Cell Count': rbc_count,
        'Red Blood Cells': red_blood_cells,
        'Hypertension': hypertension
    }])

    # Define numerical columns
    num_cols = ['Blood Pressure', 'Specific Gravity', 'Albumin', 'Sugar', 
                'Blood Urea', 'Serum Creatinine', 'Sodium', 'Potassium', 
                'Hemoglobin', 'White Blood Cell Count', 'Red Blood Cell Count']
    
    # Scale numerical features
    input_data_scaled = input_data.copy()
    input_data_scaled[num_cols] = loaded_scaler.transform(input_data[num_cols])

    # Predict button
    if st.button("Predict"):
        # Make prediction
        prediction = loaded_model.predict(input_data_scaled)

        # Display the result
        if prediction[0] == 1:
            st.error("⚠️ The patient is at risk of kidney disease.")
            col1, col2, col3 = st.columns([1, 2, 1])  # Centering
            with col2:
                st.image("Images/kidney_risk.jpg", caption="⚠️ Please consult a nephrologist. 🏥", width=350)
        else:
            st.success("✅ The patient is not at risk of kidney disease.")
            col1, col2, col3 = st.columns([1, 2, 1])  # Centering
            with col2:
                st.image("Images/kidney_safe.jpg", caption="✅ Your kidneys are healthy! 😊", width=350)

    # Back button to navigate back to Home
    if st.button("Back to Main Page"):
        st.session_state.current_page = "Home"  # Update session state for navigation