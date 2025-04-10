import streamlit as st
import random
import time
from streamlit_extras.let_it_rain import rain

# Game Settings
GAME_DURATION = 30  # seconds
CROSSHAIR = "🎯"
MAX_TARGETS = 1

st.set_page_config(page_title="🎯 Military Aim Trainer", layout="centered")
st.title("🪖 Military Aim Trainer")
st.write("Click the targets as fast as you can! You have 30 seconds.")

# Game State
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.start_time = None
    st.session_state.game_over = False
    st.session_state.target_position = None

# Start Game
if st.button("Start Game"):
    st.session_state.score = 0
    st.session_state.start_time = time.time()
    st.session_state.game_over = False
    st.session_state.target_position = (random.randint(100, 500), random.randint(100, 400))

# Gameplay Logic
if st.session_state.start_time:
    elapsed = time.time() - st.session_state.start_time

    if elapsed > GAME_DURATION:
        st.session_state.game_over = True

    if not st.session_state.game_over:
        st.write(f"⏱️ Time Left: {int(GAME_DURATION - elapsed)}s")
        st.write(f"🎯 Score: {st.session_state.score}")

        pos_x, pos_y = st.session_state.target_position

        # Render target button
        target_clicked = st.button(CROSSHAIR, key=f"target_{pos_x}_{pos_y}")

        if target_clicked:
            st.session_state.score += 1
            st.session_state.target_position = (random.randint(100, 500), random.randint(100, 400))
            rain(emoji="💥", font_size=30, falling_speed=3, animation_length="short")

    else:
        st.success(f"Game Over! Final Score: {st.session_state.score}")
        if st.button("Play Again"):
            st.session_state.start_time = time.time()
            st.session_state.score = 0
            st.session_state.game_over = False
            st.session_state.target_position = (random.randint(100, 500), random.randint(100, 400))
