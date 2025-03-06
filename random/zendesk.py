import requests as r
import yaml
import pprint
import base64
import urllib.parse

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

url = config['zendesk_url']
token = config['zendesk_token']
user = config['zendesk_user']

# # Encode the client ID and client secret
authorization = base64.b64encode(bytes(user + "/token:" + token, "ISO-8859-1")).decode("ascii")
# authorization = base64.b64encode(bytes(user + "/" + token, "ISO-8859-1"))
# auth = urllib.parse.quote(authorization)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Basic " + authorization
}

response = r.get(url, headers=headers)

print(response.status_code)

print(authorization)

