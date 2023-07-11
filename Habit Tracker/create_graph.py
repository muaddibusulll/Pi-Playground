import requests

class Create_new_graph:

    def __init__(self, id: str, name: str, unit: str, type: str, color: str, token: str) -> None:
        
        self.my_graph_configuration = {
            "id" : id,
            "name" : name,
            "unit" : unit,
            "type" : type,
            "color" : color
        }
    
        self.headers = {
            "X-USER-TOKEN": token
        }    

    def create_new_graph(self, user_graph_api_url):
        graph_response = requests.post(url=user_graph_api_url, json=self.my_graph_configuration, headers=self.headers)
        print(graph_response.text)