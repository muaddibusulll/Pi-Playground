# Weather API link.
# https://openweathermap.org/

import requests

city = "Stockholm"
appid = ""
exclude = "current,minutely,alerts,daily"
# exclude: current,minutely,hourly,alerts,daily

parameters = {
    "city": city,
    "appID": appid,
    "exclude": exclude
}

weather_API_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={parameters['city']}&appid={parameters['appID']}")

weather_API_response.raise_for_status()

latitude = weather_API_response.json()["coord"]["lat"] 

longitude = weather_API_response.json()["coord"]["lon"] 

print(f"Latitude: {latitude}\nLongitude: {longitude}")

forecast_API_response = requests.get(f"https://api.openweathermap.org/data/2.8/onecall?lat={latitude}&lon={longitude}&exclude={parameters['exclude']}&appid={parameters['appID']}")

forecast_API_response.raise_for_status()

weather_hourly = forecast_API_response.json()["hourly"]

def forecast_output(weather_id: int, will_rain: bool):
    if weather_id >= 200 and weather_id < 300:
        forecast_text = "It rain heavily\nYou should need an umbrella"
        will_rain = True 
        return will_rain, forecast_text
    elif weather_id >= 300 and weather_id < 500:
        forecast_text = "It will drizzle\nYou should need an umbrella"
        will_rain = True
        return will_rain, forecast_text
    elif weather_id >= 500 and weather_id < 600:
        forecast_text = "It will rain\nYou should need an umbrella"
        will_rain = True
        return will_rain, forecast_text
    elif weather_id >= 600 and weather_id < 700:
        forecast_text = "It will snow\nYou should need an umbrella"
        will_rain = True
        return will_rain, forecast_text
    elif weather_id >= 700 and weather_id < 800:
        forecast_text = "It will have fog"
        will_rain = False
        return will_rain, forecast_text
    elif weather_id == 800:
        forecast_text = "It will be clear sky"
        will_rain = False
        return will_rain, forecast_text
    else:
        forecast_text = "It will have clouds"
        will_rain = False
        return will_rain, forecast_text

will_rain = False

for weather in range(len(weather_hourly[:12])):
    weather_id = weather_hourly[weather]["weather"][0]["id"]
    final_output = forecast_output(weather_id, will_rain=will_rain)
    if final_output[0] == True:
        print(final_output[1])
    else:
        print(final_output[1])