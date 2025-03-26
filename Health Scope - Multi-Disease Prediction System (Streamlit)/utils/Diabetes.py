import streamlit as st
import pandas as pd
import joblib

def show_diabetes_page():
        # Load the model, top 10 features, and scaler
        rf_model = joblib.load('Models/Diabetes/best_model.pkl')
        features = joblib.load('Models/Diabetes/features.pkl')
        scaler = joblib.load('Models/Diabetes/scaler.pkl')

        # Streamlit app
        st.title("Diabetes Risk Prediction App")

        # Input fields for the top 10 features
        st.header("Enter Patient Details")

        # Create input fields for each feature
        polyuria = st.selectbox("Do you experience excessive urination (Polyuria)?", ["No", "Yes"])
        polydipsia = st.selectbox("Do you feel excessively thirsty (Polydipsia)?", ["No", "Yes"])
        gender = st.selectbox("What is your gender?", ["Female", "Male"])
        age = st.number_input("What is your age?", min_value=10, max_value=100, value=30)
        sudden_weight_loss = st.selectbox("Have you experienced sudden weight loss?", ["No", "Yes"])
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
            'Age': age,  # Age will be standardized later
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
                st.error("The patient is at risk of diabetes.")
            else:
                st.success("The patient is not at risk of diabetes.")

        # Back button
        if st.button("Back to Main Page"):
            st.switch_page("app.py")