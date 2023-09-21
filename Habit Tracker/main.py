import requests
import create_new_user
import create_graph
from datetime import date, datetime, timedelta

PIXELA_API_URL = "https://pixe.la/v1/users"
USERNAME="your username"
PIXELA_API_TOKEN_KEY="your PIXELA API KEY"
user_graph_api_url = f"{PIXELA_API_URL}/{USERNAME}/graphs"
list_of_graphs_ids = ["graph1", "graph2"]

def get_user_header():
    
    headers={
        "X-USER-TOKEN": PIXELA_API_TOKEN_KEY
    }
    return headers

# ------------------------------------- Create New User -------------------------------------

# Uncomment so to create a new user with a new API KEY.
# new_user = create_new_user.Create_new_user(token=PIXELA_API_TOKEN_KEY, username=USERNAME, agreeTerms="yes", notMinor="yes")
# new_user.create_user()

# ------------------------------------- Create New Graph -------------------------------------

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

def post_new_pixel():

    add_pixel_url = f"{PIXELA_API_URL}/{USERNAME}/graphs/{list_of_graphs_ids[1]}"    
    

    today_date = datetime.today().strftime("%Y%m%d")
    
    pixel_graph_configuration = {
        "date": today_date,
        "quantity": get_input()
    }

    create_new_pixel = requests.post(url=add_pixel_url, json=pixel_graph_configuration, headers=get_user_header())
    print(create_new_pixel.text)

def get_the_exact_date():
    days_ago =input("For how many days ago do you want to make a change to pixels? ")

    try:
        days_ago = int(days_ago)
    except ValueError:
        print("Invalid input. Please ensure that you insert a number.")

    date = (datetime.today() - timedelta(days=days_ago)).strftime("%Y%m%d")

    return date


def change_a_pixel():
    
    change_date = get_the_exact_date()
    change_value = input(f"How much do you want to change the value of your pixel? At {change_date} ")

    change_pixel_configuration = { 
        "quantity": str(change_value),
    }

    change_pixel_url = f"{PIXELA_API_URL}/{USERNAME}/graphs/{list_of_graphs_ids[1]}/{change_date}"

    change_old_pixel = requests.put(url=change_pixel_url, json=change_pixel_configuration, headers=get_user_header())
    print(change_old_pixel.text)


def delete_a_pixel():

    delete_pixel_date = get_the_exact_date()

    delete_pixel_url= f"{PIXELA_API_URL}/{USERNAME}/graphs/{list_of_graphs_ids[1]}/{delete_pixel_date}"

    delete_pixel = requests.delete(url=delete_pixel_url, headers=get_user_header())
    print(delete_pixel.text)


delete_a_pixel()

# change_a_pixel()

#post_new_pixel()