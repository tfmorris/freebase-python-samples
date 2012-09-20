import json
import urllib
import os

api_key = open(os.environ['HOME'] + "/.api_key").read()
query = 'blue bottle'
service_url = 'https://www.googleapis.com/freebase/v1/search'
params = {
	'query': query,
	'key': api_key
}
url = service_url + '?' + urllib.urlencode(params)
response = json.loads(urllib.urlopen(url).read())
for result in response['result']:
    print result['name'] + ' (' + str(result['score']) + ')'
