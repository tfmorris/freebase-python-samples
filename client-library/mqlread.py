from apiclient import discovery, model
import json
import os

api_key = open(os.environ['HOME'] + "/.freebase_api_key").read()
query = [{'id': None, 'name': None, 'type': '/astronomy/planet'}]

model.JsonModel.alt_param = ""
freebase = discovery.build('freebase', 'v1', developerKey=api_key)

response = json.loads(freebase.mqlread(query=json.dumps(query)).execute())
for planet in response['result']:
	print planet['name']
