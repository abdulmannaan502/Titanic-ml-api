from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from schema.graphql import graphql_app  

# Load model and encoders
model = joblib.load("model/titanic_model.pkl")
label_encoders = joblib.load("model/label_encoders.pkl")

# FastAPI app
app = FastAPI(title="Titanic Prediction API")

# REST Input schema
class Passenger(BaseModel):
    Pclass: int
    Sex: str
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Embarked: str

# Preprocessing function
def preprocess_input(passenger: Passenger):
    data = passenger.dict()
    df = pd.DataFrame([data])
    for col, le in label_encoders.items():
        df[col] = le.transform(df[col])
    return df

# REST endpoint
@app.post("/predict")
def predict(passenger: Passenger):
    input_df = preprocess_input(passenger)
    prediction = model.predict(input_df)[0]
    return {"survived": bool(prediction)}

# Mount GraphQL app
app.include_router(graphql_app, prefix="/graphql")
