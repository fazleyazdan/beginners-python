import requests
from munch import Munch

# Define the necessary variables
PACKAGE_VERSION_ID= '77f05aec40589c0a60501c142390deaa3bef4c67b777d7f569a77738b1a68722'
PACKAGE_ID = '77f05aec40589c0a60501c142390deaa3bef4c67b777d7f569a77738b1a68722'
LICENSE_ID = '60be5249b6a0aa778bf420abb96fb4564b3af887874887514d6521b079873da5'
PACKAGE_NAME = 'multikiwi'
EXACT_PACKAGE = 'multikiwilogger'
VERSION_NAME = '6.1.0rc0'
LICENSE_PARTIAL = 'apache'
LICENSE_EXACT_NAME = 'BSD-1-Clause'


#! Function for hitting the end point
def hit_end_pont(end_point):
    response = requests.get(end_point)
    if response.status_code == 200:
        return response.json()
    else:
        assert False


def test_get_license_exact_name():
    end_point = f'https://api.complyvantage.com/api/licenses/search-by-exact-name-or-spdxid/{LICENSE_EXACT_NAME}?exact_attribute_name=name'
    response = hit_end_pont(end_point)
    if response['total_count'] == 1:
        assert True
    else:
        assert False
    store_items = response['items']
    exact_license_name = [item['name'] for item in store_items if 'name' in item]
    if LICENSE_EXACT_NAME in exact_license_name:
        print(exact_license_name)
        print(True)
    else:
        print("Test Case Failed")
test_get_license_exact_name()