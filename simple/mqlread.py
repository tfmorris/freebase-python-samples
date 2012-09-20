import json
import urllib
import os

api_key = open(os.environ['HOME'] + "/.freebase_api_key").read()
service_url = 'https://www.googleapis.com/freebase/v1/mqlread'
query = [{'id': None, 'name': None, 'type': '/astronomy/planet'}]
params = {
	'query': json.dumps(query),
	'key': api_key
}
url = service_url + '?' + urllib.urlencode(params)
response = json.loads(urllib.urlopen(url).read())
for planet in response['result']:
  print planet['name']
