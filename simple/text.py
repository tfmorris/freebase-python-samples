import sys
import json
import urllib
import os

api_key = open(os.environ['HOME'] + "/.freebase_api_key").read()
topic_id = '/en/bob_dylan'
service_url = 'https://www.googleapis.com/freebase/v1/text'
url = service_url + topic_id + '?key=' + api_key;
response = json.loads(urllib.urlopen(url).read())
print response['result']

