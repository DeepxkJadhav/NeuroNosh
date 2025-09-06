import streamlit as st
from recommender import predict_food, recommend_foods
from utils.nlp_utils import map_text_to_goal
import pandas as pd

st.title("🧠 NeuroNosh – Smarter Brain Food Recommender")
user_input = st.text_input("How can we help your brain today?")
age = st.slider("Age", 15, 80, 25)

# Collect nutrition inputs
st.markdown("### Nutritional Preferences")
calories = st.number_input("Calories (approx)", 50, 1000, 300)
protein = st.number_input("Protein (g)", 0.0, 100.0, 5.0)
fat = st.number_input("Total Fat (g)", 0.0, 100.0, 5.0)
fiber = st.number_input("Fiber (g)", 0.0, 50.0, 2.0)
carbs = st.number_input("Carbs (g)", 0.0, 200.0, 20.0)

if user_input:
    goal = map_text_to_goal(user_input)
    nutrition_input = {
        'calories': calories,
        'protein': protein,
        'fat': fat,
        'fiber': fiber,
        'carbs': carbs
    }
    suggested = predict_food(age, goal, nutrition_input)
    st.success(f" Based on your goal and nutrition input, try: **{suggested}**")
    
    st.markdown("### Other options for this goal:")
    results = recommend_foods(goal)
    for _, row in results.iterrows():
        st.write(f"- **{row['food']}** — Nutrients: {row['nutrients']}")
