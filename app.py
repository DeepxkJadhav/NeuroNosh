import streamlit as st
from recommender import recommend_foods, predict_food
from utils.nlp_utils import map_text_to_goal

st.set_page_config(page_title="NeuroNosh", layout="centered")
st.title("🧠 NeuroNosh – Brain Food Recommender")

st.markdown("## 🍽️ What do you want to improve today?")
user_input = st.text_input("e.g., Help me focus, reduce stress, improve memory...")

age = st.slider("Select your age", 15, 80, 25)

if user_input:
    goal = map_text_to_goal(user_input)

    st.markdown(f"### 🧠 Based on your age and goal, we recommend:")
    predicted_food = predict_food(age, goal)
    st.success(f"**{predicted_food}** ✅")

    st.markdown("### 🥗 Other foods that can help:")
    results = recommend_foods(goal)
    
    for _, row in results.iterrows():
        st.subheader(row["food"])
        st.write(f"**Nutrients**: {row['nutrients']}")
