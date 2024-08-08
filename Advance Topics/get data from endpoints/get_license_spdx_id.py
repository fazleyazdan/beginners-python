import requests

LICENSE_SPDX_ID = 'GPL-1.0-only'

#! Function for hitting the end point
def hit_end_pont(end_point):
    response = requests.get(end_point)
    if response.status_code == 200:
        return response.json()
    else:
        assert False


#! TEST : Get License via Spdx id
def test_get_license_spdxid():
    end_point = f'https://api.complyvantage.com/api/licenses/search-by-exact-name-or-spdxid/{LICENSE_SPDX_ID}?exact_attribute_name=spdx_id'
    response = hit_end_pont(end_point)
    store_items = response['items']
    spdx_id = [item['spdx_id'] for item in store_items if 'spdx_id' in item]
    print(spdx_id)
    
test_get_license_spdxid()