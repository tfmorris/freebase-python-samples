from apiclient import discovery
from apiclient import model
import json
import os

api_key = open(os.environ['HOME'] + "/.freebase_api_key").read()
model.JsonModel.alt_param = ""
freebase = discovery.build('freebase', 'v1', developerKey=api_key)

response = freebase.search(query='John Smith').execute()
for result in response['results']:
	print result['id']
