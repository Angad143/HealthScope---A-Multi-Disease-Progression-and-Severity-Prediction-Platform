# pdf for heart report
from fpdf import FPDF

# Function to generate heart disease report in PDF format
def generate_heart_report(input_data, prediction):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Heart Disease Risk Assessment Report", ln=1, align='C')
    pdf.ln(10)
    
    # Prediction result
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Prediction Result:", ln=1) # A width of 200 and a height of 10.
    pdf.set_font("Arial", size=12)
    
    if prediction == 1:
        pdf.cell(200, 10, txt="High Risk of Heart Disease (Positive)", ln=1)
    else:
        pdf.cell(200, 10, txt="Low Risk of Heart Disease (Negative)", ln=1)
    pdf.ln(5)
    
    # Patient information
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Patient Information:", ln=1)
    pdf.set_font("Arial", size=12)
    
    # Convert input data to readable format
    readable_data = {
        "Age": input_data['Age'][0],
        "Gender": "Male" if input_data['Sex'][0] == 1 else "Female",
        "Chest Pain Type": {
            0: "Typical Angina",
            1: "Atypical Angina",
            2: "Non-anginal Pain",
            3: "Asymptomatic"
        }[input_data['Chest Pain Type'][0]],
        "Resting Blood Pressure (mm Hg)": input_data['Resting Blood Pressure'][0],
        "Cholesterol (mg/dl)": input_data['Cholesterol'][0],
        "Fasting Blood Sugar > 120 mg/dl": "Yes" if input_data['Fasting Blood Sugar'][0] == 1 else "No",
        "Resting ECG": {
            0: "Normal",
            1: "ST-T wave abnormality",
            2: "Left ventricular hypertrophy"
        }[input_data['Resting ECG'][0]],
        "Max Heart Rate": input_data['Max Heart Rate'][0],
        "Exercise Induced Angina": "Yes" if input_data['Exercise Induced Angina'][0] == 1 else "No",
        "ST Depression": input_data['ST Depression'][0],
        "Slope of ST Segment": {
            0: "Upsloping",
            1: "Flat",
            2: "Downsloping"
        }[input_data['Slope of ST Segment'][0]],
        "Number of Major Vessels": input_data['Number of Major Vessels'][0],
        "Thalassemia": {
            0: "Normal",
            1: "Fixed Defect",
            2: "Reversible Defect"
        }[input_data['Thalassemia'][0]]
    }
    
    for key, value in readable_data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=1)
    
    pdf.ln(10)
    
    # Recommendations
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Recommendations:", ln=1)
    pdf.set_font("Arial", size=12)
    
    if prediction == 1:
        recommendations = [
            "1. Consult with a cardiologist immediately",
            "2. Schedule a comprehensive cardiac evaluation",
            "3. Monitor your blood pressure regularly",
            "4. Engage in regular, moderate exercise as advised by your doctor",
            "5. Quit smoking if you currently smoke",
            "6. Maintain a healthy weight",
            "7. Limit alcohol consumption",
        ]
    else:
        recommendations = [
            "1. Continue with regular health check-ups",
            "2. Maintain a heart-healthy diet (Mediterranean diet recommended)",
            "3. Engage in regular physical activity (150 mins/week moderate exercise)",
            "4. Monitor your blood pressure and cholesterol levels annually",
            "5. Maintain a healthy weight (BMI 18.5-24.9)",
            "6. Manage stress through healthy coping mechanisms",
            "7. Limit alcohol consumption to moderate levels",
            "8. Avoid smoking and secondhand smoke",
            "9. Get 7-9 hours of quality sleep each night",
        ]
    
    for item in recommendations:
        pdf.cell(200, 10, txt=item, ln=1)
    
    return pdf.output(dest='S').encode('latin1')