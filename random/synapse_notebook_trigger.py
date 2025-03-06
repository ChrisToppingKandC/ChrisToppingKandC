import requests
import json
from azure.identity import DefaultAzureCredential
import time
import pprint
import uuid

# Variables
workspace_name: str = "pins-synw-odw-dev-uks"
notebook_name: str = "py_utils_get_storage_account"
subscription_id: str = "ff442a29-fc06-4a13-8e3e-65fd5da513b3"
resource_group: str = "pins-rg-data-odw-dev-uks"
polling_interval: int = 10
run_id: str = str(uuid.uuid4())
api_version: str = "2022-03-01-preview"

# Get an access token using Azure Identity
credential: DefaultAzureCredential = DefaultAzureCredential()
token: str = credential.get_token("https://dev.azuresynapse.net/.default")

print("Token obtained...")

# Create the URL for the notebook run API
url = f"https://{workspace_name}.dev.azuresynapse.net/notebooks/runs/{run_id}?api-version={api_version}"

# Define headers for the REST API call
headers = {
    "Authorization": f"Bearer {token.token}",
    "Content-Type": "application/json"
}

params = {
    "notebook": notebook_name
}

# Make the API call to trigger the notebook
response = requests.put(url, headers=headers, data=json.dumps(params))

# Check if the request to start the notebook run was successful
if response.status_code == 202:
    run_response = response.json()
    print(f"Notebook run triggered successfully with run ID: {run_id}")
else:
    print(f"Failed to trigger notebook: {response.status_code} - {response.text}")

# Step 2: Poll for the notebook run status
status_url = f"https://{workspace_name}.dev.azuresynapse.net/notebooks/runs/{run_id}?api-version={api_version}"

while True:
    status_response = requests.get(status_url, headers=headers)

    if status_response.status_code == 200:
        status_data = status_response.json()
        run_status = status_data.get('status')  # This could be Queued, Running, Succeeded, Failed, etc.
        print(f"Current notebook run status: {run_status}")
        
        # Break the loop if the run is completed (either Succeeded or Failed)
        if run_status in ['Succeeded', 'Failed', 'Cancelled']:
            break
    else:
        print(f"Failed to get the run status: {status_response.status_code} - {status_response.text}")
    
    # Wait for a few seconds before polling again
    time.sleep(polling_interval)

# Step 3: Print the exit status and other details
if run_status == "Succeeded":
    print("Notebook completed successfully.")
elif run_status == "Failed":
    print("Notebook run failed.")
else:
    print(f"Notebook run ended with status: {run_status}")
