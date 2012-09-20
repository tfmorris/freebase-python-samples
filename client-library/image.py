from apiclient import discovery
from apiclient import model

import json
import Image
import os

api_key = open(os.environ['HOME'] + "/.freebase_api_key").read()

model.JsonModel.alt_param = ""
freebase = discovery.build('freebase', 'v1sandbox', developerKey=api_key)

response = freebase.image(id='/en/espresso').execute()
im = Image.open(response)
im.save('image.jpg', "JPEG")
