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

