import streamlit as st
import pandas as pd
import joblib

# Load the trained SVM model and scaler
svm_loaded = joblib.load("Models/best_model.pkl")
scaler_loaded = joblib.load("Models/scaler.pkl")

# Define numerical columns
numerical_cols = ['Age', 'Resting Blood Pressure', 'Cholesterol', 'Max Heart Rate', 'ST Depression']

# Streamlit UI
st.title("💓 Heart Disease Prediction App")

# User Inputs
age = st.number_input("📅 What is your age?", min_value=20, max_value=100, value=50)
sex = st.radio("⚤ Select your biological sex:", ["Male", "Female"])

max_hr = st.number_input("🏃‍♂️ What is the maximum heart rate achieved during exercise?", 
                         min_value=60, max_value=220, value=140)

exercise_angina = st.radio("🚶‍♂️ Do you experience chest pain (angina) during exercise?", ["No", "Yes"])

st_depression = st.number_input("📉 How much ST depression was induced by exercise? (mm)", 
                                min_value=0.0, max_value=5.0, value=1.0, step=0.1)

rest_bp = st.number_input("💓 What is your resting blood pressure? (mm Hg)", 
                          min_value=80, max_value=200, value=120)

cholesterol = st.number_input("🩸 What is your cholesterol level? (mg/dl)", 
                              min_value=100, max_value=600, value=200)

fasting_bs = st.radio("🍚 Is your fasting blood sugar greater than 120 mg/dl?", ["No", "Yes"])

# Chest Pain Mapping
chest_pain_options = {
    "Typical Angina (Chest pain during exertion)": "Typical Angina",
    "Atypical Angina (Chest pain not related to exertion)": "Atypical Angina",
    "Non-anginal Pain (Chest discomfort, not heart-related)": "Non-anginal Pain",
    "Asymptomatic (No chest pain)": "Asymptomatic"
}

# Resting ECG Mapping
rest_ecg_options = {
    "Normal (No abnormality detected)": "Normal",
    "ST-T wave abnormality (Indicates heart muscle damage)": "ST-T wave abnormality",
    "Left ventricular hypertrophy (Thickened heart muscle)": "Left ventricular hypertrophy"
}

# Slope Mapping
slope_options = {
    "Upsloping (Better heart health)": "Upsloping",
    "Flat (Moderate risk)": "Flat",
    "Downsloping (Higher risk of heart disease)": "Downsloping"
}

major_vessels = st.slider("🫀 How many major blood vessels are visible in your angiogram? (0-3)", 0, 3, 1)

# Thalassemia Mapping
thal_options = {
    "Normal (No issue)": "Normal",
    "Fixed Defect (Past heart damage)": "Fixed Defect",
    "Reversible Defect (Possible current heart issue)": "Reversible Defect"
}

slope = st.selectbox("📈 What is the slope of your ST segment?", list(slope_options.keys()))
slope = slope_options[slope]

thal = st.selectbox("🧬 What type of thalassemia do you have?", list(thal_options.keys()))
thal = thal_options[thal]

chest_pain = st.selectbox("❤️ What type of chest pain do you experience?", list(chest_pain_options.keys()))
chest_pain = chest_pain_options[chest_pain] 

rest_ecg = st.selectbox("📊 Resting ECG Results:", list(rest_ecg_options.keys()))
rest_ecg = rest_ecg_options[rest_ecg]

# Convert categorical inputs to numerical values
sex = 1 if sex == "Male" else 0
fasting_bs = 1 if fasting_bs == "Yes" else 0
exercise_angina = 1 if exercise_angina == "Yes" else 0

# Encoding categorical features manually
chest_pain_mapping = {"Typical Angina": 0, "Atypical Angina": 1, "Non-anginal Pain": 2, "Asymptomatic": 3}
rest_ecg_mapping = {"Normal": 0, "ST-T wave abnormality": 1, "Left ventricular hypertrophy": 2}
slope_mapping = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
thal_mapping = {"Normal": 0, "Fixed Defect": 1, "Reversible Defect": 2}

# Convert categorical variables to numerical values
chest_pain = chest_pain_mapping[chest_pain]
rest_ecg = rest_ecg_mapping[rest_ecg]
slope = slope_mapping[slope]
thal = thal_mapping[thal]

# Create DataFrame for prediction
new_data = pd.DataFrame([{
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
new_data_scaled = new_data.copy()
new_data_scaled[numerical_cols] = scaler_loaded.transform(new_data[numerical_cols])

# Prediction Button
if st.button("🔍 Predict"):
    prediction = svm_loaded.predict(new_data_scaled)

    # Display Result
    if prediction[0] == 1:
        st.error("🚨 The person is **likely** to have heart disease.")
    else:
        st.success("✅ The person is **unlikely** to have heart disease.")
