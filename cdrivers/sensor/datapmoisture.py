import unittest
import numpy as np

from common.dataclient import DataClient




class Test_DataClient(unittest.TestCase):
    def setUp(self):
        ""
        self.dc=DataClient()


    def test_get_data(self):
        data=np.narray(self.dc.get_data())
        assert data.shape[0] == 100
        assert data.shape[1] == 2

    def test_load_csv(self):
        assert data

class Test_SmapUtil(unittest.TestCase):
    def setUp(self):
        self.s=SmapUtil()
        if s.load_csv(data):



    def
        assert