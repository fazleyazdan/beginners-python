import requests
from munch import Munch

PACKAGE_ID= '77f05aec40589c0a60501c142390deaa3bef4c67b777d7f569a77738b1a68722'

def test_get_pkg_version():
    
    end_point = f'https://api.complyvantage.com/api/packages/{PACKAGE_ID}/versions'
    response = requests.get(end_point)
    
    assert response.status_code == 200
    response = response.json()
    list_version = response['items']
    
    if len(list_version) > 0:
        print(len(list_version))
        assert True
    else:
        print("test case failed!")
        assert False
    
test_get_pkg_version()
    
    