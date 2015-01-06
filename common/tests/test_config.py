import unittest
from weathergit.common.config import Config

class ConfigTest(unittest.TestCase):
    def setUp(self):

        with open('data.conf', 'w') as file:
            file.write("""
{"maps":[{"id":"blabla","iscategorical":"0"},{"id":"blabla","iscategorical":"0"}],
"masks":{"id":"valore"},
"om_points":"value",
"parameters":{"id":"valore"}
}
            """
            )

        self.data= Config("data.conf")


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


