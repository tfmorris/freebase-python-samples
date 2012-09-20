import urllib
import urllib2
import json

api_key = open('DEVELOPER_KEY').read()
url = 'https://www.googleapis.com/rpc'
request = {
  'method': 'freebase.search', 
  'apiVersion': 'v1', 
  'params': {
    'query': 'nirvana',
    'key': api_key
  }
}
headers = { 'Content-Type': 'application/json' }

req = urllib2.Request(url, json.dumps(request), headers)
response = urllib2.urlopen(req)
print response.read()
