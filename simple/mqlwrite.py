from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run

import json
from urllib import urlencode
import httplib2
import os

CLIENT_ID = open(os.environ['HOME'] + "/.freebase_client_id").read()
CLIENT_SECRET = open(os.environ['HOME'] + "/.freebase_client_secret").read()

def authenticated_http():
  storage = Storage('freebase.dat')
  credentials = storage.get()
  if credentials is None or credentials.invalid == True:
    flow = OAuth2WebServerFlow(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        scope='https://www.googleapis.com/auth/freebase',
        user_agent='freebase-cmdline-sample/1.0',
        xoauth_displayname='Freebase Client Example App')
    credentials = run(flow, storage)
  http = httplib2.Http()
  return credentials.authorize(http)

http = authenticated_http()
query = {"create":"unconditional","id":None,"name":"Nowhere","type":"/location/location"}
data = dict(query=json.dumps(query))
headers = {
'X-HTTP-Method-Override': 'GET',
'Content-Type': 'application/x-www-form-urlencoded'
}
url = 'https://www.googleapis.com/freebase/v1sandbox/mqlwrite' + '?' + urlencode(data)
resp, content = http.request(url, "GET", headers=headers)  
print content

