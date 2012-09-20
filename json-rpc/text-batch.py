import urllib
import urllib2
import json

url = 'https://www.googleapis.com/rpc'
requests = [{
  'method': 'freebase.text.get', 
  'apiVersion': 'v1', 
  'params': {
    'id': ['en','bob_dylan']
  }
},{
  'method': 'freebase.text.get', 
  'apiVersion': 'v1', 
  'params': {
    'id': ['en','blade_runner']
  }
}]
headers = { 'Content-Type': 'application/json' }
req = urllib2.Request(url, json.dumps(requests), headers)
response = urllib2.urlopen(req)
print response.read()
