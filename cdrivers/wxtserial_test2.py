#!/usr/bin/env python

# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

"""
Example using MouseMan protocol with the SerialPort transport.
"""

import sys
from twisted.python import usage, log

if sys.platform == 'win32':
    # win32 serial does not work yet!
    # raise NotImplementedError, "The SerialPort transport does not currently support Win32"
    from twisted.internet import win32eventreactor
    win32eventreactor.install()

class Options(usage.Options):
    optParameters = [
        ['port', 'p', '/dev/ttyO2', 'Device for serial mouse'],
        ['baudrate', 'b', '19200', 'Baudrate for serial mouse'],
        ['outfile', 'o', None, 'Logfile [default: sys.stdout]'],
    ]

from twisted.internet import protocol
from twisted.protocols.basic import LineReceiver

class McFooMouse(protocol.Protocol):
    # def down_left(self):
    #     log.msg("LEFT")
    #
    # def up_left(self):
    #     log.msg("left")
    #
    # def down_middle(self):
    #     log.msg("MIDDLE")
    #
    # def up_middle(self):
    #     log.msg("middle")
    #
    # def down_right(self):
    #     log.msg("RIGHT")
    #
    # def up_right(self):
    #     log.msg("right")
    #
    # def move(self, x, y):
    #     log.msg("(%d,%d)" % (x, y))

    def dataReceived(self, data):
        print data
        # for c in data:
        #     byte = ord(c)
        #     # self.state = getattr(self, 'state_'+self.state)(byte)
        #     print byte

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


import time

class VaisalaListener(LineReceiver):
    def lineReceived(self, line):
        # self.log.debug("Read: " + line)
        print line
        try:
            self.process(line)
        except Exception, e:
            print str(e)
            # self.log.error("Error in update: " + str(e))

    def process(self, line):
        fields = line.split(',')
        reg = fields[0][1:]

        # print reg
        # print 'REG'

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
                # self.inst.add(path, ts, val_)

                # print unit
                # print path
                # print k
                # print v
                # print "Debug"

            # print data




if __name__ == '__main__':
    from twisted.internet import reactor
    from twisted.internet.serialport import SerialPort
    o = Options()
    try:
        o.parseOptions()
    except usage.UsageError, errortext:
        print "%s: %s" % (sys.argv[0], errortext)
        print "%s: Try --help for usage details." % (sys.argv[0])
        raise SystemExit, 1

    logFile = sys.stdout
    if o.opts['outfile']:
        logFile = o.opts['outfile']
    log.startLogging(logFile)

    port=o.opts['port']
    baudrate=int(o.opts['baudrate'])

    SerialPort(VaisalaListener(), port, reactor, baudrate=baudrate)
    reactor.run()