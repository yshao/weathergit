import os
import time
import logging

from smap.util import periodicSequentialCall
from smap.driver import SmapDriver

from hd264utils import get_snapshot
from common.utils import get_timestamp


class TrendnetDriver(SmapDriver):
    path = '/trendnet0/time'

    def setup(self, opts):
        self.host = opts.get('Address')
        self.port = int(opts.get('Port', 8020))
        self.save_dir=opts.get('SaveDir')
        self.log = logging.getLogger('Trendnet')
        self.set_metadata('/', {
            'Instrument/Manufacturer' : 'Trendnet',
            'Instrument/Model' : 'WXT520' })


        # self.conn = DbConn()

        ### create timeseries
        if not self.inst.lookup(self.path):
            self.add_timeseries(self.path, '', data_type="double",timezone=self.tz)

    def poll_snapshot(self):

        imagepath=get_snapshot(self.save_dir)
        imageidx=os.path.basename(imagepath)
        self.conn.insert(imageidx)

        self.inst.add(self.path, imageidx)

    def poll_timestamp(self):
        timeidx=get_timestamp()
        self.instd.add(self.path,timeidx)


    def start(self):
        # self.factory = ReconnectingClientFactory()
        # # self.factory.protocol = VaisalaDriver.VaisalaListener
        # self.point = TCP4ClientEndpoint(reactor, self.host, self.port)
        # d = self.point.connect(self.factory)
        # d.addCallback(self.gotprotocol)

        periodicSequentialCall(self.poll_timestamp).start(self.rate)