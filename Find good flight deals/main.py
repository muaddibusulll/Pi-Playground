import requests

USERNAME = "<Your Sheety username>"
PROJECT_NAME = "<Your project name>"
SHEET_NAME = "<Your sheet name>"
SHEETY_END_POINT = "<Your end point>"

sheety_url = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"


def get_sheet_information():

    return requests.get(url=sheety_url).json()


def get_airport_iata_code():

    return [i["iataCode"] for i in get_sheet_information()[f"{SHEET_NAME}"]]
        


print(get_airport_iata_code())

