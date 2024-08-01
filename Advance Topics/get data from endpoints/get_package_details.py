import requests
from munch import Munch

# Define the necessary variables
PACKAGE_ID = 'd5beabd62dbb9832795b6a5ac1cfd0b7a9299f1b0b8b50f3b3e385b88039e926'

def hit_end_pont(end_point):
    response = requests.get(end_point)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def test_get_package_details():
    
    end_point = f"https://api.complyvantage.com/api/packages/{PACKAGE_ID}"
    response = hit_end_pont(end_point)
    split_response = Munch(response)
    
    if (split_response.id == PACKAGE_ID):
        print("Test case Passed !")    
    else:
        print("Test case Failed !")
    
test_get_package_details()