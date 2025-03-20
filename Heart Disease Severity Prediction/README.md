# **🛠 Tools and Libraries Used in Our Project**  

<div style="display: flex; flex-wrap: wrap; gap: 10px;">  
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white" alt="Streamlit" style="flex: 1 1 30%;">  
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white" alt="Pandas" style="flex: 1 1 30%;">  
  <img src="https://img.shields.io/badge/Numpy-013243?style=flat&logo=numpy&logoColor=white" alt="Numpy" style="flex: 1 1 30%;">  
  <img src="https://img.shields.io/badge/Scikit_Learn-F7931E?style=flat&logo=scikit-learn&logoColor=white" alt="Scikit-Learn" style="flex: 1 1 30%;">  
  <img src="https://img.shields.io/badge/Joblib-3776AB?style=flat&logo=python&logoColor=white" alt="Joblib" style="flex: 1 1 30%;">  
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=flat&logo=python&logoColor=white" alt="Matplotlib" style="flex: 1 1 30%;">  
  <img src="https://img.shields.io/badge/Seaborn-3776AB?style=flat&logo=python&logoColor=white" alt="Seaborn" style="flex: 1 1 30%;">  
  <img src="https://img.shields.io/badge/XGBoost-3776AB?style=flat&logo=xgboost&logoColor=white" alt="XGBoost" style="flex: 1 1 30%;">  
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=flat&logo=tensorflow&logoColor=white" alt="TensorFlow" style="flex: 1 1 30%;">  
  <img src="https://img.shields.io/badge/Keras-D00000?style=flat&logo=keras&logoColor=white" alt="Keras" style="flex: 1 1 30%;">  
  <img src="https://img.shields.io/badge/SHAP-3776AB?style=flat&logo=python&logoColor=white" alt="SHAP" style="flex: 1 1 30%;">  
</div>  

# **💓 Heart Disease Severity Prediction**

## **Introduction**
Heart disease is a major global health concern. Early detection and severity prediction can assist in timely treatment and prevention. This project utilizes machine learning to predict the severity of heart disease based on various medical attributes.

## **Project Overview**
- Dataset: [Heart Disease Dataset](https://www.kaggle.com/datasets/arezaei81/heartcsv)
- Features include age, cholesterol, blood pressure, and other health indicators.
- The project covers data preprocessing, exploratory data analysis (EDA), model building, evaluation, and deployment.
- A web application using Streamlit is developed for easy access to predictions.

## **Objectives**
- Analyze and preprocess the dataset.
- Train and compare classification models.
- Evaluate performance using accuracy and other metrics.
- Develop a Streamlit web app for user interaction.

## **Project Workflow**
### **1. Data Preprocessing & Analysis**
- Loaded and explored the dataset.
- Handled missing values and outliers.
- Performed feature scaling and encoding.

### **2. Model Training & Evaluation**
- Applied multiple classification algorithms (Logistic Regression, Random Forest, SVM, etc.).
- Evaluated models based on accuracy and classification report.
- Selected the best-performing model.

### **3. Web Application (Streamlit)**
- Developed an interactive UI for users to input medical details.
- The model predicts heart disease severity based on input.
- Displays prediction results with a user-friendly interface.

## **Installation & Usage**
### **1. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **2. Run the Streamlit App**
```bash
streamlit run app.py
```

## **Results & Conclusion**
- The best model achieved high accuracy in predicting heart disease severity.
- The Streamlit app provides a simple and accessible way for users to make predictions.
- Future improvements include adding more advanced models and real-time data integration.

