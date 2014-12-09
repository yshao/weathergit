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
        ['port', 'p', 'COM4', 'Device for serial mouse'],
        ['baudrate', 'b', '19200', 'Baudrate for serial mouse'],
        ['outfile', 'o', None, 'Logfile [default: sys.stdout]'],
    ]

from twisted.internet import protocol
from twisted.protocols.basic import LineReceiver

class McFooMouse(protocol.Protocol):
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

    def dataReceived(self, data):
        print data
        # for c in data:
        #     byte = ord(c)
        #     # self.state = getattr(self, 'state_'+self.state)(byte)
        #     print byte

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
    
    SerialPort(McFooMouse(), o.opts['port'], reactor, baudrate=int(o.opts['baudrate']))
    reactor.run()