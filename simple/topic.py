import json
import urllib
import os

api_key = open(os.environ['HOME'] + "/.freebase_api_key").read()
service_url = 'https://www.googleapis.com/freebase/v1/topic'
topic_id = '/m/0d6lp'
params = {
  'key': api_key,
  'filter': 'suggest'
}
url = service_url + topic_id + '?' + urllib.urlencode(params)
topic = json.loads(urllib.urlopen(url).read())

for property in topic['property']:
  print property + ':'
  for value in topic['property'][property]['values']:
    print ' - ' + value['text']
