import urllib
import urllib2
import json
import os

api_key = open(os.environ['HOME'] + "/.freebase_api_key").read()
url = 'https://www.googleapis.com/rpc'
query = [{
  'id':'/en/blade_runner',
  'name':None
}]
request = {
  'method': 'freebase.mqlread', 
  'apiVersion': 'v1', 
  'params': {
    'query': json.dumps(query)
  }
}
headers = { 'Content-Type': 'application/json' }

req = urllib2.Request(url, json.dumps(request), headers)
response = urllib2.urlopen(req)
print response.read()
