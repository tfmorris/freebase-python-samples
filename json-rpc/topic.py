import urllib
import urllib2
import json
import os

api_key = open(os.environ['HOME'] + "/.freebase_api_key").read()
url = 'https://www.googleapis.com/rpc'
request = {
            'method': 'freebase.topic.lookup', 
            'jsonrpc' : '2.0',
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
