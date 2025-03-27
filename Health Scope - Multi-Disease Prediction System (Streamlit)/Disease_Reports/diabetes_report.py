# pdf for diabetes_report
from fpdf import FPDF

# Function to generate diabetes report in PDF format
def generate_diabetes_report(input_data, prediction, age):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Title 
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Diabetes Risk Assessment Report", ln=1, align='C')
    pdf.ln(10)
    
    # Prediction result
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Prediction Result:", ln=1)
    pdf.set_font("Arial", size=12)
    
    if prediction == 1:
        pdf.cell(200, 10, txt="High Risk of Diabetes (Positive)", ln=1)
    else:
        pdf.cell(200, 10, txt="Low Risk of Diabetes (Negative)", ln=1)
    pdf.ln(5)
    
    # Patient information
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Patient Information:", ln=1)
    pdf.set_font("Arial", size=12)
    
    # Convert input data to readable format
    readable_data = {
        "Gender": "Male" if input_data['Gender'] == 1 else "Female",
        "Age": age,
        "Excessive Urination (Polyuria)": "Yes" if input_data['Polyuria'] == 1 else "No",
        "Excessive Thirst (Polydipsia)": "Yes" if input_data['Polydipsia'] == 1 else "No",
        "Sudden Weight Loss": "Yes" if input_data['Sudden Weight Loss'] == 1 else "No",
        "Muscle Weakness (Partial Paresis)": "Yes" if input_data['Partial Paresis'] == 1 else "No",
        "Hair Loss (Alopecia)": "Yes" if input_data['Alopecia'] == 1 else "No",
        "Mood Swings (Irritability)": "Yes" if input_data['Irritability'] == 1 else "No",
        "Slow Wound Healing": "Yes" if input_data['Delayed Healing'] == 1 else "No",
        "Skin Itching": "Yes" if input_data['Itching'] == 1 else "No"
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
            "1. Consult with a healthcare professional immediately",
            "2. Schedule blood glucose tests (Fasting and Postprandial)",
            "3. Monitor your blood sugar levels regularly",
            "4. Engage in regular physical activity",
            "5. Maintain a healthy weight",
            "6. Stay hydrated and limit alcohol consumption",
        ]
    else:
        recommendations = [
            "1. Continue with regular health check-ups",
            "2. Maintain a balanced diet with limited processed sugars",
            "3. Engage in regular physical activity (150 mins/week)",
            "4. Monitor your weight and maintain healthy BMI",
            "5. Stay hydrated with water as primary beverage",
            "6. Get sufficient sleep (7-9 hours per night)",
            "7. Manage stress through relaxation techniques",
        ]
    
    for item in recommendations:
        pdf.cell(200, 10, txt=item, ln=1)
    
    return pdf.output(dest='S').encode('latin1')