import requests

# Define the necessary variables
GITHUB_TOKEN = 'change the token'
OWNER = 'fazleyazdan7'
REPO = 'github-api'
WORKFLOW_ID = 'main.yml'  # or you can use the workflow ID

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


trigger_url = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/workflows/{WORKFLOW_ID}/dispatches"

# Define the payload with the branch or tag to run the workflow on
data = {
    "ref": "main"  # or the branch/tag you want to run the workflow on
}

# Make the POST request to trigger the workflow
response = requests.post(trigger_url, headers=headers, json=data)

# Check the response status and print the result
if response.status_code == 204:
    print("Workflow triggered successfully!")
else:
    print(f"Failed to trigger workflow: {response.status_code}")
    print(response.json())