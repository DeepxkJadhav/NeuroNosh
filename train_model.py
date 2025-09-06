import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# Sample dataset
data = pd.DataFrame({
    'age': [20, 25, 30, 35, 40, 45, 22, 28, 32, 38],
    'goal': ['focus', 'memory', 'anti-stress', 'focus', 'memory', 'anti-stress', 'focus', 'memory', 'anti-stress', 'focus'],
    'food': ['Dark Chocolate', 'Blueberries', 'Spinach', 'Salmon', 'Walnuts', 'Avocado', 'Dark Chocolate', 'Blueberries', 'Spinach', 'Salmon']
})

# Encode categorical columns
goal_enc = LabelEncoder()
food_enc = LabelEncoder()

data['goal_encoded'] = goal_enc.fit_transform(data['goal'])
data['food_encoded'] = food_enc.fit_transform(data['food'])

# Train model
X = data[['age', 'goal_encoded']]
y = data['food_encoded']

model = RandomForestClassifier()
model.fit(X, y)

# Save model and encoders
joblib.dump(model, 'models/food_model.pkl')
joblib.dump(goal_enc, 'models/goal_encoder.pkl')
joblib.dump(food_enc, 'models/food_encoder.pkl')

print("✅ Model trained and saved.")
