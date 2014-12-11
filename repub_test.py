import pycurl, json

#curl 'http://new.openbms.org/backend/api/prev/Metadata__Instrument__Manufacturer/UC%20Berkeley/Metadata__Location__Room/465/Properties__UnitofMeasure/mW?starttime=1315272705000'

#curl -XPOST -d 'Metadata/Extra/Type = "oat"' http://new.openbms.org/backend/republish

#curl -XPOST -d 'Metadata/SourceName = "BEST WeatherStation"' http://192.168.1.120:8079/api/republish

#curl -XPOST -d @data.json -H "Content-Type: application/json" http://localhost:8079/add/<KEY>

data={
  "/sensor0" : {
    "Metadata" : {
      "SourceName" : "Test Source",
      "Location" : { "City" : "Berkeley" }
    },
    "Properties": {
      "Timezone": "America/Los_Angeles",
      "UnitofMeasure": "Watt",
      "ReadingType": "double"
    },
    "Readings" : [[1351043674000, 0], [1351043675000, 1]],
    "uuid" : "d24325e6-1d7d-11e2-ad69-a7c2fa8dba61"
  }
}

#curl http://ar1.openbms.org:8079/api/query/Properties__UnitofMeasure

#curl http://192.168.1.120:8079/api/query/Properties__UnitofMeasure


github_url = 'https://api.postmarkapp.com/email'

data = json.dumps({"From": "user@example.com", "To": "receiver@example.com", "Subject": "Pycurl", "TextBody": "Some text"})

c = pycurl.Curl()
c.setopt(pycurl.URL, github_url)
c.setopt(pycurl.HTTPHEADER, ['X-Postmark-Server-Token: API_TOKEN_HERE','Accept: application/json'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, data)
c.perform()

c = pycurl.Curl()
c.setopt(c.URL, 'http://news.ycombinator.com')
c.perform()

import cStringIO

print "1"
buf = cStringIO.StringIO()

c = pycurl.Curl()
c.setopt(c.URL, 'http://news.ycombinator.com')
c.setopt(c.WRITEFUNCTION, buf.write)
c.perform()

print buf.getvalue()
buf.close()


print "2"
# buf = cStringIO.StringIO()
#
# c = pycurl.Curl()
# c.setopt(c.URL, 'http://news.ycombinator.com')
# c.setopt(c.WRITEFUNCTION, buf.write)
# c.setopt(c.CONNECTTIMEOUT, 5)
# c.setopt(c.TIMEOUT, 8)
# c.setopt(c.PROXY, 'http://inthemiddle.com:8080')
# c.perform()
#
# print buf.getvalue()
# buf.close()

print "3"

c = pycurl.Curl()
c.setopt(c.URL, 'http://myappserver.com/ses1')
c.setopt(c.CONNECTTIMEOUT, 5)
c.setopt(c.TIMEOUT, 8)
c.setopt(c.COOKIEFILE, '')
c.setopt(c.FAILONERROR, True)
c.setopt(c.HTTPHEADER, ['Accept: text/html', 'Accept-Charset: UTF-8'])
try:
    c.perform()

    c.setopt(c.URL, 'http://myappserver.com/ses2')
    c.setopt(c.POSTFIELDS, 'foo=bar&bar=foo')
    c.perform()
except pycurl.error, error:
    errno, errstr = error
    print 'An error occurred: ', errstr

print "4"
#curl -XPOST -d 'Metadata/Extra/Type = "oat"' http://new.openbms.org/backend/republish
cmd={'key':'','port':'8079','host':'new.openbms.org/backend/republish'}

c = pycurl.Curl()
c.setopt(c.URL, 'http://%(host)/republish' % cmd)
try:
    c.perform()

    c.setopt(c.POSTFIELDS, 'Metadata/Extra/Type')

except:

print "5"
cmd={'key':'','port':'8079','host':'192.168.1.120'}


c = pycurl.Curl()
c.setopt(c.URL, 'http://%(host):%(port)/add/%(key)' % cmd)
c.setopt(c.CONNECTTIMEOUT, 5)
c.setopt(c.TIMEOUT, 8)
c.setopt(c.COOKIEFILE, '')
c.setopt(c.FAILONERROR, True)
# c.setopt(c.HTTPHEADER, ['Accept: text/html', 'Accept-Charset: UTF-8'])
try:
    c.perform()

    c.setopt(c.URL, 'http://myappserver.com/ses2')
    c.setopt(c.POSTFIELDS, 'foo=bar&bar=foo')
    c.perform()
except pycurl.error, error:
    errno, errstr = error
    print 'An error occurred: ', errstr


