import sys
import socket
import time
import logging
import re

from twisted.internet import reactor
from twisted.internet.protocol import ReconnectingClientFactory
from twisted.internet.endpoints import SerialPortEndpoint

from twisted.protocols.basic import LineReceiver

from smap.driver import SmapDriver

# VAISALA_UNITS = {
#     'R1' : {
#       'D' : 'deg',
#       'M' : 'm/s',
#       },
#     'R2' : {
#       'C' : 'C',
#       'P' : 'rh',
#       'H' : 'Pa',
#       },
#     'R3' : {
#       'M' : 'mm',
#       's' : 'second',
#       },
#     'R5' : {
#       'V' : 'V',
#       'C' : 'C',
#       '#' : '#',
#
#     }
#     }
#
# VAISALA_POINTS = {
#     'R1' : (
#        'wind', {
#          'direction' : ('Dm', 'Dn', 'Dx'),
#          'speed' : ('Sm', 'Sn', 'Sx')
#          }
#        ),
#     'R2' : (
#        'pth', {
#          'temperature' : ('Ta', None, None),
#          'rh' : ('Ua', None, None),
#          'pressure' : ('Pa', None, None),
#          }
#        ),
#     'R3' : (
#        'precipitation', {
#           'rain_accumulation' : ('Rc', None, None),
#           'rain_duration' : ('Rd', None, None),
#           'rain_intensity' : ('Ri', None, 'Rp'),
#           'hail_accumulation' : ('Hc', None, None),
#           'hail_duration' : ('Hd', None, None),
#           'hail_intensity' : ('Hi', None, 'Hp')
#           }
#        ),
#
#     'R5': (
#         'status',{
#             'temp' : ('Th',None,None),
#             'voltage' : ('Vh','Vs','Vr'),
#
#
#         }
#
#     )
#     }


GARMIN_UNTS={
            'utc':'',
            'longitude':'deg E',
            'latitude':'deg N',
            'altitude':'mm',
            'geoid':'M',
            'fix':'',
            'speed':'M',
            'tracking_angle':'M',
            'magnetic_variation':'',


}

from nmea import NMEAReceiver as GPSProtocolBase
from twisted.python import log, usage

class GPSFixLogger:
    def handle_fix(self, *args):
      """
      handle_fix gets called whenever either rockwell.Zodiac or nmea.NMEAReceiver
      receives and decodes fix data.  Generally, GPS receivers will report a
      fix at 1hz. Implementing only this method is sufficient for most purposes
      unless tracking of ground speed, course, utc date, or detailed satellite
      information is necessary.

      For example, plotting a map from MapQuest or a similar service only
      requires longitude and latitude.
      """
      log.msg('fix:\n' +
      '\n'.join(map(lambda n: '  %s = %s' % tuple(n), zip(('utc', 'lon', 'lat', 'fix', 'sat', 'hdp', 'alt', 'geo', 'dgp'), map(repr, args)))))


    def handle_positiontime(self, *args):
        """"""
        log.msg('positiontime:\n' +
        '\n'.join(map(lambda n: '  %s = %s' % tuple(n), zip(('lat', 'lon', 'spd', 'cor', 'utc', 'utcd', 'mag'), map(repr, args)))))


    def handle_activesatellites(self,*args):
        """"""
        log.msg('activesatellites:\n' +
        '\n'.join(map(lambda n: '  %s = %s' % tuple(n), zip(('satlist', 'mode', 'pdop', 'hdop', 'vdop'), map(repr, args)))))

class GarminSerial(SmapDriver):
    class GarminSerialListener(GPSProtocolBase):
        def handle_fix(self, *args):
            """"""
            # log.msg('fix:\n' +
            # '\n'.join(map(lambda n: '  %s = %s' % tuple(n), zip(('utc', 'lon', 'lat', 'fix', 'sat', 'hdp', 'alt', 'geo', 'dgp'), map(repr, args)))))
            na=dict(zip(('utc', 'lon', 'lat', 'fix', 'sat', 'hdp', 'alt', 'geo', 'dgp'), map(repr, args)))

            data={}
            data['utc']=na['utc']
            data['longitude']=na['lon']
            data['latitude']=na['lat']
            data['altitude']=na['alt']
            data['geoid']=na['geo']
            data['fix']=na['fix']


            self.upload(data,'gga')


        def handle_positiontime(self, *args):
            """"""
            na=dict(zip(('lat', 'lon', 'spd', 'cor', 'utc', 'utcd', 'mag'), map(repr, args)))


            data={}
            data['speed']=na['spd']
            # data['tacking_angle']=na['cor']
            data['magnetic_variation']=na['mag']


            self.upload(data,'rmc')


        # def handle_activesatellites(self,*args):
        #     """"""
        #     # log.msg('activesatellites:\n' +
        #     #  '\n'.join(map(lambda n: '  %s = %s' % tuple(n), zip(('satlist', 'mode', 'pdop', 'hdop', 'vdop'), map(repr, args)))))
        #     na=dict(zip(('satlist', 'mode', 'pdop', 'hdop', 'vdop'), map(repr, args)))
        #     print na
        #     # print "AA"
        #     # print args
        #     # args=dict((y, x) for x, y in args)
        #     data={}
        #     data['pdop']=na['pdop']
        #     data['hdop']=na['hdop']
        #     data['vdop']=na['vdop']


            # self.upload(data,'na')


        def upload(self,data,reg):
            for k,v in data.iteritems():
                ts = int(time.time())
                num=re.findall(r"[-+]?\d*\.\d+|\d+", v)
                # print num
                val = float(num[0])
                path = 'garmin0/'+k
                unit = GARMIN_UNTS[k]

                if not self.inst.lookup(path):
                    self.inst.add_timeseries(path, unit, data_type='double')

                self.inst.add(path,ts,val)

    def setup(self, opts):
        self.port = opts.get('Port')
        self.log = logging.getLogger('GarminReader')
        self.set_metadata('/', {
            'Extra/Driver' : 'garmin.GarminSerial',
            'Instrument/Manufacturer' : 'Garmin',
            'Instrument/Model' : '18xLVC' })


        self.serialPort=opts.get('SerialPort')
        self.baud=int(opts.get('Baud'))
            

    def gotprotocol(self, p):
        # give the new listener class references to us
        p.inst = self
        p.log = self.log

    def start(self):

        self.factory = ReconnectingClientFactory()
        self.factory.protocol = GarminSerial.GarminSerialListener
        self.point = SerialPortEndpoint(self.serialPort,reactor,self.baud)

        d = self.point.connect(self.factory)
        d.addCallback(self.gotprotocol)

