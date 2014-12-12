import re
import unittest
from common.config import Config
from common.sourceclient import SourceClient


class SMAPConnectionTest(unittest.TestCase):
    def setUp(self):
        self.config=Config("../../common/weatherplotter.conf")


    def testConnect(self):
        login=dict(hostname=self.config['smap_source_host'], key_filename="../"+self.config['smap_source_keyfile'],
                   username=self.config['smap_source_user'],password=self.config['smap_source_password'])

        self.c=SourceClient(login)

        assert self.c.connected == True

    def testSendCmd(self):
        login=dict(hostname=self.config['smap_source_host'], key_filename="../"+self.config['smap_source_keyfile'],
                   username=self.config['smap_source_user'],password=self.config['smap_source_password'])

        self.c=SourceClient(login)

        print self.c.send_cmd("CMD_DATE")
        assert len("\n".join(self.c.send_cmd("CMD_DATE"))) > 0

    def testCmdDISKSPACE(self):
        login=dict(hostname=self.config['smap_source_host'], key_filename="../"+self.config['smap_source_keyfile'],
                   username=self.config['smap_source_user'],password=self.config['smap_source_password'])

        self.c=SourceClient(login)

        ln=self.c.send_cmd("CMD_DISKSPACE")[0]
        a=re.split(' +',ln)
        ln=dict(filesystem=a[0],size=a[1],used=a[2],avail=a[3],use_percent=a[4],mounted_on=a[5])
        self.assertRegexpMatches(ln['used'],r'([0-9]|\.)*G')

