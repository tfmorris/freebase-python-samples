from apiclient import discovery, model
from apiclient.http import BatchHttpRequest
import json
import os

api_key = open(os.environ['HOME'] + "/.freebase_api_key").read()
query1 = [{"name~=":"*doubt*","name":None,"type":"/media_common/quotation","author":[{"name":"William Shakespeare"}]}]
query2 = [{"name~=":"*law*","name":None,"type":"/media_common/quotation","author":[{"name":"William Shakespeare"}]}]

model.JsonModel.alt_param = ""
freebase = discovery.build('freebase', 'v1', developerKey=api_key)

def display_results(request_id, response, exception):
	for topic in json.loads(response)['result']:
		print topic['name']

batch = BatchHttpRequest(callback=display_results)
batch.add(freebase.mqlread(query=json.dumps(query1)))
batch.add(freebase.mqlread(query=json.dumps(query2)))
batch.execute()
