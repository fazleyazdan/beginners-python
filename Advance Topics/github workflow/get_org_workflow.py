import requests

# Define the necessary variables
GITHUB_TOKEN = 'change the token'
OWNER = 'sequenxx'
REPO = 'cv-service-internal'
WORKFLOW_ID = 'trigger_kb_update.yml'  # or you can use the workflow ID

# Set up the API endpoint to get the workflow information
url = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/workflows/{WORKFLOW_ID}"

# Set up the headers with authentication
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {GITHUB_TOKEN}"
}

# Make the GET request to retrieve the workflow information
response = requests.get(url, headers=headers)

# Check the response status and print the workflow information
if response.status_code == 200:
    workflow_info = response.json()
    print(workflow_info)
else:
    print(f"Failed to retrieve workflow information: {response.status_code}")
    print(response.json())
