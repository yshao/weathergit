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

VAISALA_UNITS = {
    'R1' : {
      'D' : 'deg',
      'M' : 'm/s',
      },
    'R2' : {
      'C' : 'C',
      'P' : 'rh',
      'H' : 'Pa',
      },
    'R3' : {
      'M' : 'mm',
      's' : 'second',
      },
    'R5' : {
      'V' : 'V',
      'C' : 'C',
      '#' : '#',

    }
    }

VAISALA_POINTS = {
    'R1' : (
       'wind', {
         'direction' : ('Dm', 'Dn', 'Dx'),
         'speed' : ('Sm', 'Sn', 'Sx')
         }
       ),
    'R2' : (
       'pth', {
         'temperature' : ('Ta', None, None),
         'rh' : ('Ua', None, None),
         'pressure' : ('Pa', None, None),
         }
       ),
    'R3' : (
       'precipitation', {
          'rain_accumulation' : ('Rc', None, None),
          'rain_duration' : ('Rd', None, None),
          'rain_intensity' : ('Ri', None, 'Rp'),
          'hail_accumulation' : ('Hc', None, None),
          'hail_duration' : ('Hd', None, None),
          'hail_intensity' : ('Hi', None, 'Hp')
          }
       ),

    'R5': (
        'status',{
            'temp' : ('Th',None,None),
            'voltage' : ('Vh','Vs','Vr'),


        }

    )
    }


from twisted.internet import reactor
from twisted.internet.serialport import SerialPort


# port=o.opts['port']
# baudrate=int(o.opts['baudrate'])
#
# SerialPort(VaisalaListener(), port, reactor, baudrate=baudrate)
# reactor.run()

class VaisalaSerial(SmapDriver):
    class VaisalaSerialListener(LineReceiver):
        def lineReceived(self, line):
            self.log.debug("Read: " + line)
            try:
                self.process(line)
            except Exception, e:
                self.log.error("Error in update: " + str(e))

        def process(self, line):
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
                        self.inst.add_timeseries(path, unit, data_type='double')

                    val_ = float(data.get(v[0])[0])
                    min_ = data.get(v[1], None)
                    if min_ != None: min_ = min_[0]
                    max_ = data.get(v[2], None)
                    if max_ != None: max_ = max_[0]
                    self.inst.add(path, ts, val_)


    def setup(self, opts):
        # self.host = opts.get('Address')
        # self.port = int(opts.get('Port', 4660))
        self.port = opts.get('Port')
        self.log = logging.getLogger('VaisalaSerial')
        self.set_metadata('/', {
            'Extra/Driver' : 'smap.drivers.vaisalaserial.VaisalaSerial',
            'Instrument/Manufacturer' : 'Vaisala',
            'Instrument/Model' : 'WXT520' })


        self.serialPort=opts.get('SerialPort')
        self.baud=int(opts.get('Baud'))
            

    def gotprotocol(self, p):
        # give the new listener class references to us
        p.inst = self
        p.log = self.log

    def start(self):
        # SDH : this is supposed to reconnect us automatically when
        # the socket dies.  I haven't tried it, though.
        self.factory = ReconnectingClientFactory()
        self.factory.protocol = VaisalaSerial.VaisalaSerialListener
        # self.point = TCP4ClientEndpoint(reactor, self.host, self.port)
        self.point = SerialPortEndpoint(self.serialPort,reactor,self.baud)


        d = self.point.connect(self.factory)
        d.addCallback(self.gotprotocol)





