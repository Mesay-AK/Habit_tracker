import requests
import datetime

# CREATING A USER

USERNAME = 'kabetobit'
TOKEN = 'ksjojfoekf9084'
GRAPH_ID= 'graph1'

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': "yes",
    'notMinor': "yes",
}

#Checking the User...
# response = requests.post(url=pixela_endpoint, json = user_params)
# print(response.text)


# CREATING A GRAPH DEFINITION

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {'id':GRAPH_ID, 
                'name':'Cycling Graph' , 
                'unit': 'km', 
                'type':'int' , 
                'color':'ajisai'}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Checking the graph defintion...
# response = requests.post(url=graph_endpoint, json = graph_config, headers=headers )
# print(response.text)


#POSTING THE PIXEL TO THE GRAPH

pixel_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today=datetime.datetime.now()

pixel_data={
    'date': today.strftime("%Y%m%d"),
    'quantity': input('How many kilometers did you Cycle today? '),
}

#Checking the creation of the pixels
# response = requests.post(url=pixel_creation_endpoint, json = pixel_data, headers=headers )
# print(response.text)

#UPDATES...

update_endpoint=f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}'

new_pixel_data={
    'quantity':'5'
}

# response = requests.put(url=update_endpoint, json = new_pixel_data, headers=headers )
# print(response.text)

#DELETION...

delete_endpoint=f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}'

# response = requests.delete(url=delete_endpoint, headers=headers )
# print(response.text)

