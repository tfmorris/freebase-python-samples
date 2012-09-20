import json
import urllib
import os

api_key = open(os.environ['HOME'] + "/.freebase_api_key").read()
query = [{'id': None, 'name': None, 'type': '/location/country'}]
service_url = 'https://www.googleapis.com/freebase/v1/mqlread'
params = {
	'query': json.dumps(query),
	'cursor': '',
	'key': api_key
}
while params['cursor'] != False:
	url = service_url + '?' + urllib.urlencode(params)
	response = json.loads(urllib.urlopen(url).read())
	for result in response['result']:
	  print result['name']
	params['cursor'] = response['cursor']
