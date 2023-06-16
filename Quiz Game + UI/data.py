import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

trivia_API = requests.get("https://opentdb.com/api.php?", params=parameters)
trivia_API.raise_for_status()

question_data = trivia_API.json()["results"]