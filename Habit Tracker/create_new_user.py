import requests

class Create_new_user:

    def __init__(self, token: str, username: str, agreeTerms: str, notMinor: str) -> None:
        self.PIXELA_API_URL = "https://pixe.la/v1/users"
        self.user_parameters = {
            "token": token,
            "username": username,
            "agreeTermsOfService": agreeTerms,
            "notMinor": notMinor,
        }


    def create_user(self):
        response = requests.post(url=self.PIXELA_API_URL, json=self.user_parameters)
        print(response.text)