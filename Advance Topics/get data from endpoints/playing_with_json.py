import json

# Here in this code we used built in JSON library to work with json file
# here i am demonstrating how to access different members/properties in json file
# split right the json file to get a better idea of how accessing works

def playing_with_json():
    with open('response.json', 'r') as file:
        data = json.load(file)
    return data

data = playing_with_json()

print(data['total_count'])
print(data['items'][0]['vulnerability_details'])
print(data['items'][0]['vulnerability_details']['credits'][0]['name'])
print(data['items'][0]['affected_package_details']['cpe'])
