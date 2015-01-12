import unittest
from weathergit.common.smaputils import SmapUtils
from weathergit.common.env import Env


class MonitException(Exception):
    ""


class SmapRequestException(Exception):
    ""



sn=SmapNet()
sc=SmapUtils()

if sc.test_live(Env['port_monit'],''):
    ""

else:
    raise MonitException()



class SmapNet(object):
    def __init__(self):
        ""

    def iperf(self):
        ""
        return msg

    def multiping(self):
        targets=['192.168.1.223']

    def scan_camera(self):
        return ['192.168.1.121']


    def scan_network(self):
        return True

    def multipoll(self):




### NodeChecker ###

class Test_SmapNet(unittest.TestCase):
    n=SmapNet()

    def setUp(self):
        ""


    def test_scan_camera(self):
        # self.assertEqual()

        self.assertListEqual(self.n.multiping(),['192.168.1.121'])

    def test_iperf(self):
        ""

    def test_scan_network(self):

        assert self.n.scan_network() == True
