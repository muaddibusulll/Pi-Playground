import requests
from datetime import datetime

APPLICATION_ID = "<Your application ID>"
API_KEY = "<Your API key>"

# You can find these information from Sheety API dashboard 
USERNAME = "<Your Sheety username>"
PROJECT_NAME = "<Your project name>"
SHEET_NAME = "<Your sheet name>"
SHEETY_END_POINT = "<Your end point>"
SHEETY_AUTHENTICATION_TOKEN = "<Your authentication token"
AUTHENTICATION_TYPE = "<Add your authentication type>"

exercise_post_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_url = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"

def get_track_headers():

    headers = {
        "x-app-id": APPLICATION_ID,
        "x-app-key": API_KEY,
        "x-remote-user-id": "0"
    }
    return headers

def get_sheety_headers():

    headers = {"Authorization": f"{AUTHENTICATION_TYPE} {SHEETY_AUTHENTICATION_TOKEN}"}

    return headers

def exercise_post(post_url):

    user_exercise = input("Write witch exercise you did: ")

    workout_exercise = {

        "query": user_exercise
    }

    make_post = requests.post(url=post_url, json=workout_exercise, headers=get_track_headers())

    return make_post.json()

def get_all_workouts_from_sheet():

    get_workouts = requests.get(url=sheety_url)
    return get_workouts.json()


def add_workout_to_sheet():

    user_exercise = exercise_post(post_url=exercise_post_url)["exercises"]
    
    current_day = datetime.now().strftime('%d/%m/%Y')
    current_time =  datetime.now().strftime('%H:%M:%S')
    

    for workout in [workout for workout in user_exercise]:
        sheet_input = {
            f"{SHEETY_END_POINT}" : {
                "date": current_day,
                "time": current_time,
                "exercise": workout['name'].title(),
                "duration": workout['duration_min'],
                "calories": workout['nf_calories']
            }
        }
        requests.post(url=sheety_url, json=sheet_input, headers=get_sheety_headers())
        print(sheet_input)

add_workout_to_sheet()