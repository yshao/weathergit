from urlparse import urlparse

p = urlparse('http://example.com:8080/Nord%2FLB/logo?shape=square&dpi=96')



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

# from verbose_http import VerboseHTTPHandler
import urllib, urllib2
opener = urllib2.build_opener(VerboseHTTPHandler)
info=opener.open('http://www.ietf.org/rfc/rfc2616.txt')

print info.code

print info.msg


print info.read().strip()


nonexistent_url = 'http://example.com/better-living-through-http'
response = opener.open(nonexistent_url)

try:
 response = opener.open(nonexistent_url)
except urllib2.HTTPError, e:
 print e.code
 print e.msg
 print e.readline()
 pass


request = urllib2.Request('http://www.twitter.com')
info = urllib2.urlopen(request)
print request.redirect_dict
# {'http://twitter.com/': 1}