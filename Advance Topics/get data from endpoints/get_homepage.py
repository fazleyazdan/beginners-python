import requests

def hit_end_point(end_point):
    response = requests.get(end_point)
    if response.status_code == 200:
        return response.text
    else:
        return False
    
def get_homepage():
    end_point = 'https://api.complyvantage.com/prd/'
    response = hit_end_point(end_point)
    if response:
        print(response)
    else:
        print(response)
        print('test case failed')
        
get_homepage()
    