import smtplib
import datetime as dt
import random

quotes_list = open("quotes.txt").readlines()

# Add your mail here. From witch you want to send mail.
MY_EMAIL = "your mail"
# Add your mail Password.
MY_PASSWORD = "your_password"

TO_ADDRESS = "mail you want to send"

def check_day():
    if dt.datetime.now().weekday() == 2:
        return (random.choice(quotes_list))


def send_motivational_mail():
    # Here we need to write our mail provider server.
    # For Gmail: smtp.gmail.com
    # For Hotmail: smtp-mail.outlook.com
    # For Yahoo: smtp.mail.yahoo.com
    # 
    with smtplib.SMTP("smtp-mail.outlook.com", 587) as connection:

        # Start a secure encrypted connection.
        connection.starttls()

        # Log in into our mail. Giving Username and Password.
        connection.login(user=MY_EMAIL, password=MY_PASSWORD )

        # Send my mail
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=TO_ADDRESS, 
            msg=f"Subject: Test motivation\n\n{check_day()}"
            )

send_motivational_mail()