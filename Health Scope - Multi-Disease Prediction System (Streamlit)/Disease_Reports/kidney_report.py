# pdf for kidney disease reprt
from fpdf import FPDF

# Functions of generating pdf report for kidney disease
def generate_kidney_report(input_data, prediction):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Kidney Disease Risk Assessment Report", ln=1, align='C')
    pdf.ln(10)
    
    # Prediction result
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Prediction Result:", ln=1)
    pdf.set_font("Arial", size=12)
    
    if prediction == 1:
        pdf.cell(200, 10, txt="High Risk of Kidney Disease (Positive)", ln=1)
    else:
        pdf.cell(200, 10, txt="Low Risk of Kidney Disease (Negative)", ln=1)
    pdf.ln(5)
    
    # Patient information
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Patient Information:", ln=1)
    pdf.set_font("Arial", size=12)
    
    # Convert input data to readable format
    readable_data = {
        "Blood Pressure (mmHg)": input_data['Blood Pressure'][0],
        "Specific Gravity (Urine Concentration)": input_data['Specific Gravity'][0],
        "Albumin Level (Protein in Urine)": input_data['Albumin'][0],
        "Sugar Level": input_data['Sugar'][0],
        "Blood Urea (mg/dL)": input_data['Blood Urea'][0],
        "Serum Creatinine (mg/dL)": input_data['Serum Creatinine'][0],
        "Sodium Level (mEq/L)": input_data['Sodium'][0],
        "Potassium Level (mEq/L)": input_data['Potassium'][0],
        "Hemoglobin Level (g/dL)": input_data['Hemoglobin'][0],
        "White Blood Cell Count (cells/cmm)": input_data['White Blood Cell Count'][0],
        "Red Blood Cell Count (millions/cmm)": input_data['Red Blood Cell Count'][0],
        "Red Blood Cell Condition": "Normal" if input_data['Red Blood Cells'][0] == 0 else "Abnormal",
        "Hypertension": "Yes" if input_data['Hypertension'][0] == 1 else "No"
    }
    
    for key, value in readable_data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=1)
    
    pdf.ln(10)
    
    # Normal ranges
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Normal Ranges:", ln=1)
    pdf.set_font("Arial", size=12)
    
    normal_ranges = [
        "Blood Pressure: 90-120 mmHg",
        "Specific Gravity: 1.005-1.030",
        "Albumin: 0-1",
        "Sugar: 0",
        "Blood Urea: 7-25 mg/dL",
        "Serum Creatinine: 0.6-1.3 mg/dL",
        "Sodium: 135-145 mEq/L",
        "Potassium: 3.5-5.0 mEq/L",
        "Hemoglobin: 12-17.5 g/dL",
        "WBC Count: 4,000-11,000 cells/cmm",
        "RBC Count: 4.2-6.1 million/cmm"
    ]
    
    for item in normal_ranges:
        pdf.cell(200, 10, txt=item, ln=1)
    
    pdf.ln(10)
    
    # Recommendations
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Recommendations:", ln=1)
    pdf.set_font("Arial", size=12)
    
    if prediction == 1:
        recommendations = [
            "1. Consult with a nephrologist immediately",
            "2. Schedule comprehensive kidney function tests",
            "3. Monitor your blood pressure regularly",
            "4. Reduce sodium intake in your diet",
            "5. Stay hydrated with water (unless fluid restricted)",
            "6. Control blood sugar if diabetic",
            "7. Quit smoking if you currently smoke",
            "8. Get regular exercise as tolerated"
        ]
    else:
        recommendations = [
            "1. Continue with regular health check-ups",
            "2. Maintain a kidney-friendly diet (low sodium, moderate protein)",
            "3. Stay well hydrated (6-8 glasses of water daily)",
            "4. Monitor blood pressure regularly",
            "5. Limit alcohol consumption",
            "6. Avoid unnecessary use of pain medications",
            "7. Maintain healthy blood sugar levels",
            "8. Exercise regularly (30 mins most days)",
            "9. Maintain a healthy weight"
        ]
    
    for item in recommendations:
        pdf.cell(200, 10, txt=item, ln=1)
    
    return pdf.output(dest='S').encode('latin1')