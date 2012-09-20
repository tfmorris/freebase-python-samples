from apiclient import discovery
from apiclient import model
import json

DEVELOPER_KEY = 'YOUR-KEY-GOES-HERE'
DEVELOPER_KEY = open('DEVELOPER_KEY').read() #hide

model.JsonModel.alt_param = ""
freebase = discovery.build('freebase', 'v1', developerKey=DEVELOPER_KEY)
topic = freebase.topic.lookup(id='/en/san_francisco').execute()

for property in topic['property']:
  print property + ':'
  for value in topic['property'][property]['values']:
    print ' - ' + value['text']
