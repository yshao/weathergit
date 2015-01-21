import unittest
from gui.handlers.datawidgethandler import datawidgetHandler

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '1/21/2015' '10:07 AM'

class test_handler(unittest.TestCase,datawidgetHandler):
    ""
    def setUp(self):
        ""
        self.data={
            'start_time':1,
            'end_time':2,
            'stream_limit':1,
            'paths':['/garmin0/altitude']
        }
        # win=DataWidget()


    def test_on_download_data(self):
        self.assertEquals("select data 1 2 streamlimit 1 where path like '/garmin0/altitude'",self.on_download_data(self.data))