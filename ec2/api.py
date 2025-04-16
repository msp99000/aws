from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained model
model = joblib.load("iris_model.pkl")

# Define FastAPI app
app = FastAPI(title="Iris Classifier API")

# Request body schema
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def read_root():
    return {"msg": "Iris classifier is up and running!"}

@app.post("/predict")
def predict_species(features: IrisFeatures):
    input_data = np.array([[features.sepal_length,
                            features.sepal_width,
                            features.petal_length,
                            features.petal_width]])
    prediction = model.predict(input_data)[0]
    species = ["setosa", "versicolor", "virginica"][prediction]
    return {"prediction": species}
