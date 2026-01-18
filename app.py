import streamlit as st
import os
from PIL import Image

# ---------- PATHS ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "assets", "images")
MUSIC_PATH = os.path.join(BASE_DIR, "assets", "music")

# ---------- DATA ----------
mood_images = {
    "happy": "happy.png",
    "calm": "calm.png",
    "stressed": "relax.png",
    "sad": "hope.png"
}

mood_music = {
    "happy": "happy.mp3",
    "calm": "calm.mp3",
    "stressed": "relax.mp3",
    "sad": "hope.mp3"
}

mood_quotes = {
    "happy": "Happiness grows when shared 🌞",
    "calm": "Peace begins with a single breath 🌿",
    "stressed": "This moment will pass — breathe 💙",
    "sad": "Even the darkest night leads to sunrise 🌅"
}

st.set_page_config(page_title="Mental Wellness", layout="wide")

# ---------- SESSION STATE ----------
if "step" not in st.session_state:
    st.session_state.step = 1

if "name" not in st.session_state:
    st.session_state.name = ""

if "confirmed_mood" not in st.session_state:
    st.session_state.confirmed_mood = ""

# ---------- STEP 1: NAME ----------
if st.session_state.step == 1:
    st.title("Welcome 🌿")
    name = st.text_input("Your Name", key="name_input")

    if st.button("Continue", key="name_btn"):
        if name.strip():
            st.session_state.name = name
            st.session_state.step = 2
        else:
            st.warning("Please enter your name")

# ---------- STEP 2: MOOD ----------
elif st.session_state.step == 2:
    st.title(f"Hi {st.session_state.name} 💙")
    st.subheader("How are you feeling today?")

    selected_mood = st.radio(
        "Select your mood",
        ["happy", "calm", "stressed", "sad"],
        key="mood_radio"
    )

    if st.button("Continue", key="mood_btn"):
        st.session_state.confirmed_mood = selected_mood
        st.session_state.step = 3

# ---------- STEP 3: DASHBOARD ----------
elif st.session_state.step == 3:
    mood = st.session_state.confirmed_mood

    # Quote
    st.markdown(
        f"<h3 style='text-align:center;'>{mood_quotes[mood]}</h3>",
        unsafe_allow_html=True
    )

    # Image (SMALLER & MOOD-BASED)
    image_file = os.path.join(IMAGE_PATH, mood_images[mood])
    img = Image.open(image_file).convert("RGB")
    img = img.resize((800, 800))   # 👈 SMALLER SIZE
    st.image(img, use_container_width=800)

    # Music (correct mood)
    music_file = os.path.join(MUSIC_PATH, mood_music[mood])
    st.audio(music_file)

    if st.button("Start Again"):
        st.session_state.clear()
        st.rerun()
