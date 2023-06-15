import datetime as dt
import random
import pandas
import os
import shutil
import smtplib

birthday_csv = pandas.read_csv("birthdays.csv")
birthdays = birthday_csv.to_dict("records")
today = dt.datetime.now()

MY_EMAIL = "your-mail"
MY_PASSWORD = "your-password"

def pick_random_letter_copy_letter():
    random_letter = random.choice(os.listdir("letter_templates"))

    shutil.copyfile(f"letter_templates/{random_letter}", "wish_letter.txt")

def rewrite_letter(birthday_name):
    with open("wish_letter.txt", "r") as letter:
        letter_content = letter.read()
        new_letter_content = letter_content.replace('[NAME]', birthday_name)
        return new_letter_content

def send_mail(name, content, to_address):
    with smtplib.SMTP("smtp-mail.outlook.com", 587) as connection:

            # Start a secure encrypted connection.
            connection.starttls()

            # Log in into our mail. Giving Username and Password.
            connection.login(user=MY_EMAIL, password=MY_PASSWORD )

            # Send my mail
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs=to_address, 
                msg=f"Subject: Happy Birthday {name}\n\n{content}"
                )


def check_day():
    for day in birthdays:
        birthday_month = day["month"]
        birthday_day = day["day"]
        name = day["name"]
        if (today.month == birthday_month) and (today.day == birthday_day):
            to_address = day["email"]
            send_mail(name, rewrite_letter(birthday_name=name), to_address)
            


pick_random_letter_copy_letter()
        
check_day()






