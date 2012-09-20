from apiclient import discovery, model
import json

DEVELOPER_KEY = 'YOUR-KEY-GOES-HERE'
DEVELOPER_KEY = open('DEVELOPER_KEY').read() #hide
query = [{'id': None, 'name': None, 'type': '/astronomy/planet'}]

model.JsonModel.alt_param = ""
freebase = discovery.build('freebase', 'v1', developerKey=DEVELOPER_KEY)

response = freebase.mqlread(query=json.dumps(query)).execute()
for planet in response['result']:
	print planet['name']
