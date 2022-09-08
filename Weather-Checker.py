from dotenv import load_dotenv
import os

#Environment variables
load_dotenv()

import requests

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 0) * 2 + 30
    feels_like = round(data["main"]["feels_like"] - 273.15, 0) * 2 + 30
    temp_min = round(data["main"]["temp_min"] - 273.15, 0) * 2 + 30
    temp_max = round(data["main"]["temp_max"] - 273.15, 0) * 2 + 30
    
    print("Weather:", weather)
    print("Temperature:", temperature, "F")
    print("Feels Like:", feels_like, "F")
    print("Min:", temp_min, "F", "Max:", temp_max, "F")
else:
    print("An error has occured.")