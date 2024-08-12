# Constants for negative Testing
PACKAGE_VERSION_ID_N= '77f05aec40589c0a60501c142390deaa3bef4c67b777d7f569a77738b1a687221'
PACKAGE_ID_N = '77f05aec40589c0a60501c142390deaa3bef4c67b777d7f569a77738b1a687221'
LICENSE_ID_N = '60be5249b6a0aa778bf420abb96fb4564b3af887874887514d6521b079873da52'
EXACT_PACKAGE_N = 'multikiwiloggers'
VERSION_NAME_N = '6.1.0rc01'
LICENSE_EXACT_NAME_N = 'BSD-1-Clause2'
LICENSE_SPDX_ID_N = 'GPL-1.0-onlyl'


#! ======  Negative Testing =======

#! TEST : Get Package Details by package ID
def test_get_package_details():
    
    end_point = f"https://api.complyvantage.com/api/packages/{PACKAGE_ID_N}"
    response = hit_end_pont(end_point)
    
    if (response['id'] == PACKAGE_ID):
        assert True  
    else:
        assert False
        

#! TEST : Get Package Details By Exact Name
def test_search_pkg_by_exact_name():
    end_point = f"https://api.complyvantage.com/api/packages/find-by-exact-package-name/{EXACT_PACKAGE}"
    response = hit_end_pont(end_point)
    list_items = response.get('items', [])
    
    # Check if the response contains the exact package name
    package_names = [item['name'] for item in list_items if 'name' in item]
    if EXACT_PACKAGE in package_names:
        assert True
    else:
        assert False
        
        
#! TEST : Get Package Versions by ID
def test_get_pkg_version():
    
    end_point = f'https://api.complyvantage.com/api/packages/{PACKAGE_VERSION_ID}/versions'
    response = hit_end_pont(end_point)
    list_version = response['items']
    
    #! Validations : Check whether the version associated with the pkg id is > 0
    if len(list_version) > 0:
        assert True
    else:
        assert False


#! TEST: Get Package Version Details by Package ID & Version name
def test_get_pkg_version_details():
    end_point = f'https://api.complyvantage.com/api/packages/{PACKAGE_ID}/find-by-version-name/{VERSION_NAME}'
    response = hit_end_pont(end_point)
    version = response['version_name']
    if VERSION_NAME == version:
        assert True
    else:
        assert False


#! TEST: Get License Details by License ID
def test_get_license_details():
    end_point = f'https://api.complyvantage.com/api/licenses/{LICENSE_ID}'
    response = hit_end_pont(end_point)
    license_id = response['id']
    if license_id == LICENSE_ID:
        assert True
    else:
        assert False
        
        
#! TEST : Get License by Giving exact name
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
        assert True
    else:
        assert False
        
        
#! TEST : Get License via Spdx id
def test_get_license_spdxid():
    end_point = f'https://api.complyvantage.com/api/licenses/search-by-exact-name-or-spdxid/{LICENSE_SPDX_ID}?exact_attribute_name=spdx_id'
    response = hit_end_pont(end_point)
    store_items = response['items']
    spdx_id = [item['spdx_id'] for item in store_items if 'spdx_id' in item]
    if LICENSE_SPDX_ID in spdx_id:
        assert True
    else:
        assert False       