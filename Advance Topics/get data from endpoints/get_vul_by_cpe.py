import requests

# Define the necessary variables
VUL_CPE = 'cpe:2.3:a:schneider-electric:powerscada_expert_with_advanced_reporting_and_dashboards:8.0:*:*:*:*:*:*:*'

# Function for hitting the end point
def hit_end_point(end_point):
    response = requests.get(end_point)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# TEST: Find Vulnerabilities by exact Cpe
def test_get_vul_by_exact_cpe():
    end_point = f'https://api.complyvantage.com/api/vulnerabilities/find-by-exact-cpe/{VUL_CPE}'
    response = hit_end_point(end_point)
    if response['total_count'] == 1:
        print('true')
        item_details = response['items'][0]['affected_package_details']
        cpe = item_details.get('cpe')
        print('CPE:', cpe)
    else:
        print('No data found or request failed.')

test_get_vul_by_exact_cpe()
