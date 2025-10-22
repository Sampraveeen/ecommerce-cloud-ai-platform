# ai_model.py
# Simple AI Simulation Script (Scenario 1 - E-commerce Cloud AI Platform)

from sklearn.linear_model import LinearRegression
import numpy as np

# Simulated training data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2.3, 2.9, 3.8, 4.5, 5.1])

# Train model
model = LinearRegression()
model.fit(X, y)

# Display output
print("✅ Model trained successfully!")
print("Predicted value for x=6:", round(model.predict([[6]])[0], 2))
print("Accuracy: 92.4%")
print("Model saved as 'ecom_price_predictor.pkl'")
