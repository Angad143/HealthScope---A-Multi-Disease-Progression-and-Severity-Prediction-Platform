from fpdf import FPDF
from datetime import datetime

def generate_kidney_report(input_data, prediction):
    # Create PDF instance with better page management
    pdf = FPDF()
    pdf.set_left_margin(20)
    pdf.set_right_margin(20)
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Set font for the entire document
    pdf.set_font("Arial", size=12)
    
    # Add title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(170, 10, txt="Kidney Disease Risk Assessment Report", ln=2, align='C')
    pdf.ln(4)
    
    # Add report date
    pdf.set_font("Arial", 'I', 10)
    pdf.cell(170, 8, txt=f"Report generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=2, align='C')
    pdf.ln(10)
    
    # Prediction result section
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 8, txt="Prediction Result:", ln=2)
    pdf.set_font("Arial", size=12)
    
    if prediction == 1:
        pdf.set_text_color(220, 53, 69)  # Red color for high risk
        pdf.cell(200, 8, txt="High Risk of Kidney Disease (Positive)", ln=2)
    else:
        pdf.set_text_color(40, 167, 69)  # Green color for low risk
        pdf.cell(200, 8, txt="Low Risk of Kidney Disease (Negative)", ln=2)
    
    pdf.set_text_color(0, 0, 0)  # Reset to black
    pdf.ln(8)
    
    # Patient information section
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 8, txt="Patient Information:", ln=2)
    pdf.set_font("Arial", size=12)
    
    # Convert input data to readable format
    readable_data = {
        "Blood Pressure": f"{input_data['Blood Pressure'][0]} mmHg",
        "Specific Gravity": str(input_data['Specific Gravity'][0]),
        "Albumin Level": str(input_data['Albumin'][0]),
        "Sugar Level": str(input_data['Sugar'][0]),
        "Blood Urea": f"{input_data['Blood Urea'][0]} mg/dL",
        "Serum Creatinine": f"{input_data['Serum Creatinine'][0]} mg/dL",
        "Sodium Level": f"{input_data['Sodium'][0]} mEq/L",
        "Potassium Level": f"{input_data['Potassium'][0]} mEq/L",
        "Hemoglobin Level": f"{input_data['Hemoglobin'][0]} g/dL",
        "White Blood Cell Count": f"{input_data['White Blood Cell Count'][0]} cells/cmm",
        "Red Blood Cell Count": f"{input_data['Red Blood Cell Count'][0]} million/cmm",
        "Red Blood Cell Condition": "Normal" if input_data['Red Blood Cells'][0] == 0 else "Abnormal",
        "Hypertension": "Yes" if input_data['Hypertension'][0] == 1 else "No"
    }
    
    # More compact table layout
    col_width = 85
    row_height = 8
    
    for key, value in readable_data.items():
        if pdf.get_y() + row_height > pdf.page_break_trigger:
            pdf.add_page()
        pdf.cell(col_width, row_height, txt=str(key), border=0)
        pdf.cell(col_width, row_height, txt=str(value), border=0, ln=1)
    
    pdf.ln(10)
    
    # Normal ranges section
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 8, txt="Normal Ranges:", ln=2)
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
        if pdf.get_y() + 8 > pdf.page_break_trigger:
            pdf.add_page()
        pdf.cell(200, 8, txt=item, ln=1)
    
    pdf.ln(10)
    
    # Recommendations section
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 8, txt="Recommendations:", ln=2)
    pdf.set_font("Arial", size=12)
    
    recommendations = [
        "1. Consult with a nephrologist immediately",
        "2. Schedule comprehensive kidney function tests",
        "3. Monitor your blood pressure regularly",
        "4. Reduce sodium intake in your diet",
        "5. Stay hydrated with water (unless fluid restricted)",
        "6. Control blood sugar if diabetic",
        "7. Quit smoking if you currently smoke",
        "8. Get regular exercise as tolerated",
        "9. Limit protein intake if recommended by doctor",
        "10. Avoid NSAIDs and other kidney-damaging medications"
    ] if prediction == 1 else [
        "1. Continue with regular health check-ups",
        "2. Maintain a kidney-friendly diet (low sodium, moderate protein)",
        "3. Stay well hydrated (6-8 glasses of water daily)",
        "4. Monitor blood pressure regularly",
        "5. Limit alcohol consumption",
        "6. Avoid unnecessary use of pain medications",
        "7. Maintain healthy blood sugar levels",
        "8. Exercise regularly (30 mins most days)",
        "9. Maintain a healthy weight",
        "10. Get annual kidney function tests if over 60 or at risk"
    ]
    
    for item in recommendations:
        if pdf.get_y() + 8 > pdf.page_break_trigger:
            pdf.add_page()
        pdf.multi_cell(0, 6, txt=item)
        pdf.ln(1)
    
    pdf.ln(8)
    
    # Disclaimer section
    if pdf.get_y() + 20 > pdf.page_break_trigger:
        pdf.add_page()
    pdf.set_font("Arial", 'I', 9)
    pdf.multi_cell(0, 5, txt="Disclaimer: This report is generated by an AI system and is for informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.")
    
    # Return the PDF as bytes
    return pdf.output(dest='S').encode('latin1')
