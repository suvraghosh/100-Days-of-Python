import requests
from datetime import datetime

USERNAME = "suvra"
TOKEN = "gsyhoshkshtrhskd"
GRAPH_ID = "graph2"

# Step1: Create your user account

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)


# Step2: Create a graph definition

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Programming Graph",
    "unit": "hr",
    "type": "int",
    "color": "ajisai"
}

# It is the authentication token specified at the time of user registration.
headers = {
    "X-USER-TOKEN": TOKEN
}

"""
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
"""

# Step3: To get the graph!You need to run https://pixe.la/v1/users/suvra/graphs/graph2.html this in the server.

# Step4: Post value to the graph

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2023, month=2, day=25)
# today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? "),
}

"""
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
"""

# Update the pixel

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_pixel_data = {
    "quantity": input("How many hours did you code today? "),
}

"""
response = requests.put(url=update_pixel_endpoint, json=update_pixel_data, headers=headers)
print(response.text)
"""

# Delete the pixel

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

"""
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
"""
