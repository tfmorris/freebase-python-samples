from apiclient import discovery
from apiclient import model
import json
import os

api_key = open(os.environ['HOME'] + "/.freebase_api_key").read()
model.JsonModel.alt_param = ""
freebase = discovery.build('freebase', 'v1', developerKey=api_key)
topic = freebase.topic.lookup(id='/en/san_francisco').execute()

for property in topic['property']:
  print property + ':'
  for value in topic['property'][property]['values']:
    print ' - ' + value['text']
