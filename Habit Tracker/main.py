import requests
import create_new_user
import create_graph
from datetime import date, datetime

PIXELA_API_URL = "https://pixe.la/v1/users"
USERNAME="your username"
PIXELA_API_TOKEN_KEY="your PIXELA API KEY"
user_graph_api_url = f"{PIXELA_API_URL}/{USERNAME}/graphs"
list_of_graphs_ids=[]

# ------------------------------------- Create New User -------------------------------------

# Uncomment so to create a new user with a new API KEY.
# new_user = create_new_user.Create_new_user(token=PIXELA_API_TOKEN_KEY, username=USERNAME, agreeTerms="yes", notMinor="yes")
# new_user.create_user()

# ------------------------------------- Create New Graph -------------------------------------

list_of_graphs_ids = ["graph1", "graph2"]
# Uncomment so to create a new user with a new API KEY.
# new_graph = create_graph.Create_new_graph(id="graph2", name="Coding-Graph", unit="Minutes", type="int", color="shibafu", token=PIXELA_API_TOKEN_KEY)
# new_graph.create_new_graph(user_graph_api_url=user_graph_api_url)

# ------------------------------------- Create Graph Input -------------------------------------

def get_input():
    while True:
        try:
            quantity=input("Insert how much did you work today ")
            return quantity
        except ValueError:
            print("Not accurate value")

add_pixel_url = f"{PIXELA_API_URL}/{USERNAME}/graphs/{list_of_graphs_ids[1]}"

headers={
    "X-USER-TOKEN": PIXELA_API_TOKEN_KEY
}

today_date = datetime.today().strftime("%Y%m%d")

pixel_graph_configuration = {
    "date": today_date,
    "quantity": get_input()
}

create_new_pixel = requests.post(url=add_pixel_url, json=pixel_graph_configuration, headers=headers)
print(create_new_pixel.text)