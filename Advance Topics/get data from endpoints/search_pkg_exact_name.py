import requests
from munch import Munch

# Define the necessary variables
PACKAGE_NAME = 'multikiwilogger'

def get_package_by_exact_name(package_name):
    end_point = f"https://api.complyvantage.com/api/packages/find-by-exact-package-name/{package_name}"
    response = requests.get(end_point)
    if response.status_code == 200:
        return response.json()

def test_search_pkg_by_exact_name():
    response = get_package_by_exact_name(PACKAGE_NAME)
    list_items = response.get('items', [])
    
    # Check if the response contains the package name
    package_names = [item['name'] for item in list_items if 'name' in item]
    if PACKAGE_NAME in package_names:
        print("Test Case Passed!")
    else:
        print("Test Case Failed")
        
    # assert PACKAGE_NAME in package_names, f"Package name '{PACKAGE_NAME}' not found in response items" 

# if __name__ == "__main__":
#     test_search_pkg_by_name()
#     print("Test Case Passed!")

test_search_pkg_by_exact_name()
# for list in list_items:
#     for k,v in list.items():
#         if v == 'multikiwilogger':
#             print("Test Case Passed !")
#             break
