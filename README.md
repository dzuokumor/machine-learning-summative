# Lagos Travel Time Prediction

## Mission and Problem

This project is part of my mission to **improve quality of life using technology in urbanization and governance**.

Traffic congestion between Lagos and other Nigerian cities is a major urbanization problem, causing delays and reducing productivity.

Using machine learning, this solution predicts travel time based on distance, congestion, direction, and weather.

The goal: **help citizens and city planners make better travel decisions and optimize route planning**.

**Dataset Description & Source**  
The dataset contains structured records of travel routes between Nigerian states, with features like distance, congestion level, weather, road conditions, and estimated travel time. It was originally designed to train a Random Forest-based Traffic Advisory System using realistic data sourced via the GraphHopper API.  
**Source:** [Nigerian States Travel Data – Kaggle](https://www.kaggle.com/datasets/vektur/nigerian-states-travel-data)


## Public API

The model is deployed as a REST API.

Base URL:  
**https://machine-learning-summative.onrender.com/**

Use the Swagger UI to test predictions directly in the browser:  
[Swagger UI Documentation](https://machine-learning-summative.onrender.com/docs)

### Example POST request

`POST /predict-time`

```json
{
  "road_length_km": 250,
  "weather": 0,
  "direction": 1,
  "congestion_level": 2
}
```

## Demo Video

YouTube demo (≤ 5 min):  
[Demo Video](https://youtu.be/R0edFghd1gQ)

## Mobile App

A Flutter mobile app is provided for a user-friendly interface.

### How to Run the App

1. Install Flutter (if not already installed):  
   [Flutter installation guide](https://docs.flutter.dev/get-started/install)

2. Clone the repository:
   ```bash
   git clone https://github.com/dzuokumor/machine-learning-summative.git
   cd machine-learning-summative/machine_learning_summative_flutter_app
   ```

3. Get packages:
   ```bash
   flutter pub get
   ```

4. Run on emulator or phone:
   ```bash
   flutter run
   ```

### How to Use the App

1. Select a city from the dropdown (distance auto-fills).
2. (Optional) Adjust the road distance manually.
3. Choose direction (FROM Lagos or TO Lagos).
4. Select traffic congestion (Light / Moderate / Heavy).
5. Choose weather condition (Clear, Cloudy, Rainy, Foggy).
6. Tap PREDICT TRAVEL TIME.
7. The app calls the API.
8. Results appear with:
   - Predicted travel time in minutes
   - Approximate hours
   - Informational notes about predictions
9. Error messages will display if the API request fails.

## Features

- 48 Nigerian cities supported
- Real-time predictions using a machine learning backend
- Swagger-based API for external testing
