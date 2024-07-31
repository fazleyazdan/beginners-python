import requests
from munch import Munch

# Define the necessary variables
PACKAGE_ID = 'd5beabd62dbb9832795b6a5ac1cfd0b7a9299f1b0b8b50f3b3e385b88039e926'

def test_get_package_details():
    
    end_point = f"https://api.complyvantage.com/api/packages/{PACKAGE_ID}"

    # Make the get request to get package details
    response = requests.get(end_point)
    return response
    
response = test_get_package_details()
split_response = Munch(response.json())

if (split_response.id == PACKAGE_ID):
    print("Test case Passed !")
    
else:
    print("Test case Failed !")
    