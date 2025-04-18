from flask import Flask, render_template, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from config import Config
from auth.login import login
from auth.register import register
from auth.forgot_password import forgot_password, reset_password
from auth.activate_account import activate_account
from flask import request, send_file, jsonify
from prediction_diseases.diabetes import DiabetesPredictor
from prediction_diseases.heart import HeartDiseasePredictor
from prediction_diseases.kidney import KidneyDiseasePredictor
import io
import numpy as np
import os
from flask import current_app
from datetime import datetime
from AI_Powered_Medical_Insights.ai_health_assistant import AIHealthAssistant
from AI_Powered_Medical_Insights.ai_voice_assistant import AIVoiceHealthAssistant
from AI_Powered_Medical_Insights.ai_image_diagnosis import diagnose_image
from AI_Powered_Medical_Insights.medical_report_analysis import process_medical_report, analyze_query

# Create a Flask web application instance
app = Flask(__name__)
app.config.from_object(Config)

# Initialize MySQL and Bcrypt (to be used in the Flask app)
mysql = MySQL(app)
bcrypt = Bcrypt(app)

# Main index route
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

# Set up routes and views for login
@app.route("/login", methods=["GET", "POST"])
def login_user():
    return login(mysql, bcrypt)

# Set up routes and views for registration
@app.route("/register", methods=["GET", "POST"])
def register_user():
    return register(mysql, bcrypt)

# Set up routes and views for account activation
@app.route("/activate_account")
def activate_account_route():
    return activate_account(mysql)

# Set up routes and views for forgot password and reset password
@app.route("/forgot_password", methods=["GET", "POST"])
def forgot_password_user():
    return forgot_password(mysql)

@app.route("/reset_password", methods=["GET", "POST"])
def reset_password_user():
    return reset_password(mysql, bcrypt)

# Set up routes and views for about and help pages
@app.route("/help")
def help_questions():
    return render_template("help.html")

# Set up dashboard route (requires user to be logged in)
@app.route("/dashboard")
def dashboard():
    if session.get("logged_in"):  # ✅ Use .get() to avoid KeyError
        return render_template("dashboard.html", user=session["user_name"])
    else:
        flash("Please log in first!", "warning")
        return redirect(url_for("login_user"))

# Details about different disease route
@app.route("/disease_details")
def disease_details():
    if session.get("logged_in"):  # ✅ Use .get() to avoid KeyError
        return render_template("disease_details.html", user=session["user_name"])
    else:
        flash("Please log in first!", "warning")
        return redirect(url_for("login_user"))

# Set up logout route (clears session data and flashes a message)
@app.route("/logout")
def logout():
    session.clear()  # Clears all session data, including flash messages
    # flash("You have been logged out!", "info")
    return redirect(url_for("home"))

################################ Diabetes Diseases Prediction ###########################################
# Initialize the predictor
diabetes_predictor = DiabetesPredictor()

def convert_numpy_types(obj):
    """Convert numpy types to native Python types for JSON serialization"""
    if isinstance(obj, (np.integer)):
        return int(obj)
    elif isinstance(obj, (np.floating)):
        return float(obj)
    elif isinstance(obj, (np.ndarray,)):
        return obj.tolist()
    elif isinstance(obj, dict):
        return {k: convert_numpy_types(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_numpy_types(v) for v in obj]
    return obj

@app.route('/diabetes-prediction', methods=['GET', 'POST'])
def diabetes_prediction():
    if request.method == 'POST':
        # Get form data and make prediction
        prediction, pdf_report = diabetes_predictor.predict(request.form)
        
        # Convert numpy types to native Python types
        prediction = convert_numpy_types(prediction)
        
        # Store the PDF in session for download
        session['diabetes_report'] = pdf_report.decode('latin1') if isinstance(pdf_report, bytes) else pdf_report
        session['diabetes_prediction'] = prediction
        
        # Render the template with prediction result
        return render_template('diabetes.html', prediction=prediction, user=session["user_name"])
    
    # For GET requests, just show the form
    return render_template('diabetes.html', prediction=None, user=session["user_name"])

@app.route('/download-diabetes-report')
def download_diabetes_report():
    # Retrieve the PDF from session
    pdf_content = session.get('diabetes_report')
    if not pdf_content:
        return redirect(url_for('diabetes_prediction'))
    
    # Create a file-like object in memory
    pdf_file = io.BytesIO(pdf_content.encode('latin1') if isinstance(pdf_content, str) else io.BytesIO(pdf_content))
    
    # Send the file as a download
    return send_file(
        pdf_file,
        mimetype='application/pdf',
        as_attachment=True,
        download_name='diabetes_risk_report.pdf'
    )

################################ Heart Disease Prediction ###########################################
# Initialize the predictor
heart_predictor = HeartDiseasePredictor()

@app.route('/heart-disease-prediction', methods=['GET', 'POST'])
def heart_disease_prediction():
    if request.method == 'POST':
        # Get form data and make prediction
        prediction, pdf_report = heart_predictor.predict(request.form)

        # Convert numpy types to native Python types
        prediction = convert_numpy_types(prediction)

        # 🔥 Ensure temp folder exists
        temp_folder = os.path.join(current_app.root_path, 'static/temp')
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)  # Create the folder if it doesn't exist

        # 🔥 Store PDF in a temporary directory instead of session
        temp_path = os.path.join(temp_folder, 'heart_report.pdf')
        with open(temp_path, "wb") as f:
            f.write(pdf_report)

        session['heart_report_path'] = temp_path  # Store **only** the file path
        session['heart_prediction'] = prediction

        print(f"✅ PDF Saved at: {temp_path}")  # Debugging print

        return render_template('heart.html', prediction=prediction, user=session["user_name"])

    return render_template('heart.html', prediction=None, user=session["user_name"])

@app.route('/download-heart-report')
def download_heart_report():
    # Retrieve stored **file path** instead of binary data
    pdf_path = session.get('heart_report_path')

    if not pdf_path or not os.path.exists(pdf_path):
        print("❌ ERROR: PDF file missing!")  # Debugging print
        return redirect(url_for('heart_disease_prediction'))

    print(f"📂 Downloading PDF from: {pdf_path}")  # Debugging print

    return send_file(
        pdf_path,
        mimetype='application/pdf',
        as_attachment=True,
        download_name='heart_disease_risk_report.pdf'
    )

################################ Kidney Disease Prediction ###########################################
# Initialize the predictor
kidney_predictor = KidneyDiseasePredictor()

@app.route('/kidney-disease-prediction', methods=['GET', 'POST'])
def kidney_disease_prediction():
    if request.method == 'POST':
        # Get form data and make prediction
        prediction, pdf_report = kidney_predictor.predict(request.form)

        # Convert numpy types to native Python types
        prediction = convert_numpy_types(prediction)

        # 🔥 Ensure temp folder exists
        temp_folder = os.path.join(current_app.root_path, 'static/temp')
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)  # Create the folder if it doesn't exist

        # 🔥 Store PDF in a temporary directory instead of session
        temp_path = os.path.join(temp_folder, 'kidney_report.pdf')
        with open(temp_path, "wb") as f:
            f.write(pdf_report)

        session['kidney_report_path'] = temp_path  # Store **only** the file path
        session['kidney_prediction'] = prediction

        print(f"✅ PDF Saved at: {temp_path}")  # Debugging print

        return render_template('kidney.html', prediction=prediction, user=session["user_name"])

    return render_template('kidney.html', prediction=None, user=session["user_name"])


@app.route('/download-kidney-report')
def download_kidney_report():
    # Retrieve stored **file path** instead of binary data
    pdf_path = session.get('kidney_report_path')

    if not pdf_path or not os.path.exists(pdf_path):
        print("❌ ERROR: PDF file missing!")  # Debugging print
        return redirect(url_for('kidney_disease_prediction'))

    print(f"📂 Downloading PDF from: {pdf_path}")  # Debugging print

    return send_file(
        pdf_path,
        mimetype='application/pdf',
        as_attachment=True,
        download_name='kidney_disease_risk_report.pdf'
    )

################################ AI Health Assistant ###########################################
def datetime_format(value, format="%H:%M"):
    if isinstance(value, str):
        value = datetime.fromisoformat(value)
    return value.strftime(format)

app.jinja_env.filters['datetimeformat'] = datetime_format

@app.route("/ai-health-assistant", methods=["GET", "POST"])
def ai_health_assistant():
    assistant = AIHealthAssistant()
    chat_history = assistant.initialize_chat_history(session)
    
    if request.method == "POST":
        user_input = request.form.get("user_input")
        button_clicked = request.form.get("button_clicked")
        
        # Call the assistant's response handler
        chat_history = assistant.handle_user_input(session, user_input=user_input, button_clicked=button_clicked)

    return render_template("ai_health_assistant.html", chat_history=chat_history, user=session["user_name"])

################################ AI Voice Health Assistant ###########################################
assistant = AIVoiceHealthAssistant()

@app.route('/ai-voice-assistant')
def ai_voice_assistant():
    return render_template('ai_voice_assistant.html', user=session["user_name"])

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form.get('user_input', '').strip()
    if not user_input:
        return jsonify({'response': 'Please ask a question.'})
    
    response = assistant.process_query(user_input)
    return jsonify({'response': response})

################################ Medical Images Diagnosis ###########################################
@app.route('/ai-image-diagnosis', methods=['GET', 'POST'])
def ai_image_diagnosis():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            diagnosis_result = diagnose_image(file)
            return {'result': diagnosis_result}
    return render_template('ai_image_diagnosis.html', user=session["user_name"])


################################## Medical Report Analysis System #########################################

app.config['UPLOAD_FOLDER'] = 'AI_Powered_Medical_Insights/Uploaded_Medical_Report/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/medical-report-analysis')
def medical_report_analysis():
    return render_template('medical_report_analysis.html', user=session["user_name"])

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and file.filename.lower().endswith('.pdf'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        # Process the medical report
        result = process_medical_report(filepath)
        if result.get('error'):
            return jsonify(result), 400
        return jsonify({'message': 'File processed successfully'})
    else:
        return jsonify({'error': 'Please upload a PDF file'}), 400

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({'error': 'No query provided'}), 400
    
    query = data['query']
    response = analyze_query(query)
    return jsonify(response)

###########################################################################

if __name__ == "__main__":
    app.run(debug=True)
