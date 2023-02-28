import requests
import os
from datetime import datetime

API_ID = os.environ["API_ID"]
API_KEY = os.environ["API_KEY"]

GENDER = "male"
WEIGHT = 62
HEIGHT = 180.2
AGE = 21

EXERCISE_ENDPOINT = os.environ["EXERCISE_ENDPOINT"]
SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]

exercise_input = input("Tell me which exercises you did today? ")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}
parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=EXERCISE_ENDPOINT, json=parameters, headers=headers)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    SHEET_TOKEN = {"Authorization": f"Bearer {os.environ['SHEET_TOKEN']}"}
    sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs, headers=SHEET_TOKEN)

