import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal
from fastapi.middleware.cors import CORSMiddleware
import joblib

model = joblib.load("../models/best_model.pkl")
scaler = joblib.load("../models/scaler.pkl")

app = FastAPI(
    title="Lagos Travel Time Prediction API",
    description="Predicts inter-city travel time in Nigeria using road and environmental features.",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TravelInput(BaseModel):
    road_length_km: float = Field(..., gt=0, description="Length of the road segment in kilometers")
    weather: Literal[0, 1, 2, 3] = Field(..., description="0=Clear, 1=Cloudy, 2=Rainy, 3=Foggy")
    direction: Literal[0, 1] = Field(..., description="1 if route is FROM Lagos, 0 if TO Lagos")
    congestion_level: Literal[1, 2, 3] = Field(..., description="1=Low, 2=Medium, 3=High")

@app.post("/predict-time")
def predict_travel_time(data: TravelInput):
    input_df = pd.DataFrame([[
        data.road_length_km,
        data.weather,
        data.direction,
        data.congestion_level
    ]], columns=['Road Length (km)', 'Weather', 'direction', 'Congestion Level'])

    scaled_features = scaler.transform(input_df)
    prediction = model.predict(scaled_features)[0]

    return {
        "predicted_travel_time_min": round(prediction, 2)
    }