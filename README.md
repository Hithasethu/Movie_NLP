# 🎬 Movie Genre Predictor

Predict the top  most likely genres of a movie based on its **plot summary** using **Natural Language Processing (NLP)** and **Machine Learning**.

![App Screenshot](https://github.com/Hithasethu/Movie_NLP/blob/main/Screenshot%202025-06-13%20012653.png) <!-- optional, replace with your image path -->

## 🚀 Live App

👉 [Try the App on Streamlit](https://movienlp-tcwpstfcvvaphq52xwij5u.streamlit.app/)

---

## 📌 Project Overview

This Streamlit web application takes a movie plot and returns the **top 3 predicted genres** with confidence scores. It uses a Logistic Regression model trained on a dataset of 90,000+ movie descriptions.

### ✅ Key Features
- Input a plot, get **genre predictions** (multi-label)
- Trained using **TF-IDF Vectorization + Logistic Regression**
- Fully deployed with **Streamlit Cloud**
- Responsive UI with genre emojis and background styling


---

## 📂 Tech Stack

- **Python** (NLP, ML)
- **scikit-learn**, **joblib**
- **Streamlit** for web UI
- **TF-IDF** for vectorization
- **pandas**, **numpy**,**Matplotlib**,**seaborn**
- **Deployment**: Streamlit Cloud

---

## 📁 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/Hithasethu/Movie_NLP.git


# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
