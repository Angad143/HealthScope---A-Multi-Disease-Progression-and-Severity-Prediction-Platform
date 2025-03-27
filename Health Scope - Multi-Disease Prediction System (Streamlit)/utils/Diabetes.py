import streamlit as st
import pandas as pd
import joblib
from Disease_Reports.diabetes_report import generate_diabetes_report

def show_diabetes_page():
    # Load the model, top 10 features, and scaler
    rf_model = joblib.load('Models/Diabetes/best_model.pkl')
    features = joblib.load('Models/Diabetes/features.pkl')
    scaler = joblib.load('Models/Diabetes/scaler.pkl')

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
            <h1 class="title-text">🩸 Diabetes Risk Prediction App 🩸</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Input fields section with color
    st.markdown("<h2 style='color: #128DAC;'>📝 Please Provide Your Health Information about Diabetes:</h2>", unsafe_allow_html=True)

    # Create a two-column layout (5 rows x 2 columns)
    col1, col2 = st.columns(2)

    with col1:
        polyuria = st.selectbox("Do you experience excessive urination (Polyuria)?", ["No", "Yes"])
        polydipsia = st.selectbox("Do you feel excessively thirsty (Polydipsia)?", ["No", "Yes"])
        gender = st.selectbox("What is your gender?", ["Female", "Male"])
        age = st.number_input("What is your age?", min_value=10, max_value=100, value=30)
        sudden_weight_loss = st.selectbox("Have you experienced sudden weight loss?", ["No", "Yes"])

    with col2:
        partial_paresis = st.selectbox("Do you have muscle weakness (Partial Paresis)?", ["No", "Yes"])
        alopecia = st.selectbox("Have you noticed hair loss (Alopecia)?", ["No", "Yes"])
        irritability = st.selectbox("Do you experience frequent mood swings (Irritability)?", ["No", "Yes"])
        delayed_healing = st.selectbox("Do your wounds heal slowly (Delayed Healing)?", ["No", "Yes"])
        itching = st.selectbox("Do you experience skin itching (Itching)?", ["No", "Yes"])

    # Map "Yes" to 1 and "No" to 0
    input_data = {
        'Polyuria': 1 if polyuria == "Yes" else 0,
        'Polydipsia': 1 if polydipsia == "Yes" else 0,
        'Gender': 1 if gender == "Male" else 0,
        'Age': age,  # Will be standardized later
        'Sudden Weight Loss': 1 if sudden_weight_loss == "Yes" else 0,
        'Partial Paresis': 1 if partial_paresis == "Yes" else 0,
        'Alopecia': 1 if alopecia == "Yes" else 0,
        'Irritability': 1 if irritability == "Yes" else 0,
        'Delayed Healing': 1 if delayed_healing == "Yes" else 0,
        'Itching': 1 if itching == "Yes" else 0,
    }

    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])

    # Standardize the 'Age' feature
    input_df['Age'] = scaler.transform(input_df[['Age']])

    # Ensure the input data has the same column order as the top 10 features
    input_df = input_df[features]

    # Predict button
    if st.button("Predict"):
        # Make prediction
        prediction = rf_model.predict(input_df)

        # Display the result
        if prediction[0] == 1:
            st.error("⚠️ The patient is at risk of diabetes.")
            col1, col2, col3 = st.columns([1, 2, 1])  # Centering
            with col2:
                st.image("Images/diabetes_risk.jpg", caption="⚠️ Please consult a doctor. 🏥", width=350)

        else:
            st.success("✅ The patient is not at risk of diabetes.")
            col1, col2, col3 = st.columns([1, 2, 1])  # Centering
            with col2:
                st.image("Images/diabetes_save.jpg", caption="✅ Stay Healthy! 😊", width=350)


        # Generate and show download button for PDF report in both cases
        pdf_report = generate_diabetes_report(input_data, prediction[0], age)
        st.download_button(
            label="📄 Download Detailed Report (PDF)",
            data=pdf_report,
            file_name="diabetes_risk_report.pdf",
            mime="application/pdf",
        )

    # Back button to navigate back to Home
    if st.button("Back to Main Page"):
        st.session_state.current_page = "Home"  # Update session state for navigation
