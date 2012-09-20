import urllib
import urllib2
import json

api_key = open('DEVELOPER_KEY').read()
url = 'https://www.googleapis.com/rpc'
request = {
            'method': 'freebase.topic', 
            'apiVersion': 'v1', 
            'params': {
              'id': ['en','bob_dylan'],
              'key': api_key
            }
          }
headers = { 'Content-Type': 'application/json' }

req = urllib2.Request(url, json.dumps(request), headers)
response = urllib2.urlopen(req)
print response.read()
