import json
from pprint import pprint


class Config(object):
    def __init__(self,path):
        self.fhandle=open(path)
        self.data = json.load(self.fhandle)


    def close(self):
        self.fhandle.close()

    def __str__(self):
        return str(pprint(self.data))

    def __getitem__(self, item):
        return self.data[item]


import unittest

class ConfigTest(unittest.TestCase):
    def setUp(self):
        self.data=Config("data.conf")

    def testGet(self):
        assert self.data["maps"][0]["id"] == "blabla"
        assert self.data["masks"]["id"] == "valore"
        assert self.data["om_points"] == "value"

 #    def testPrint(self):
 #        assert self.__str__() == """{u'maps': [{u'id': u'blabla', u'iscategorical': u'0'},
 #           {u'id': u'blabla', u'iscategorical': u'0'}],
 # u'masks': {u'id': u'valore'},
 # u'om_points': u'value',
 # u'parameters': {u'id': u'valore'}}"""


