import httplib
import urllib
import urllib2

c = httplib.HTTPConnection('www.python.org')
c.request('GET', '/', headers={'Connection': 'close'})
original_sock = c.sock
content = c.getresponse().read()
c.request('GET', '/about/')
c.sock is original_sock


request = urllib2.Request('http://www.twitter.com')
info = urllib2.urlopen(request)
print request.redirect_dict


data = urllib.urlencode({'inputstring': 'Phoenix, AZ'})
info = urllib2.urlopen('http://forecast.weather.gov/zipcity.php', data)
content = info.read()
open('phoenix.html', 'w').write(content)


# nonexistent_url = 'http://example.com/better-living-through-http'
# response = opener.open(nonexistent_url)
# print response

#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 9 - verbose_handler.py
# HTTP request handler for urllib2 that prints requests and responses.
import StringIO, httplib, urllib2
class VerboseHTTPResponse(httplib.HTTPResponse):
 def _read_status(self):
  s = self.fp.read()
  print '-' * 20, 'Response', '-' * 20
  print s.split('\r\n\r\n')[0]
  self.fp = StringIO.StringIO(s)
  return httplib.HTTPResponse._read_status(self)
class VerboseHTTPConnection(httplib.HTTPConnection):
 response_class = VerboseHTTPResponse
 def send(self, s):
  print '-' * 50
  print s.strip()
  httplib.HTTPConnection.send(self, s)
class VerboseHTTPHandler(urllib2.HTTPHandler):
 def http_open(self, req):
  return self.do_open(VerboseHTTPConnection, req)
