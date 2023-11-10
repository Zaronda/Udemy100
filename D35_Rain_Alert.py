import requests
import os
from Twilio.rest import Client

# hourly seems to be paid subscription
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
#OWM_Endpoint = "https://pro.openweathermap.org/data/2.5/forecast/hourly"

api_key = "3d3f544343fe97033899107b5caf2c2d"

MY_LAT = "51.391810"
MY_LONG = "-0.450201"

# Params dictionary: Lat, long as floats
weather_params = {
    "lat": 51.391810,
    "lon": -0.450201,
    "appid": api_key,
}

# https://api.openweathermap.org/data/2.5/weather?lat={51.391810}&lon={-0.45020}&appid={"3d3f544343fe97033899107b5caf2c2d"}

response = requests.get(OWM_Endpoint, params=weather_params)
#print(response.status_code)
weather_data = response.json()
weather_slice = weather_data["wind"]
print(weather_slice)
# hourly not available?
#print(weather_data["hourly"] [0] ["weather"] [0] ["id"])
#print(weather_data["main"] [0] ["weather"] [0] ["id"])
# slice condition code out of hourly weather
~if int(condition_code) < 700:
#    print("Bring an umbrella.")





