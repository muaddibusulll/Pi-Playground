import requests

parameters = {
    "city": "Stockholm",
    "appID": "6b5f7c1b959c058e4659bd65fea1b114",
    "exclude": "current,minutely,alerts,daily"
}

# exclude: current,minutely,hourly,alerts,daily

weather_API_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={parameters['city']}&appid={parameters['appID']}")

weather_API_response.raise_for_status()

latitude = weather_API_response.json()["coord"]["lat"] 

longitude = weather_API_response.json()["coord"]["lon"] 

print(f"Latitude: {latitude}\nLongitude: {longitude}")

forecast_API_response = requests.get(f"https://api.openweathermap.org/data/2.8/onecall?lat={latitude}&lon={longitude}&exclude={parameters['exclude']}&appid={parameters['appID']}")

forecast_API_response.raise_for_status()

for weather in range(len(forecast_API_response.json()["hourly"])):
    print(forecast_API_response.json()["hourly"][weather]["weather"])
