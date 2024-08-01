import requests
from munch import Munch

# Define the necessary variables
PACKAGE_NAME = 'multikiwi'
exact_package = 'multikiwilogger'

def get_package_by_name():
    end_point = f"https://api.complyvantage.com/api/packages/find-by-package-name/{PACKAGE_NAME}"
    response = requests.get(end_point)
    if response.status_code == 200:
        return response.json()

def test_search_pkg_by_name():
    response = get_package_by_name()
    list_items = response.get('items', [])

    # Check if the response contains the package name
    package_names = [item['name'] for item in list_items if 'name' in item]
    assert exact_package in package_names, f"Package name '{exact_package}' not found in response items"
    if len(list_items) > 0: 
        if exact_package in package_names:
            print("Test Case Passed!")
        else:
            print("Test Case Failed")
    else:
        print("Test Case Failed")
       
test_search_pkg_by_name()