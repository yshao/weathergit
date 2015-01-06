import unittest
from requests.packages.urllib3 import request
from response import Response

class HTTPResponse(Response):
    def __init__(self):
        super(__init__())

class test_HTTPResponse(unittest.TestCase):
    url='www.google.com'

    def setUp(self):
        self.resp=HTTPResponse()


    def test_urlget(self):
        ""
        url='www.google.com'
        r=request.GET(self.url)
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.reason,'OK')

    def test_urlpost(self):
        r=request.POST(self.url)

