import requests
from datetime import datetime
import smtplib
import time

MY_LATITUDE = 59.329323
MY_LONGITUDE = 18.068581

MY_EMAIL = "your-mail"
MY_PASSWORD = "your-password"

my_location = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE
}

# ------------------------ RSS API ------------------------ #
rss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
rss_response.raise_for_status()

# ------------------------ SUNRISE API ------------------------ #
sun_response = requests.get("https://api.sunrise-sunset.org/json?formatted=0&", params=my_location)
sun_response.raise_for_status()

def take_sunrise_hour():
    sunrise = sun_response.json()["results"]["sunrise"]
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    return sunrise_hour

def take_sunset_hour():
    sunset = sun_response.json()["results"]["sunset"]
    sunset_hour = int(sunset.split("T")[1].split(":")[0])
    return sunset_hour

def current_hour():
    time_now = datetime.now()    
    return time_now.hour

def get_iss_position():
    latitude = float(rss_response.json()["iss_position"]["latitude"])
    longitude = float(rss_response.json()["iss_position"]["longitude"])
    iss_position = (latitude, longitude)
    
    return iss_position

def is_ass_above_me():
    if ( (my_location["lat"] - 5) <= get_iss_position()[0] <=  (my_location["lat"] - 5) ) and\
    ( (my_location["lng"] - 5) <= get_iss_position()[1] <=  (my_location["lng"] - 5) ):
        return True
    else:
        return False

def is_night():
    if ( current_hour() >= take_sunset_hour() ) or ( current_hour() <= take_sunrise_hour() ):
        return True
    else:
        return False

def send_mail_for_rss():
    if ( is_ass_above_me() == True ) and ( is_night() == True ):
        with smtplib.SMTP("smtp-mail.outlook.com", 587) as connection:

            # Start a secure encrypted connection.
            connection.starttls()

            # Log in into our mail. Giving Username and Password.
            connection.login(user=MY_EMAIL, password=MY_PASSWORD )

            # Send my mail
            # I used the same mail to send from and destination. Because I want to send this mail to me.
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs=MY_EMAIL,
                msg=f"Subject: RSS Is Here\n\nRss Is Here\nLook to the sky!!"
                )

while True:
    time.sleep(60)
    send_mail_for_rss()