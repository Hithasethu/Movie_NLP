import streamlit as st
import joblib
import base64

# ✅ Set page config FIRST
st.set_page_config(page_title="Movie Genre Predictor", page_icon="🎬", layout="centered")

# ✅ Load background image from local file
def set_bg(local_img_path):
    with open(local_img_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
                    url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
        color: white;
    }}
    textarea, input {{
        background-color: rgba(255, 248, 220, 0.95) !important;  /* ← light beige */
        color: black !important;
        font-weight: 500;
        border-radius: 8px;
        border: 1px solid #cccccc;
    }}
    label {{
        color: #000000 !important;  /* 👈 dark label text */
        font-weight: 600;
    }}
    .stButton>button {{
        background-color: #f63366;
        color: white;
        border-radius: 10px;
        font-weight: bold;
        padding: 0.5rem 1rem;
    }}
     @media (max-width: 768px) {{
        .stTextInput > div > input,
        .stTextArea > div > textarea {{
            font-size: 16px !important;
        }}
        .stButton > button {{
            width: 100% !important;
            font-size: 18px !important;
        }}
        .stApp {{
            padding-left: 1rem;
            padding-right: 1rem;
        }}
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


set_bg("images.jpeg")  # 👈 Make sure this file exists in the same folder




# Load model and vectorizer
model = joblib.load("genre_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
original_map = joblib.load("genre_map.pkl")
genre_map = {v: k for k, v in original_map.items()}

# Genre emojis
genre_emojis = {
    'fantasy': '🧙‍♂️',
    'horror': '👻',
    'family': '👨‍👩‍👧‍👦',
    'scifi': '👽',
    'action': '💥',
    'crime': '🕵️',
    'adventure': '🧭',
    'mystery': '🔍',
    'romance': '❤️',
    'thriller': '😱'
}

# App title

st.title("🎬 Movie Genre Predictor")
st.markdown("Enter a movie **plot** (and optionally a title), and we'll predict the top  genres.")

# Inputs
title = st.text_input("🎞️ Movie Title (optional)")
plot = st.text_area("📝 Movie Plot", height=200)



# Predict button
if st.button("🔮 Predict Genre"):
    if not plot.strip():
        st.warning("Please enter a movie plot.")
    else:
        X_input = vectorizer.transform([plot])
        probs = model.predict_proba(X_input)[0]
        top3 = probs.argsort()[-3:][::-1]

        if title:
            st.subheader(f"🎞️ **{title}**")
        
        st.markdown("### 🎯 Top  Predicted Genres:")
        with st.container():
            for i in top3:
                if probs[i] > 0.15:
                    genre = genre_map[int(i)]
                    emoji = genre_emojis.get(genre, "")
                   
                    st.markdown(f"""
                    <div style='background-color: rgba(255, 255, 255, 0.85); 
                            padding: 10px; margin-bottom: 10px;
                            border-radius: 8px; color: black;'>
                        <strong style='font-size: 18px'>{emoji} {genre.title()}</strong> 
                        
                    </div>
                    """, unsafe_allow_html=True)
