import requests
from munch import Munch

# Define the necessary variables
PACKAGE_NAME = 'multikiwilogger'

def search_pkg_by_name(package_name):
    end_point = f"https://api.complyvantage.com/api/packages/find-by-package-name/{package_name}"
    response = requests.get(end_point)
    list_items = response['items']

def test_search_pkg_by_name():
    
    end_point = f"https://api.complyvantage.com/api/packages/find-by-package-name/{PACKAGE_NAME}"

    # Make the get request to get package details
    response = requests.get(end_point)
    return response.json()
    
response = test_search_pkg_by_name()
list_items = response['items']


for list in list_items:
    for k,v in list.items():
        if v == 'multikiwilogger':
            print("Test Case Passed !")
            break

        
# print(split_response)

# if split_response.name == "multikiwilogger":
#     print("Test Case Passed !")
# else:
#     print("Test Case Failed")
    
# list_of_dict = split_response['items']

# for list in list_of_dict:
#     print(list)
    # for k,v in list.items():
    #     print(f"{k} : {v}")

