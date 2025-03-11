import requests
import json
import os
from requests.exceptions import HTTPError

api_key = os.getenv('OPENWEATHER_API_KEY')
url = f'https://api.openweathermap.org/data/2.5/weather?q=Tashkent&appid={api_key}'

response = requests.get(url)
res_json = response.json()

# Convert temperature from Kelvin to Celsius
temperature = res_json["main"]["temp"] - 273.15
humidity = res_json["main"]["humidity"]
pressure = res_json["main"]["pressure"]

print(f"Temperature - {temperature:.2f} Celsius")
print(f"Humidity - {humidity}%")
print(f"Pressure - {pressure} hPa")