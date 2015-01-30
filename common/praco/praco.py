from PyQt4.QtCore import pyqtSignal, pyqtSlot
from common.praco.pracoclient import PracoClient

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '1/27/2015' '10:59 AM'

class Praco():
    ""
    def __init__(self):
        ""
        self.pc=PracoClient()

        self.decode()


    def setup(self):
        ""


    def start(self):
        ""


    @pyqtSlot()
    def publish_imu(self):
        ""
        self.inst.add_timeseries()


    @pyqtSlot()
    def publish_enc(self):
        ""

    @pyqtSlot()
    def publish_rad(self):
        ""

    def close(self):
        ""


class Decoder(object):
    ""
    sigUpdate=pyqtSignal()
    def __init__(self):
        ""

    def update(self):
        ""

    def decode(self):
        ""

class ImuDecoder(Decoder):
    ""
    def setup(self):
        ""

    def decode(self):
        ""

class EncDecoder(Praco):
    ""
    def setup(self):
        ""

class RadDecoder(Praco):
    ""
    def setup(self):
        ""

