import json
import MimeWriter
import mimetools
import urllib
import urllib2
import StringIO
import os

api_key = open(os.environ['HOME'] + "/.freebase_api_key").read()
service_url = 'https://www.googleapis.com/freebase/v1/mqlread'

def write_query_request(writer, query_name, query, service_url, api_key):
	params = {
		'query': json.dumps(query),
		'key': api_key
	}
	txtin = StringIO.StringIO("GET " + service_url + '?' + urllib.urlencode(params) + "\n")
	subpart = writer.nextpart()
	subpart.addheader("Content-Transfer-Encoding", "binary")
	subpart.addheader("Content-ID", "<" + query_name + ">")
	pout = subpart.startbody("application/http")
	mimetools.encode(txtin, pout, '8bit')
	txtin.close()

query1 = [{'id': None, 'name': None, 'type': '/astronomy/planet'}]
query2 = [{'id': None, 'name': None, 'type': '/location/country'}]


out = StringIO.StringIO()
writer = MimeWriter.MimeWriter(out)
boundary = "batch_boundary"
writer.startmultipartbody("mixed", boundary)
writer.flushheaders()

write_query_request(writer, "q1", query1, service_url, api_key)
write_query_request(writer, "q2", query2, service_url, api_key)

writer.lastpart()
msg = out.getvalue()
msg = "\n".join(msg.split("\n")[4:])
out.close()
print msg

headers = {
	'Content-Type': 'multipart/mixed; boundary=' + boundary
}

request = urllib2.Request("https://www.googleapis.com/batch", msg, headers)

response = urllib2.urlopen(request).read()
print response
