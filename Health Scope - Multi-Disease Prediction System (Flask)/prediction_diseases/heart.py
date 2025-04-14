import pandas as pd
import joblib
import numpy as np
from disease_reports.heart_report import generate_heart_report

class HeartDiseasePredictor:
    def __init__(self):
        # Load the model, features, and scaler
        self.model = joblib.load('models/heart/best_model.pkl')
        self.scaler = joblib.load('models/heart/scaler.pkl')
        self.numerical_cols = ['Age', 'Resting Blood Pressure', 'Cholesterol', 'Max Heart Rate', 'ST Depression']
    
    def predict(self, form_data):
        # Process form data
        input_data = {
            'Age': int(form_data.get('age', 50)),
            'Sex': 1 if form_data.get('gender') == "Male" else 0,
            'Chest Pain Type': int(form_data.get('chest_pain', 0)),
            'Resting Blood Pressure': int(form_data.get('resting_bp', 120)),
            'Cholesterol': int(form_data.get('cholesterol', 200)),
            'Fasting Blood Sugar': 1 if form_data.get('fasting_bs') == "Yes" else 0,
            'Resting ECG': int(form_data.get('resting_ecg', 0)),
            'Max Heart Rate': int(form_data.get('max_hr', 140)),
            'Exercise Induced Angina': 1 if form_data.get('exercise_angina') == "Yes" else 0,
            'ST Depression': float(form_data.get('st_depression', 1.0)),
            'Slope of ST Segment': int(form_data.get('slope', 0)),
            'Number of Major Vessels': int(form_data.get('major_vessels', 0)),
            'Thalassemia': int(form_data.get('thal', 0))
        }
        
        # Convert to DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Scale numerical columns
        input_df_scaled = input_df.copy()
        input_df_scaled[self.numerical_cols] = self.scaler.transform(input_df[self.numerical_cols])
        
        # Make prediction
        prediction = int(self.model.predict(input_df_scaled)[0])
        
        # Generate report
        pdf_report = generate_heart_report(input_df, prediction)
        
        return prediction, pdf_report