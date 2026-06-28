# 💻 Laptop Price Predictor

A Machine Learning-powered web application that predicts laptop prices based on hardware specifications such as brand, processor, RAM, storage, display features, GPU, and operating system.

## 🚀 Live Demo

🔗 **Try the application here:**

https://laptop-price-predictor-regression-project-q2qt.onrender.com/

---

## 📌 Features

* Predict laptop prices instantly using Machine Learning
* Modern and responsive user interface
* Supports multiple laptop brands and configurations
* Real-time price estimation
* Interactive input controls
* Publicly deployed on Render

---

## 🛠️ Tech Stack

### Machine Learning

* Python
* Scikit-Learn
* XGBoost
* NumPy
* Pandas

### Frontend

* Streamlit

### Deployment

* Render

---

## 📊 Input Parameters

The model predicts laptop prices using:

* Brand
* Laptop Type
* RAM
* Weight
* Touchscreen Support
* IPS Display
* Screen Resolution
* Screen Size
* CPU Brand
* HDD Capacity
* SSD Capacity
* GPU Brand
* Operating System

---

## 🧠 Machine Learning Pipeline

1. Data Cleaning & Preprocessing
2. Feature Engineering
3. Exploratory Data Analysis (EDA)
4. One-Hot Encoding
5. Model Training
6. Ensemble Learning
7. Model Evaluation
8. Deployment

The final model uses an ensemble-based regression pipeline to improve prediction accuracy and generalization.

---

## 📂 Project Structure

```text
Laptop-Price-Predictor/
│
├── app.py
├── pipe.pkl
├── df.pkl
├── requirements.txt
├── render.yaml
├── README.md
└── assets/
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/Vineet112111/Laptop-Price-Predictor.git
```

### Move into the Project Directory

```bash
cd Laptop-Price-Predictor
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 📈 Sample Prediction

| Configuration                | Predicted Price |
| ---------------------------- | --------------- |
| Acer, 2GB RAM, AMD Processor | ₹23,623         |
| Dell, 8GB RAM, Intel i5      | Dynamic         |
| HP, 16GB RAM, SSD            | Dynamic         |

---

## 🎯 Future Improvements

* Improve prediction accuracy with advanced tuning
* Add laptop recommendation system
* Integrate cloud database support
* Add historical price trend analysis
* Introduce model explainability features
* Build a REST API for third-party integration

---

## 👨‍💻 Author

**Vineet Kumar Yadav**

B.Tech Information Technology
IIIT Sonepat

**GitHub:**
https://github.com/Vineet112111

**LinkedIn:**
https://www.linkedin.com/in/vineet-yadav-68059533a/

---

## ⭐ Support

If you found this project useful:

* ⭐ Star the repository
* 🍴 Fork the project
* 🚀 Share it with others

---

Made with ❤️ using Machine Learning, XGBoost, and Streamlit.
