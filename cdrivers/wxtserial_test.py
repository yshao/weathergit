#!/usr/bin/env python

# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

"""
Example using MouseMan protocol with the SerialPort transport.
"""

# TODO set tty modes, etc.
# This works for me:

# speed 1200 baud; rows 0; columns 0; line = 0;
# intr = ^C; quit = ^\; erase = ^?; kill = ^U; eof = ^D;
# eol = <undef>; eol2 = <undef>; start = ^Q; stop = ^S; susp = ^Z;
# rprnt = ^R; werase = ^W; lnext = ^V; flush = ^O; min = 1; time = 0;
# -parenb -parodd cs7 hupcl -cstopb cread clocal -crtscts ignbrk
# -brkint ignpar -parmrk -inpck -istrip -inlcr -igncr -icrnl -ixon
# -ixoff -iuclc -ixany -imaxbel -opost -olcuc -ocrnl -onlcr -onocr
# -onlret -ofill -ofdel nl0 cr0 tab0 bs0 vt0 ff0 -isig -icanon -iexten
# -echo -echoe -echok -echonl -noflsh -xcase -tostop -echoprt -echoctl
# -echoke

import sys
from twisted.python import usage, log
from twisted.protocols.mice import mouseman

if sys.platform == 'win32':
    # win32 serial does not work yet!
    # raise NotImplementedError, "The SerialPort transport does not currently support Win32"
    from twisted.internet import win32eventreactor
    win32eventreactor.install()

class Options(usage.Options):
    optParameters = [
        ['port', 'p', '/dev/ttyO2', 'Device for serial mouse'],
        ['baudrate', 'b', '115200', 'Baudrate for serial mouse'],
        ['outfile', 'o', None, 'Logfile [default: sys.stdout]'],
    ]

class McFooMouse(mouseman.MouseMan):
    def down_left(self):
        log.msg("LEFT")

    def up_left(self):
        log.msg("left")

    def down_middle(self):
        log.msg("MIDDLE")

    def up_middle(self):
        log.msg("middle")

    def down_right(self):
        log.msg("RIGHT")

    def up_right(self):
        log.msg("right")

    def move(self, x, y):
        log.msg("(%d,%d)" % (x, y))

import sys
import socket
import time
import logging

from twisted.internet import reactor
from twisted.internet.protocol import ReconnectingClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.protocols.basic import LineReceiver


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
       )
    }



class VaisalaSerialDriver(protocol.):
    class VaisalaListener(LineReceiver):
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
        # self.port = opts.get('Port')
        # self.host = opts.get('Address')
        # self.port = int(opts.get('Port', 4660))
        self.log = logging.getLogger('VaisalaReader')
        self.set_metadata('/', {
            'Extra/Driver' : 'smap.drivers.vaisala.VaisalaSerialDriver',
            'Instrument/Manufacturer' : 'Vaisala',
            'Instrument/Model' : 'WXT520' })


    def gotprotocol(self, p):
        # give the new listener class references to us
        p.inst = self
        p.log = self.log

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
    
    SerialPort(VaisalaSerialDriver(), o.opts['port'], reactor, baudrate=int(o.opts['baudrate']))
    reactor.run()