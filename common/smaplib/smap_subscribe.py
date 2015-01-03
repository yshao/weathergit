#!/usr/bin/python
"""
Copyright (c) 2013 Regents of the University of California
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions 
are met:

 - Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
 - Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the
   distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS 
FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL 
THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, 
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) 
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, 
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED 
OF THE POSSIBILITY OF SUCH DAMAGE.
"""

"""
@author Stephen Dawson-Haggerty <stevedh@eecs.berkeley.edu>
"""

import sys
import time
import urlparse
import urllib
import optparse
import uuid
import json

from twisted.internet import reactor, defer, task
from twisted.python import util

from smap import util
from smap.contrib import dtutil
from smap.archiver import settings
from smap.archiver import client

usage = 'usage: %prog [options] querys ...'
parser = optparse.OptionParser(usage=usage)
parser.add_option('-u', '--archiver-url', dest='url',
                  default=settings.conf['default backend'],
                  help="sMAP archiver URL")
parser.add_option('-t', '--time-format', dest='timefmt',
                  default=None,
                  help="output time format string")
parser.add_option('-z', '--time-zone', dest='timezone',
                  default='Local',
                  help="output time zone string (Olson tzinfo)")
parser.add_option('-a', '--all', dest='all',
                  default=False, action="store_true",
                  help="output all data, not just the last reading")
parser.add_option('-c', '--count', dest='count',
                  default=False, action="store_true",
                  help="count distinct streams")
# TODO : add support for private streams
parser.add_option('-k', '--key', dest='key', default='',
                  help='api keys: k1[,k2 ...]')
parser.add_option('-p', '--private', dest='private', default=False,
                  help='display only results associated with the api key',
                  action='store_true')
parser.add_option('-w', '--websocket', dest='websocket', default=False,
                  help='subscribe using a websocket rather than the HTTP interface',
                  action='store_true')

if __name__ == '__main__':
    opts, args = parser.parse_args()
    start, uniq, count = time.time(), set([]), 0

    if opts.timezone == 'Local':
        tz = dtutil.tzlocal()
    else:
        tz = dtutil.gettz(opts.timezone)

    def build_restrict(args):
        clauses = []
        for a in args:
            try:
                uuid.UUID(a)
                clauses.append('uuid = "%s"' % a)
            except:
                clauses.append(a)
        return ' or '.join(clauses)

    def websocket_url(opts):
        netloc = urlparse.urlparse(opts.url).netloc
        params = urllib.urlencode(client.make_qdict(opts.key, opts.private), 
                                  doseq=True)
        return "ws://" + netloc + "/wsrepublish?" + params

    def websocket_loop(opts):
        # blocking version
        import websocket
        url = websocket_url(opts)
        print "WebSocket URL:", url
        ws = websocket.create_connection(url)
        ws.send(restrict if restrict else "has uuid")

        while True:
            try:
                result = ws.recv()
            except KeyboardInterrupt:
                print_final_stats()
                break

            try:
                val = json.loads(result)
            except ValueError:
                sys.stderr.write("WARNING: WebSocket: invalid frame received\n")
                continue

            # SDH : perhaps not the most clear way of doing this..
            print_data(*zip(*[(v['uuid'], v['Readings']) 
                              for v in val.itervalues()
                              if 'uuid' in v and 'Readings' in v]))

    def print_data(uuids, data):
        global uniq
        global count
        """Format and print the readings we just got from the archiver"""
        for u, vals in zip(uuids, data):
            uniq.add(u)
            count += len(vals)
            if opts.count:
                continue

            if not opts.all: vals = [vals[-1]]
            for latest in vals:
                ts = dtutil.ts2dt(latest[0] / 1000)
                print u,
                if opts.timefmt:
                    print dtutil.strftime_tz(ts, opts.timefmt, tzstr=opts.timezone),
                else:
                    print dtutil.strftime_tz(ts, tzstr=opts.timezone),
                print latest[1]

    @defer.inlineCallbacks
    def error(resp):
        d = defer.Deferred()
        resp.deliverBody(util.BufferProtocol(d))
        err = yield d
        print >>sys.stderr, "Error subscribing to channel, aborting"
        print >>sys.stderr, ''
        print >>sys.stderr, err
        reactor.stop()

    def print_counts():
        global uniq
        global count
        sys.stderr.write("%i\t%i\r" % (len(uniq), count))
        sys.stderr.flush()

    def print_final_stats():
        global uniq
        global count
        sys.stderr.write("\n%i\t%i\t%02fs\t%.02f/s\n" % (len(uniq),
                                                         count, 
                                                         (time.time() - start),
                                                         count / (time.time() - start)))

    if opts.count:
        task.LoopingCall(print_counts).start(1)
    reactor.addSystemEventTrigger("after", "shutdown", print_final_stats)

    restrict = build_restrict(args)
    if opts.websocket:
        websocket_loop(opts)
    else:
        rpc = client.RepublishClient(opts.url, print_data, 
                                     restrict=restrict,
                                     connect_error=error, 
                                     key=opts.key.split(','),
                                     private=opts.private)
        rpc.connect()
        reactor.run()

