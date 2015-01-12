import sys
import socket
import time
import logging

from twisted.internet import reactor
from twisted.internet.serialport import SerialPort
from twisted.internet.protocol import ReconnectingClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet.endpoints import SerialPortEndpoint

from twisted.protocols.basic import LineReceiver

from smap.driver import SmapDriver

from weathergit.common.schema import *

from twisted.internet import reactor


class PracoSource(SmapDriver):
    class VaisalaSerialListener(LineReceiver):
        def lineReceived(self, line):
            self.log.debug("Read: " + line)
            try:
                self.process(line)
            except Exception, e:
                self.log.error("Error in update: " + str(e))

        def process(self, line):

            decoder=decoderTask()

            data=decoder.decode()

            def proc_data(data):


            fields = line.split(',')
            reg = fields[0][1:]
            def proc_field(f):
                v = f.split('=')
                return (v[0], (v[1][:-1], v[1][-1]))
            data = dict(map(proc_field, fields[1:]))

            if VAISALA_POINTS.has_key(reg):
                ts = int(time.time())
                point = VAISALA_POINTS[reg][0]
                # create the point in the smap tree if necessary
                for k,v in VAISALA_POINTS[reg][1].iteritems():
                    unit = VAISALA_UNITS[reg][data[v[0]][1]]
                    path = '/%s/%s' % (point, k)
                    if not self.inst.lookup(path):
                        self.inst.add_timeseries(path, unit, data_type='double',timezone=self.tz)

                    val_ = float(data.get(v[0])[0])
                    min_ = data.get(v[1], None)
                    if min_ != None: min_ = min_[0]
                    max_ = data.get(v[2], None)
                    if max_ != None: max_ = max_[0]
                    self.inst.add(path, ts, val_)


    def setup(self, opts):
        self.tz = opts.get('Timezone')
        self.port = opts.get('Port')
        self.log = logging.getLogger('PracoSource')
        self.set_metadata('/', {
            'Extra/Driver' : 'smap.drivers.praco.PracoSource',
            'Instrument/Manufacturer' : 'BEST',
            'Instrument/Model' : 'v1' })

        self.raw_path=opts.get('')



    def gotprotocol(self, p):
        # give the new listener class references to us
        p.inst = self
        p.log = self.log


    def start(self):
        # SDH : this is supposed to reconnect us automatically when
        # the socket dies.  I haven't tried it, though.
        self.factory = ReconnectingClientFactory()
        # self.factory.protocol = VaisalaSerial.VaisalaSerialListener
        self.point = TCP4ClientEndpoint(reactor, self.host, self.port)
        # self.point = SerialPortEndpoint(self.serialPort,reactor,self.baud)


        d = self.point.connect(self.factory)
        d.addCallback(self.gotprotocol)





