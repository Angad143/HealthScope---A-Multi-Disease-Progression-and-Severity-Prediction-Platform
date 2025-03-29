# **Tools and Libraries Used in Our Project**  

<div style="display: flex; flex-wrap: wrap; gap: 10px;">  
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white" alt="Streamlit" style="flex: 1 1 30%;">  
  <img src="https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai&logoColor=white" alt="OpenAI" style="flex: 1 1 30%;">  
  <img src="https://img.shields.io/badge/Datetime-000000?style=flat&logo=python&logoColor=white" alt="Datetime" style="flex: 1 1 30%;">  
  <img src="https://img.shields.io/badge/Google%20Generative%20AI-4285F4?style=flat&logo=google&logoColor=white" alt="Google Generative AI" style="flex: 1 1 30%;">  
  <img src="https://img.shields.io/badge/FPDF-008000?style=flat&logo=pdf&logoColor=white" alt="FPDF" style="flex: 1 1 30%;">  
  <img src="https://img.shields.io/badge/Joblib-1A202C?style=flat&logo=python&logoColor=white" alt="Joblib" style="flex: 1 1 30%;">  
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white" alt="Pandas" style="flex: 1 1 30%;">  
</div>  

------

# **HealthScope - A Multi-Disease Progression and Severity Prediction Platform  (web application using streamlit)**

## **📌 Project Overview**
HealthScope is a **web-based application** built using **Streamlit** that predicts the progression and severity of multiple diseases, including **Diabetes, Heart Disease, and Kidney Disease**. It also features an **AI Health Assistant** to provide insights based on user inputs.

## Features 🚀
- **Disease Prediction**: Predicts the severity of Diabetes, Heart Disease, and Kidney Disease.
- **AI Health Assistant (DeepSeek or Google Generative AI)**: Provides medical insights using AI.
- **User-Friendly UI**: Simple and interactive web interface.
- **Real-time Analysis**: Get instant results based on your input data.

## How to Use 🏥
1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the Application**
   ```bash
   streamlit run app.py
   ```
3. **Navigate through the App**
   - Use the **sidebar** to select different prediction models.
   - Enter your health details and get predictions.
   - Chat with the **AI Health Assistant** for medical queries.

## Project Structure 📂
```
HealthScope/
│── app.py                 # Main application file
│── requirements.txt       # Dependencies
│── models/                # ML models for disease prediction
│── pages/                 # Different disease prediction pages
│── utils/                 # Helper functions and configurations
│── Images/                # Images and static files
│── Disease_Reports/       # different disease pdf files
│── AI_Chatbot/            # Different ai assistance pages   
│── README.md/             # Details about project

```

## Technologies Used 🛠️
- **Python**
- **Streamlit**
- **Machine Learning Models** (for predictions)
- **DeepSeek AI and Google Generative AI** (for Health Assistant)

## Future Improvements 🏗️
- Adding more diseases for prediction.
- Integration with real-time medical databases.
- Improving AI assistant with **better NLP models**.

## Contributors ✨
- **Angad Gupta** - Project Developer

## License 📜
This project is **open-source** and free to use. Contributions are welcome!

---

**📌 Note:** This is an academic project to assist in disease progression analysis. It is not a replacement for professional medical advice. Always consult a doctor for medical concerns. 🚑


