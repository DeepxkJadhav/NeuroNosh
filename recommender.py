import pandas as pd

def load_data(path="data/foods.csv"):
    return pd.read_csv(path)

def recommend_foods(goal="focus"):
    df = load_data()
    if goal == "focus":
        return df[df['focus_boost'] == 1]
    elif goal == "memory":
        return df[df['memory_boost'] == 1]
    elif goal == "anti-stress":
        return df[df['anti_stress'] == 1]
    else:
        return df
