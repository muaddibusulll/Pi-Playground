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

weather_hourly = forecast_API_response.json()["hourly"]

def forecast_output(weather_id, will_rain):
    if weather_id >= 200 and weather_id < 300:
        print("It rain heavily\nYou should need an umbrella")
        will_rain = True
        return will_rain
    elif weather_id >= 300 and weather_id < 500:
        print("It will drizzle\nYou should need an umbrella")
        will_rain = True
        return will_rain
    elif weather_id >= 500 and weather_id < 600:
        print("It will rain\nYou should need an umbrella")
        will_rain = True
        return will_rain
    elif weather_id >= 600 and weather_id < 700:
        return("It will snow")
    elif weather_id >= 700 and weather_id < 800:
        return("It will have fog")
    elif weather_id == 800:
        return("It will be clear sky")
    else:
        return("It will have clouds")

will_rain = False

for weather in range(len(weather_hourly[:12])):
    weather_id = weather_hourly[weather]["weather"][0]["id"]
    final_output = forecast_output(weather_id, will_rain=will_rain)
    if final_output == True:        
        print(final_output)
        break
    else:
        print(final_output)
        break