import requests
import smtplib
from datetime import datetime



# In this section you need to change the >> appid << so make the program to work.
# The APP ID you can find it from the the provided link.
# Weather API link.
# https://openweathermap.org/
# "Zurich"
city = "Zurich"
appid = "<your APP ID>"
exclude = "current,minutely,alerts,daily"
# exclude: current,minutely,hourly,alerts,daily

# Mail section
# You need to change the:
# >> MY_EMAIL  
# >> MY_PASSWORD
# >> to_address
MY_EMAIL = "<your mail send from>"
MY_PASSWORD = "<your mail's password>"
to_address="<mail address you want to send to>"

parameters = {
    "city": city,
    "appID": appid,
    "exclude": exclude
}

# --------------------- Weather API ---------------------

# Use weather API so to get latitude and longitude.

weather_API_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={parameters['city']}&appid={parameters['appID']}")

weather_API_response.raise_for_status()

latitude = weather_API_response.json()["coord"]["lat"] 

longitude = weather_API_response.json()["coord"]["lon"] 

print(f"Latitude: {latitude}\nLongitude: {longitude}")

# Use onecall from Openweathermap API so to check if will rain in the current city.

forecast_API_response = requests.get(f"https://api.openweathermap.org/data/2.8/onecall?lat={latitude}&lon={longitude}&exclude={parameters['exclude']}&appid={parameters['appID']}")

forecast_API_response.raise_for_status()

weather_hourly = forecast_API_response.json()["hourly"]

def return_day() -> datetime.date:
    current_day = datetime.now()    
    return current_day.date()

def return_forecast_text(weather_id: int) -> str:
    if weather_id >= 200 and weather_id < 300:
        forecast_text = "It rain heavily\nYou should need an umbrella"
        return forecast_text
    elif weather_id >= 300 and weather_id < 500:
        forecast_text = "It will drizzle\nYou should need an umbrella"
        return forecast_text
    elif weather_id >= 500 and weather_id < 600:
        forecast_text = "It will rain\nYou should need an umbrella"
        return forecast_text
    elif weather_id >= 600 and weather_id < 700:
        forecast_text = "It will snow\nYou should need an umbrella"
        return forecast_text
    elif weather_id >= 700 and weather_id < 800:
        forecast_text = "It will have fog"
        return forecast_text
    elif weather_id == 800:
        forecast_text = "It will be clear sky"
        return forecast_text
    else:
        forecast_text = "It will have clouds"
        return forecast_text
    
def will_rain(weather_id: int) -> bool:
    if weather_id < 700:
        return True
    else:
        return False
    
def send_mail(mail_text: str, today_date: datetime.date):
    mail_text = f"For city: {city} \n{mail_text}"
    with smtplib.SMTP("smtp-mail.outlook.com", 587) as connection:
        
        # Start a secure encrypted connection.
        connection.starttls()
        
        # Log in into our mail. Giving Username and Password.
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        
        # Send my mail
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=to_address,
            msg=f"Subject: Forecast for today: {today_date}\n\n{mail_text}"
        )

for weather in range(len(weather_hourly[:12])):
    weather_id = weather_hourly[weather]["weather"][0]["id"]
    will_need_umbrella = will_rain(weather_id)
    if will_need_umbrella == True:
        break

if will_need_umbrella == True:
    print(return_forecast_text(weather_id=weather_id))
    forecast_text = return_forecast_text(weather_id=weather_id)
    send_mail(mail_text=forecast_text, today_date=return_day())
else:
    print(return_forecast_text(weather_id=weather_id))
    forecast_text = return_forecast_text(weather_id=weather_id)
    send_mail(mail_text=forecast_text, today_date=return_day())