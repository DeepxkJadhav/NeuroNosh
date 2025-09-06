import pandas as pd
import joblib
import os

MODEL_PATH = "models/food_model.pkl"

def load_data(path="data/foods.csv"):
    return pd.read_csv(path)

def load_model():
    model = joblib.load(MODEL_PATH)
    goal_enc = joblib.load("models/goal_encoder.pkl")
    food_enc = joblib.load("models/food_encoder.pkl")
    return model, goal_enc, food_enc

def predict_food(age, goal):
    model, goal_enc, food_enc = load_model()
    goal_encoded = goal_enc.transform([goal])[0]
    prediction = model.predict([[age, goal_encoded]])
    food = food_enc.inverse_transform(prediction)[0]
    return food
