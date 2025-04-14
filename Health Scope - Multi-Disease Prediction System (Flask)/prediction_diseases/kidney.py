import pandas as pd
import joblib
import numpy as np
from disease_reports.kidney_report import generate_kidney_report

class KidneyDiseasePredictor:
    def __init__(self):
        # Load the model, features, and scaler
        self.model = joblib.load('models/kidney/best_model.pkl')
        self.scaler = joblib.load('models/kidney/scaler.pkl')
        self.numerical_cols = [
            'Blood Pressure', 'Specific Gravity', 'Albumin', 'Sugar',
            'Blood Urea', 'Serum Creatinine', 'Sodium', 'Potassium',
            'Hemoglobin', 'White Blood Cell Count', 'Red Blood Cell Count'
        ]
    
    def predict(self, form_data):
        # Process form data
        input_data = {
            'Blood Pressure': int(form_data.get('blood_pressure', 120)),
            'Specific Gravity': float(form_data.get('specific_gravity', 1.015)),
            'Albumin': int(form_data.get('albumin', 0)),
            'Sugar': int(form_data.get('sugar', 0)),
            'Blood Urea': int(form_data.get('blood_urea', 35)),
            'Serum Creatinine': float(form_data.get('serum_creatinine', 1.2)),
            'Sodium': int(form_data.get('sodium', 140)),
            'Potassium': float(form_data.get('potassium', 4.5)),
            'Hemoglobin': float(form_data.get('hemoglobin', 13.5)),
            'White Blood Cell Count': int(form_data.get('wbc_count', 7800)),
            'Red Blood Cell Count': float(form_data.get('rbc_count', 5.2)),
            'Red Blood Cells': 1 if form_data.get('red_blood_cells') == "Abnormal" else 0,
            'Hypertension': 1 if form_data.get('hypertension') == "Yes" else 0
        }
        
        # Convert to DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Scale numerical columns
        input_df_scaled = input_df.copy()
        input_df_scaled[self.numerical_cols] = self.scaler.transform(input_df[self.numerical_cols])
        
        # Make prediction
        prediction = int(self.model.predict(input_df_scaled)[0])
        
        # Generate report
        pdf_report = generate_kidney_report(input_df, prediction)
        
        return prediction, pdf_report