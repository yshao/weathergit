import json
import unittest

str={'status': {'current_filestamp':'','brightness_temp':'','receiver_temp':''}}


jo=json.dumps(str)


str={'chamber_temp':'','chamber_pressure':'','battery_level':'','disk':''}



class GetStatusTest(unittest.TestCase):
    def setUp(self):
        """"""

    def testCheckReturns(self):
        assert False

