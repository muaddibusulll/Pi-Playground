import requests
import smtplib
import os
import logging
from datetime import datetime
from typing import Tuple, Dict

logging.basicConfig(level=logging.INFO)

# Weather condition codes
HEAVY_RAIN = 200
LIGHT_RAIN = 300
MILD_RAIN = 500
SNOW = 600
FOG = 700
CLEAR_SKY = 800

class EmailSender:
    SMTP_SERVER = "smtp-mail.outlook.com"
    SMTP_PORT = "587"

    def __init__(self, email_info: Dict[str, str]):
        self.email_info = email_info
    
    def send_email(self, subject: str, message: str):
        try:
            with smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT) as connection:
                # Start a secure encrypted connection.
                connection.starttls()
                # Log in into our mail. Giving Username and Password.
                connection.login(user=self.email_info["email"], password=self.email_info["password"])
                # Send my mail
                connection.sendmail(
                    from_addr=self.email_info["email"],
                    to_addrs=self.email_info["to_address"],
                    msg=f"Subject: Forecast for today: {subject}\n\n{message}"
                )
        except Exception as exception:
            logging.error(f"Failed to send email: {exception}")
            raise

class WeatherNotifier:
    BASE_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
    BASE_FORECAST_URL = "https://api.openweathermap.org/data/2.8/onecall"

    def __init__(self, city: str, app_id: str, email_sender: EmailSender):
        self.city = city
        self.app_id = app_id
        self.email_sender = email_sender
        self.latitude, self.longitude = self.get_coordinates()

    def get_coordinates(self) -> Tuple[float, float]:
        parameters = {
            "q": self.city,
            "appid": self.app_id
        }

        response = requests.get(self.BASE_WEATHER_URL, params=parameters)
        response.raise_for_status()

        coordinate_data = response.json()
        return coordinate_data["coord"]["lat"], coordinate_data["coord"]["lat"]
    
    def get_forecast(self) -> Dict:
        parameters = {
            "lat": self.latitude,
            "lon": self.longitude,
            "exclude": "current,minutely,alerts,daily",
            "appid": self.app_id
        }

        response = requests.get(self.BASE_FORECAST_URL, params=parameters)
        response.raise_for_status()

        return response.json()
    
    def return_day(self) -> datetime.date:
        current_day = datetime.now()    
        return current_day.date()

    def return_forecast_text(self, weather_id: int) -> str:
        if weather_id >= HEAVY_RAIN and weather_id < LIGHT_RAIN:
            return "It rain heavily\nYou should need an umbrella"
        elif weather_id >= LIGHT_RAIN and weather_id < MILD_RAIN:
            return "It will drizzle\nYou should need an umbrella"
        elif weather_id >= MILD_RAIN and weather_id < SNOW:
            return "It will rain\nYou should need an umbrella"
        elif weather_id >= SNOW and weather_id < FOG:
            return "It will snow\nYou should need an umbrella"
        elif weather_id >= FOG and weather_id < CLEAR_SKY:
            return "It will have fog"
        elif weather_id == CLEAR_SKY:
            return "It will be clear sky"
        else:
            return "It will have clouds"
        
    def notify(self):
        try:
            forecast = self.get_forecast()
            for weather in forecast["hourly"][:12]:
                weather_id = weather["weather"][0]["id"]
                if weather_id < 700:
                    forecast_text = self.return_forecast_text(weather_id)
                    self.email_sender.send_email(subject=self.return_day(), message=f"City: {self.city}\n" + forecast_text)
                    break
        except Exception as exception:
            logging.error(f"Failed to send weather notification: {exception}")
            raise

if __name__ == "__main__":
    email_info = {
        "email": "difuslo@hotmail.com",
        "password" : "1234567~!A",
        "to_address": "sifis.k.i@gmail.com"
    }

    email_sender = EmailSender(email_info=email_info)
    weather_notifier = WeatherNotifier(city="Lyon", app_id="6b5f7c1b959c058e4659bd65fea1b114", email_sender=email_sender)
    weather_notifier.notify()