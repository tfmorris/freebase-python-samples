from apiclient import discovery
from apiclient import model
import json

DEVELOPER_KEY = 'YOUR-KEY-GOES-HERE'
DEVELOPER_KEY = open('DEVELOPER_KEY').read() #hide

model.JsonModel.alt_param = ""
freebase = discovery.build('freebase', 'v1', developerKey=DEVELOPER_KEY)

response = freebase.search(query='John Smith').execute()
for result in response['results']:
	print result['id']
