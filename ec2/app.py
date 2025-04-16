import streamlit as st
import numpy as np
import joblib
from sklearn.datasets import load_iris

# Load model and dataset
model = joblib.load("iris_model.pkl")
iris = load_iris()

# Title
st.title("🌸 Iris Flower Classifier")
st.write("Enter flower measurements below:")

# Input sliders
sepal_length = st.slider("Sepal length (cm)", 4.0, 8.0, 5.4)
sepal_width = st.slider("Sepal width (cm)", 2.0, 4.5, 3.4)
petal_length = st.slider("Petal length (cm)", 1.0, 7.0, 1.3)
petal_width = st.slider("Petal width (cm)", 0.1, 2.5, 0.2)

# Predict button
if st.button("🔍 Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)[0]
    predicted_class = iris.target_names[prediction]

    st.success(f"The predicted species is: 🌸 **{predicted_class.title()}**")
