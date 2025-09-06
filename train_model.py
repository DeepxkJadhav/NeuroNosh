import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
df = pd.read_csv("data/nutrition_data_with_labels.csv")

# Encode categorical goal labels (you may have multiple goal flag columns)
df['goal'] = df[['focus_boost','memory_boost','anti_stress']].idxmax(axis=1)
df['goal_encoded'] = LabelEncoder().fit_transform(df['goal'])
df['food_encoded'] = LabelEncoder().fit_transform(df['food'])

features = ['calories', 'protein', 'fat', 'fiber', 'carbs']
X = df[features + ['goal_encoded']]
y = df['food_encoded']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model and encoders
joblib.dump(model, "models/food_model.pkl")
joblib.dump(LabelEncoder().fit(df['goal']), "models/goal_encoder.pkl")
joblib.dump(LabelEncoder().fit(df['food']), "models/food_encoder.pkl")

print("Model trained with nutrition features and saved.")
