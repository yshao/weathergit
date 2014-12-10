import unittest
from common.config import Config
from common.dataclient import DataClient


class TestDataClient(unittest.TestCase):
    def setUp(self):
        config= Config("../weatherplotter.conf")
        login={}
        login['host']=config['smap_server_host']
        login['port']=config["smap_server_port"]

        self.d=DataClient(login)

    # def testGetData(self):
    #     self.d.get_data()




