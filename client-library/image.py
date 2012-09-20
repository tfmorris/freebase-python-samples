from apiclient import discovery
from apiclient import model

import json
import Image

DEVELOPER_KEY="AIzaSyABJUiXZN-2n-IWBnp29tp5WXckX7XF6bs"

def main():
  model.JsonModel.alt_param = ""
  freebase = discovery.build('freebase', 'v1sandbox', developerKey=DEVELOPER_KEY)

  response = freebase.image(id='/en/espresso').execute()
  im = Image.open(response)
  im.save('image.jpg', "JPEG")
