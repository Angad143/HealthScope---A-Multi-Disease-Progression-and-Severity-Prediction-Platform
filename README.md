# 🩺 🩸**HealthScope - A Multi-Disease Progression and Severity Prediction Platform** ❤️ 🧪

**Developer**: Angad Gupta  
**Project Type**: AI-powered health prediction and assistance system  
**Tech Stack**: Python, Streamlit, Flask, Scikit-learn, XGBoost, TensorFlow, Keras, OpenAI, Google Generative AI, MySQL etc

------------------------------

## 📌 Project Overview
HealthScope is an all-in-one AI-based platform that predicts and monitors multiple diseases, including Diabetes, Heart Disease, and Kidney Disease. It provides both progression and severity analysis, alongside an AI Health Assistant for personalized medical insights using advanced language models.

The platform is deployed using both **Streamlit** (for real-time prediction) and **Flask** (for full-stack user experience including login, dashboard, voice/image/chat medical assistant).

---------------------------

## 🔬 Disease Modules and Features

### 🩸 Diabetes Progression Prediction
[GitHub Repo](https://github.com/Angad143/HealthScope---A-Multi-Disease-Progression-and-Severity-Prediction-Platform/tree/main/Diabetes%20Progression%20Prediction)

**Objective**: Predict whether a person is at risk of early-stage diabetes using clinical data.

#### 📈 Workflow:
- Data Collection: Early Stage Diabetes Risk Prediction Dataset
- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Encoding and Scaling
- Model Training: Logistic Regression, Decision Tree, Random Forest, XGBoost, SVM
- Model Evaluation & Comparison
- Deployment using Streamlit

#### 🚀 Web App Features:
- Patient detail input form
- Real-time diabetes prediction result

#### ✅ Future Enhancements:
- More diverse features
- Deep Learning integration

----------------------------------

### ❤️ Heart Disease Severity Prediction
[GitHub Repo](https://github.com/Angad143/HealthScope---A-Multi-Disease-Progression-and-Severity-Prediction-Platform/tree/main/Heart%20Disease%20Severity%20Prediction)

**Objective**: Predict the severity of heart disease using clinical parameters.

#### 📈 Workflow:
- Dataset: Heart Disease Dataset
- Preprocessing: Missing values, scaling, encoding
- Models: Logistic Regression, Random Forest, SVM (best accuracy: **88.52%**)
- Evaluation: Accuracy, Classification Report
- Deployment using Streamlit

#### 🖥️ Streamlit App:
- Form input for user medical info
- Result shows risk level/severity

#### 🔮 Future Work:
- Real-time health data integration
- Advanced model enhancements

---------------------------------

### 🧪 Kidney Disease Progression Prediction
[GitHub Repo](https://github.com/Angad143/HealthScope---A-Multi-Disease-Progression-and-Severity-Prediction-Platform/tree/main/Kidney%20Disease%20Progression%20Prediction)

**Objective**: Predict chronic kidney disease based on medical attributes.

#### 📈 Workflow:
- Dataset: 14 medical features from Kaggle
- Models: Random Forest, XGBoost
- Evaluation: Accuracy, Precision, Recall

#### 🔍 Features:
- Instant prediction from medical inputs
- Streamlit web app with scaled input handling

#### 🌟 Highlights:
- Real-time prediction
- User-friendly interface
- Early detection

------------------------------

## 🧠 Health Scope - Multi-Disease Prediction System (Streamlit)
[GitHub Repo](https://github.com/Angad143/HealthScope---A-Multi-Disease-Progression-and-Severity-Prediction-Platform/tree/main/Health%20Scope%20-%20Multi-Disease%20Prediction%20System%20(Streamlit))

### 🔎 Features:
- Disease prediction for Diabetes, Heart, Kidney
- AI Chat Assistant using **DeepSeek** / **Google Generative AI**
- Dynamic sidebar navigation
- Disease Report generation in PDF

### 📁 Structure:
```
HealthScope/
 ├── app.py
 ├── requirements.txt
 ├── models/
 ├── pages/
 ├── utils/
 ├── AI_Chatbot/
 ├── Disease_Reports/
```

### 💬 AI Assistant Capabilities:
- Answer user health-related queries
- Provide suggestions and guidance
- Available 24/7 via chat interface

-----------------------------------

## 🌐 HealthScope (Flask Web Application)
[GitHub Repo](https://github.com/Angad143/HealthScope---A-Multi-Disease-Progression-and-Severity-Prediction-Platform/tree/main/Health%20Scope%20-%20Multi-Disease%20Prediction%20System%20(Flask))

### 🖥️ Key Functionalities:
- Secure Login & Registration System
- Dashboard with disease prediction services
- AI Assistant via chat, voice, image, and PDF report analysis

### 🔐 Tech Stack:
- Backend: Flask, MySQL, PyJWT, Flask-Mail
- Frontend: HTML5, CSS3, JavaScript, Bootstrap
- AI & ML: PyTorch, Transformers, LangChain, OpenAI, Ollama

### ⚙ How to Run:
```bash
pip install -r requirements.txt
python app.py
```

---------------------------------------------------
---------------------------------------------------

## 🛠 Tools and Libraries Used
- **Languages & Frameworks**: Python, Flask, Streamlit
- **ML Libraries**: Scikit-learn, XGBoost, TensorFlow, Keras etc
- **NLP Tools**: OpenAI, Google Generative AI, DeepSeek etc
- **Utilities**: Joblib, Pandas, NumPy, Matplotlib, Seaborn, SHAP etc
- **PDF Tools**: FPDF, PyPDF2, pdfplumber

## 📦 Installation Guide

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Angad143/HealthScope---A-Multi-Disease-Progression-and-Severity-Prediction-Platform.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd HealthScope---A-Multi-Disease-Progression-and-Severity-Prediction-Platform
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit Application**:

   ```bash
   cd 'Health Scope - Multi-Disease Prediction System (Streamlit)'
   streamlit run app.py
   ```

5. **Run the Flask Application**:

   ```bash
   cd 'Health Scope - Multi-Disease Prediction System (Flask)'
   python app.py
   ```

-------------------------------------

## 📌 Future Roadmap
- Expand prediction to include more diseases (e.g., Liver, Cancer, Alzheimer’s)
- Connect to real-time health APIs and databases
- Improve AI assistant accuracy with medical NLP models
- Launch as a cross-platform mobile app


## 🤝 Contributors
**Angad Gupta** – Developer & Maintainer  
Connect with me on [GitHub](https://github.com/Angad143)


## 📜 License
This project is for academic and research purposes. It is open-source and contributions are welcome. Not a replacement for professional healthcare advice.


> **Note**: Always consult medical professionals for accurate diagnosis and treatment. HealthScope is an assistance tool and not a substitute for a licensed doctor.

---------------------
