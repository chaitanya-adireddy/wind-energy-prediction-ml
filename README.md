# 🌬️ Wind Energy Prediction Using Machine Learning

## 📌 Project Overview

This project predicts wind turbine power output based on weather parameters using a **Random Forest Regression** model.
It integrates **real-time weather data** using the **OpenWeatherMap API** and provides an interactive **Streamlit web application** with a modern user interface.

The system demonstrates how machine learning can be applied to renewable energy forecasting and efficient power management.

---

## 🎯 Features

* 📊 Wind turbine power prediction using machine learning
* 🌤 Real-time weather data integration (OpenWeatherMap API)
* 🧭 Automatic wind speed and wind direction input for prediction
* 🖥 Multi-page Streamlit interface (Welcome → Weather → Prediction)
* 📈 Model evaluation using regression metrics and graphs
* 🔐 Secure API key using environment variables

---

## 🧠 Machine Learning Workflow

1. Data collection from Kaggle (Wind Turbine SCADA dataset)
2. Data preprocessing and feature selection
3. Train–test split
4. Model training using **Random Forest Regressor**
5. Model evaluation using MAE, RMSE, and R² Score
6. Model saved as `wind_energy_model.pkl`
7. Deployment using Streamlit

---

## 📂 Project Structure

```
wind-energy-prediction/
│
├── data/
│   ├── T1.csv
│   └── cleaned_data.csv
│
├── images/
│   ├── actual_vs_predicted.png
│   └──error_distribution.png
│   
│
├── app.py
├── wind_energy_model.pkl
├── requirements.txt
├── README.md
└── notebook/
    └── wind_energy_prediction.ipynb
```

---

## 🌤 Real-Time Weather Integration

Weather data is fetched using the **OpenWeatherMap API**.
The application automatically extracts:

* Temperature
* Humidity
* Pressure
* Wind Speed
* Wind Direction

Wind parameters are directly passed to the machine learning model for power prediction.

---

## 🖥 Streamlit Application Flow

1. **Welcome Page** – Project introduction
2. **Weather Section** – Select a city and fetch live weather data
3. **Prediction Section** – Auto-filled wind parameters used to predict power output

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/wind-energy-prediction.git
cd wind-energy-prediction
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set OpenWeatherMap API Key

#### ▶️ Linux / Mac

```bash
export OPENWEATHER_API_KEY="your_api_key_here"
```

#### ▶️ Windows (PowerShell)

```powershell
setx OPENWEATHER_API_KEY "your_api_key_here"
```

---

### 4️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

---

## 📚 Dataset

Wind Turbine SCADA Dataset from Kaggle
https://www.kaggle.com/datasets/berkerisen/wind-turbine-scada-dataset

---

## 🧪 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Streamlit
* OpenWeatherMap API
* Joblib

---

## 🎓 Academic Relevance

This project demonstrates:

* Regression modeling for renewable energy
* Data preprocessing and feature selection
* Model evaluation using statistical metrics
* Real-time API integration
* Interactive machine learning deployment

---

## 🚀 Future Enhancements

* Real-time SCADA data integration
* Deep learning models for time-series forecasting
* Cloud deployment using Streamlit Cloud or Render
* Historical prediction visualization

---

## 👨‍💻 Author

**Adireddy Chaitanya**
B.Tech – Electronics and Communication Engineering
Chaitanya Institute of Science and Technology

---

## 📜 License

This project is developed for academic and educational purposes.
