
import streamlit as st
from recommender import recommend_foods
from utils.nlp_utils import map_text_to_goal

st.set_page_config(page_title="NeuroNosh", layout="centered")
st.title("🧠 NeuroNosh – Brain Food Recommender")

st.markdown("### What do you want to improve today?")
user_input = st.text_input("Type here (e.g., I want better memory, help me focus, reduce stress...)")

if user_input:
    goal = map_text_to_goal(user_input)
    st.markdown(f"### Recommended Foods for **{goal.capitalize()}** 🍽️")
    
    results = recommend_foods(goal)
    
    for _, row in results.iterrows():
        st.subheader(row["food"])
        st.write(f"**Nutrients**: {row['nutrients']}")
