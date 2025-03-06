import requests
import json
import time
from azure.identity import DefaultAzureCredential

CREDENTIAL = DefaultAzureCredential()
WORKSPACE_NAME = "pins-synw-odw-dev-uks"
SPARK_POOL_NAME = "pinssynspodw"

token = CREDENTIAL.get_token("https://dev.azuresynapse.net/.default").token

livy_url = f"https://{WORKSPACE_NAME}.dev.azuresynapse.net/livyApi/versions/2019-11-01-preview/sparkPools/{SPARK_POOL_NAME}/sessions"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

path = "abfss://odw-raw@pinsstodwdevuks9h80mb.dfs.core.windows.net/ct_test"
script_filename = "create_spark_session_script.py"
script_path = f"{path}/{script_filename}"

payload = {
    "name": "Chris spark session test",
    "files": [script_path],
    "arguments": [],
    "conf": {
        "spark.driver.cores": "2",
        "spark.executor.cores": "2",
        "spark.driver.memory": "2g",
        "spark.executor.memory": "2g",
        "spark.executor.instances": "2"
    }
}

response = requests.post(livy_url, headers=headers, data=json.dumps(payload))

if response.status_code == 200:
    print("Job submitted successfully")
    session_id = response.json()['id']  # Get the session ID
    print(f"Session ID: {session_id}")

    # Check session status periodically
    while True:
        session_status_response = requests.get(f"{livy_url}/{session_id}", headers=headers)
        status = session_status_response.json().get('state')

        print(f"Current session status: {status}")

        if status in ["idle", "running", "success", "error"]:
            break  # Exit loop if the job is in a final state

        time.sleep(10)  # Wait before checking again

    print("Final session status:", status)
else:
    print(f"Failed to submit job: {response.status_code} - {response.text}")