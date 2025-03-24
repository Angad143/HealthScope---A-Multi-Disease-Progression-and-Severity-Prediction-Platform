import streamlit as st
import pandas as pd
import joblib

# Load saved model and scaler
loaded_model = joblib.load('Models/best_model.pkl')
loaded_scaler = joblib.load('Models/scaler.pkl')

# Streamlit UI
st.title("🩺 Kidney Disease Prediction")
st.write("Enter the patient's details below to check the likelihood of kidney disease.")

# Sidebar for input fields
st.sidebar.header("📌 Patient's Medical Details")

# Blood Pressure
blood_pressure = st.sidebar.slider(
    "🩸 Blood Pressure (mmHg)", 
    min_value=50, max_value=200, value=120,
    help="Normal range: **90-120 mmHg**. High BP may indicate kidney issues."
)

# Specific Gravity
specific_gravity = st.sidebar.selectbox(
    "🔬 Specific Gravity (Urine Concentration)", 
    [1.005, 1.010, 1.015, 1.020, 1.025, 1.030], index=3,
    help="Normal range: **1.005 - 1.030**. Higher values may indicate dehydration or kidney problems."
)

# Albumin
albumin = st.sidebar.slider(
    "💧 Albumin (Protein in Urine)", 
    min_value=0, max_value=5, value=2,
    help="Normal: **0-1**. High albumin in urine can be a sign of kidney disease."
)

# Sugar
sugar = st.sidebar.slider(
    "🍬 Sugar Level (0-5)", 
    min_value=0, max_value=5, value=1,
    help="Normal: **0**. High sugar levels in urine may indicate diabetes or kidney issues."
)

# Blood Urea
blood_urea = st.sidebar.number_input(
    "🧪 Blood Urea (mg/dL)", 
    min_value=0, max_value=300, value=35,
    help="Normal range: **7-25 mg/dL**. High levels may indicate kidney dysfunction."
)

# Serum Creatinine
serum_creatinine = st.sidebar.number_input(
    "🧪 Serum Creatinine (mg/dL)", 
    min_value=0.1, max_value=20.0, value=1.2, step=0.1,
    help="Normal: **0.7-1.3 mg/dL** (males) & **0.6-1.1 mg/dL** (females). High levels indicate kidney issues."
)

# Sodium
sodium = st.sidebar.number_input(
    "🧂 Sodium (mEq/L)", 
    min_value=100, max_value=200, value=140,
    help="Normal range: **135-145 mEq/L**. Low sodium may indicate kidney problems."
)

# Potassium
potassium = st.sidebar.number_input(
    "🍌 Potassium (mEq/L)", 
    min_value=1.0, max_value=10.0, value=4.5, step=0.1,
    help="Normal range: **3.5-5.0 mEq/L**. High levels may suggest kidney disease."
)

# Hemoglobin
hemoglobin = st.sidebar.number_input(
    "🩸 Hemoglobin (g/dL)", 
    min_value=5.0, max_value=20.0, value=13.5, step=0.1,
    help="Normal: **12-16 g/dL** (females) & **13.5-17.5 g/dL** (males). Low levels indicate anemia."
)

# White Blood Cell Count
wbc_count = st.sidebar.number_input(
    "🦠 White Blood Cell Count (cells/cmm)", 
    min_value=2000, max_value=15000, value=7800,
    help="Normal: **4,000-11,000 cells/cmm**. High WBC may indicate infection."
)

# Red Blood Cell Count
rbc_count = st.sidebar.number_input(
    "🩸 Red Blood Cell Count (millions/cmm)", 
    min_value=2.0, max_value=7.0, value=5.2, step=0.1,
    help="Normal: **4.7-6.1 million/cmm** (males) & **4.2-5.4 million/cmm** (females). Low count may indicate kidney disease."
)

# Red Blood Cells (Categorical)
red_blood_cells = st.sidebar.radio(
    "🔴 Red Blood Cells Condition", 
    options=[0, 1], index=1,
    format_func=lambda x: "Normal" if x == 0 else "Abnormal",
    help="Abnormal RBC count can indicate kidney issues."
)

# Hypertension (Categorical)
hypertension = st.sidebar.radio(
    "⚠️ Hypertension (High Blood Pressure)", 
    options=[0, 1], index=0,
    format_func=lambda x: "No" if x == 0 else "Yes",
    help="High BP is a major risk factor for kidney disease."
)

# Button to make predictions
if st.sidebar.button("Predict"):
    # Prepare input data
    new_data = pd.DataFrame([{
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
    new_data_scaled = new_data.copy()
    new_data_scaled[num_cols] = loaded_scaler.transform(new_data[num_cols])

    # Predict using the trained model
    prediction = loaded_model.predict(new_data_scaled)

    # Display prediction result
    st.subheader("Prediction Result:")
    if prediction[0] == 1:
        st.error("🚨 The person is **likely** to have kidney disease.")
    else:
        st.success("✅ The person is **unlikely** to have kidney disease.")
