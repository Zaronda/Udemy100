import requests

USERNAME = "geronimocat"
TOKEN = "kjfkjkjjfdsjkjkj"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# this post was successful, now comment out
#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN,
}

graph_config = {
    "id": "graph1",
    "name": "Gym Graph",
    "unit": "15 mins",
    "type": "int",
    "color": "ajisai",
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
