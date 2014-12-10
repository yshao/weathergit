import unittest
from common.config import Config
from common.dbconn import DbConn


class UUIDTest(unittest.TestCase):
    def setUp(self):
        config=Config("../weatherplotter.conf")
        # print config
        # print config['om_points']
        login={}
        login['dbname']=config['dbname']
        login['user']=config["user"]
        login['password']=config['password']
        login['host']=config['host']
        # print login
        self.conn=DbConn(login)

    # def testConnect(self):
    #     assert self.data["maps"][0]["id"] == "blabla"
    #     assert self.data["masks"]["id"] == "valore"
    #     assert self.data["om_points"] == "value"

    def test_SelectUUID(self):
        """"""
        uuid=self.conn.get_uuid()
        assert uuid["0049d709-eb70-50b5-8349-859ab8b9c9f8"]["Path"] == "/KCABERKE25/dew_point"

    def testInsert(self):
        """"""
        assert True