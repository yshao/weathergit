import time
import logging

from twisted.internet import reactor
from twisted.internet.protocol import ReconnectingClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.protocols.basic import LineReceiver

from smap.driver import SmapDriver

from weathergit.common.webcamutils import *

class TrendnetDriver(SmapDriver):
    def setup(self, opts):
        self.host = opts.get('Address')
        self.port = int(opts.get('Port', 8020))
        self.save_dir=opts.get('SaveDir')
        self.log = logging.getLogger('Trendnet')
        self.set_metadata('/', {
            'Instrument/Manufacturer' : 'Trendnet',
            'Instrument/Model' : 'WXT520' })
            



    def gotprotocol(self, p):
        # give the new listener class references to us
        p.inst = self
        p.log = self.log

    def start(self):
        self.factory = ReconnectingClientFactory()
        self.factory.protocol = VaisalaDriver.VaisalaListener
        self.point = TCP4ClientEndpoint(reactor, self.host, self.port)
        d = self.point.connect(self.factory)
        d.addCallback(self.gotprotocol)