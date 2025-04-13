import pandas as pd
import joblib
import numpy as np
from disease_reports.diabetes_report import generate_diabetes_report

class DiabetesPredictor:
    def __init__(self):
        # Load the model, features, and scaler
        self.model = joblib.load('Models/Diabetes/best_model.pkl')
        self.features = joblib.load('Models/Diabetes/features.pkl')
        self.scaler = joblib.load('Models/Diabetes/scaler.pkl')
    
    def predict(self, form_data):
        # Process form data
        input_data = {
            'Polyuria': 1 if form_data.get('polyuria') == "Yes" else 0,
            'Polydipsia': 1 if form_data.get('polydipsia') == "Yes" else 0,
            'Gender': 1 if form_data.get('gender') == "Male" else 0,
            'Age': int(form_data.get('age', 30)),
            'Sudden Weight Loss': 1 if form_data.get('sudden_weight_loss') == "Yes" else 0,
            'Partial Paresis': 1 if form_data.get('partial_paresis') == "Yes" else 0,
            'Alopecia': 1 if form_data.get('alopecia') == "Yes" else 0,
            'Irritability': 1 if form_data.get('irritability') == "Yes" else 0,
            'Delayed Healing': 1 if form_data.get('delayed_healing') == "Yes" else 0,
            'Itching': 1 if form_data.get('itching') == "Yes" else 0,
        }
        
        # Convert to DataFrame and scale age
        input_df = pd.DataFrame([input_data])
        input_df['Age'] = self.scaler.transform(input_df[['Age']])
        input_df = input_df[self.features]
        
        # Make prediction and convert to native Python type
        prediction = int(self.model.predict(input_df)[0])
        
        # Generate report
        pdf_report = generate_diabetes_report(input_data, prediction, int(form_data.get('age', 30)))
        
        return prediction, pdf_report