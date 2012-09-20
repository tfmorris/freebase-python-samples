from apiclient import discovery
from apiclient import model
import json

DEVELOPER_KEY="AIzaSyABJUiXZN-2n-IWBnp29tp5WXckX7XF6bs"
model.JsonModel.alt_param = ""
freebase = discovery.build('freebase', 'v1', developerKey=DEVELOPER_KEY)

response = freebase.text(id='en/bob_dylan').execute()
print response


