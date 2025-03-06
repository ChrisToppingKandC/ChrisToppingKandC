import requests as r
import yaml
import pprint
import base64

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

url = config['url']
baseurl = config['baseurl']
key = config['key']
secret = config['secret']
username = config['username']
password = config['password']

# # Encode the client ID and client secret
# authorization = base64.b64encode(bytes(key + ":" + secret, "ISO-8859-1")).decode("ascii")

headers = {
    "Accept": "application/vnd.api+json",
    "Content-Type": "application/vnd.api+json"
}
body = {
    "grant_type": "password",
    "client_id": key,
    "client_secret": secret,
    "username": username,
    "password": password
}

response = r.post(url, json=body, headers=headers)

# print(response.status_code)

# if 'access_token' in response.json():
#     print(response.json()['access_token'])

headers = {
    "Accept": "application/vnd.api+json",
    "Content-Type": "application/vnd.api+json",
    "Authorization": "Bearer " + response.json()['access_token']
}

# swagger_definition = '{}/V8/meta/swagger.json'.format(baseurl)

# swagger = r.get(swagger_definition, headers=headers)

# modules = '{}/V8/meta/modules'.format(baseurl)

dataMap = '{}/V8/module/IMS_master_data_map'.format(baseurl)

moduleData = r.get(dataMap, headers=headers)

pprint.pprint(moduleData.json())

