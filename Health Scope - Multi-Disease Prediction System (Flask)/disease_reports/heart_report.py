from fpdf import FPDF
from datetime import datetime

def generate_heart_report(input_data, prediction):
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
    pdf.cell(170, 10, txt="Heart Disease Risk Assessment Report", ln=2, align='C')
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
        pdf.cell(200, 8, txt="High Risk of Heart Disease (Positive)", ln=2)
    else:
        pdf.set_text_color(40, 167, 69)  # Green color for low risk
        pdf.cell(200, 8, txt="Low Risk of Heart Disease (Negative)", ln=2)
    
    pdf.set_text_color(0, 0, 0)  # Reset to black
    pdf.ln(8)
    
    # Patient information section
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 8, txt="Patient Information:", ln=2)
    pdf.set_font("Arial", size=12)
    
    # Convert input data to readable format
    readable_data = {
        "Age": str(input_data['Age'][0]),
        "Gender": "Male" if input_data['Sex'][0] == 1 else "Female",
        "Chest Pain Type": {
            0: "Typical Angina",
            1: "Atypical Angina",
            2: "Non-anginal Pain",
            3: "Asymptomatic"
        }.get(input_data['Chest Pain Type'][0], "Unknown"),
        "Resting Blood Pressure": f"{input_data['Resting Blood Pressure'][0]} mm Hg",
        "Cholesterol": f"{input_data['Cholesterol'][0]} mg/dl",
        "Fasting Blood Sugar > 120 mg/dl": "Yes" if input_data['Fasting Blood Sugar'][0] == 1 else "No",
        "Resting ECG": {
            0: "Normal",
            1: "ST-T wave abnormality",
            2: "Left ventricular hypertrophy"
        }.get(input_data['Resting ECG'][0], "Unknown"),
        "Max Heart Rate": str(input_data['Max Heart Rate'][0]),
        "Exercise Induced Angina": "Yes" if input_data['Exercise Induced Angina'][0] == 1 else "No",
        "ST Depression": str(input_data['ST Depression'][0]),
        "Slope of ST Segment": {
            0: "Upsloping",
            1: "Flat",
            2: "Downsloping"
        }.get(input_data['Slope of ST Segment'][0], "Unknown"),
        "Number of Major Vessels": str(input_data['Number of Major Vessels'][0]),
        "Thalassemia": {
            0: "Normal",
            1: "Fixed Defect",
            2: "Reversible Defect"
        }.get(input_data['Thalassemia'][0], "Unknown")
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
    
    # Recommendations section
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 8, txt="Recommendations:", ln=2)
    pdf.set_font("Arial", size=12)
    
    recommendations = [
        "1. Consult with a cardiologist immediately",
        "2. Schedule a comprehensive cardiac evaluation",
        "3. Monitor your blood pressure regularly",
        "4. Engage in regular, moderate exercise as advised by your doctor",
        "5. Quit smoking if you currently smoke",
        "6. Maintain a healthy weight",
        "7. Limit alcohol consumption",
        "8. Follow a heart-healthy diet (Mediterranean diet recommended)",
        "9. Manage stress through relaxation techniques",
        "10. Get regular check-ups for cholesterol and blood sugar levels"
    ] if prediction == 1 else [
        "1. Continue with regular health check-ups",
        "2. Maintain a heart-healthy diet (Mediterranean diet recommended)",
        "3. Engage in regular physical activity (150 mins/week moderate exercise)",
        "4. Monitor your blood pressure and cholesterol levels annually",
        "5. Maintain a healthy weight (BMI 18.5-24.9)",
        "6. Manage stress through healthy coping mechanisms",
        "7. Limit alcohol consumption to moderate levels",
        "8. Avoid smoking and secondhand smoke",
        "9. Get 7-9 hours of quality sleep each night",
        "10. Be aware of heart disease symptoms for early detection"
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
