import requests
from munch import Munch

# Define the necessary variables
PACKAGE_VERSION_ID= '77f05aec40589c0a60501c142390deaa3bef4c67b777d7f569a77738b1a68722'
PACKAGE_ID = '77f05aec40589c0a60501c142390deaa3bef4c67b777d7f569a77738b1a68722'
PACKAGE_NAME = 'multikiwi'
EXACT_PACKAGE = 'multikiwilogger'
VERSION_NAME = '6.1.0rc0'


#! Function for hitting the end point
def hit_end_pont(end_point):
    response = requests.get(end_point)
    if response.status_code == 200:
        return response.json()
    else:
        assert False


#! TEST: Get Package Version Details by Package ID & Version name
def test_get_pkg_version_details():
    end_point = f'https://api.complyvantage.com/api/packages/{PACKAGE_ID}/find-by-version-name/{VERSION_NAME}'
    response = hit_end_pont(end_point)
    print(response)
    version = response['version_name']
    if VERSION_NAME == version:
        print("Test case Passed")
    else:
        print("Test case Failed")

test_get_pkg_version_details()