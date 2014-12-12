from common.sourceclient import SourceClient
from gui.tasks.taskutils import *

import unittest
from common.config import Config
from common.dbconn import DbConn


class SMAPConnectionTest(unittest.TestCase):
    def setUp(self):
        self.config=Config("../../common/weatherplotter.conf")

    def test_SMAPSource(self):
        ip=self.config["smap_source_host"]
        assert testConnection(ip) == True

    def test_SMAPServer(self):
        # print

        ip=self.config["smap_server_host"]
        # print ip
        assert testConnection(ip) == True

    def test_SMAPServerPostgreMeta(self):
        login={}
        login['host']=self.config["smap_server_host"]
        login['port']=self.config["smap_server_db_port"]
        login['dbname']=self.config["dbname"]
        login['user']=self.config["user"]
        login['password']=self.config["password"]
        db=DbConn(login)
        assert db.connected == True

    def test_SMAPSourceSSHClient(self):
        login=dict(hostname=self.config['smap_source_host'], key_filename="../../common/"+self.config['smap_source_keyfile'],
                   username=self.config['smap_source_user'],password=self.config['smap_source_password'])

        conn=SourceClient(login)
        assert conn.connected == True