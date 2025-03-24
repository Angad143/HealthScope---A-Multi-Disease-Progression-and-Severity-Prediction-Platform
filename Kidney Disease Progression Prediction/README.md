# **🛠 Tools and Libraries Used in Our Project**  

<div style="display: flex; flex-wrap: wrap; gap: 10px;">  
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white" alt="Streamlit" style="flex: 1 1 30%;">  
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white" alt="Pandas" style="flex: 1 1 30%;">  
  <img src="https://img.shields.io/badge/Numpy-013243?style=flat&logo=numpy&logoColor=white" alt="Numpy" style="flex: 1 1 30%;">  
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=flat&logo=python&logoColor=white" alt="Matplotlib" style="flex: 1 1 30%;">  
  <img src="https://img.shields.io/badge/Seaborn-3776AB?style=flat&logo=python&logoColor=white" alt="Seaborn" style="flex: 1 1 30%;">  
  <img src="https://img.shields.io/badge/XGBoost-EB5B30?style=flat&logo=xgboost&logoColor=white" alt="XGBoost" style="flex: 1 1 30%;">  
  <img src="https://img.shields.io/badge/Scikit_Learn-F7931E?style=flat&logo=scikit-learn&logoColor=white" alt="Scikit-Learn" style="flex: 1 1 30%;">  
  <img src="https://img.shields.io/badge/Joblib-3776AB?style=flat&logo=python&logoColor=white" alt="Joblib" style="flex: 1 1 30%;">  
</div>  

# Kidney Disease Progression Prediction
## **Project Overview**  

Chronic Kidney Disease (CKD) is a serious condition where kidney function declines over time. Early detection is important to prevent further damage. This project uses **machine learning** to predict CKD based on **14 medical features** like blood pressure, hemoglobin levels, and creatinine levels. The dataset is available on **[Kaggle](https://www.kaggle.com/datasets/abhia1999/chronic-kidney-disease)**.

------

## **Objectives**  
✔ **Analyze** the CKD dataset  
✔ **Preprocess** data for better accuracy  
✔ **Train ML models** like Random Forest & XGBoost  
✔ **Evaluate** models using accuracy, precision & recall  


## **How It Works?**  
1. **User Inputs Data** – The user enters medical details like blood pressure, sugar, and other values.  
2. **Data Processing** – The system **scales the data** to make it ready for the machine learning model.  
3. **Prediction** – The trained model predicts if the person **has kidney disease or not**.  
4. **Result Display** – The result is shown as:  
   ✅ "The person is unlikely to have kidney disease."  
   ❌ "The person is likely to have kidney disease."  


## **Project Structure**  
```
 Kidney_Disease_Prediction
 ┣ 📂 Models
 ┃ ┣ 📜 best_model.pkl
 ┃ ┣ 📜 scaler.pkl
 ┣ 📜 app.py  
 ┣ 📜 Kidney_Disease_Prediction.ipynb
 ┣ 📜 README.md
 ┣ 📜 requirements.txt 
 ┗ 📜 new_model.csv 

```

---

## **How to Run?**  
1️⃣ **Install Required Libraries**  
```bash
pip install -r requirements.txt
```
2️⃣ **Run the Web App**  
```bash
streamlit run app.py
```
3️⃣ **Enter Patient Details & Get Prediction!**  

---

### **Why This Project is Useful?**  
✅ **Early Detection** – Helps detect kidney disease early.  
✅ **User-Friendly** – Easy to use and understand.  
✅ **Fast & Efficient** – Provides instant predictions.  

---

### **Conclusion**  
This project helps predict **kidney disease** using a **machine learning model**. With the help of **Streamlit**, users can input their medical details and get instant predictions. This can help in **early treatment and better health care.**

