import sys
import socket
import time
import logging

from twisted.internet import reactor
from twisted.internet.protocol import ReconnectingClientFactory
from twisted.internet.endpoints import SerialPortEndpoint

from twisted.protocols.basic import LineReceiver

from smaputil.driver import SmapDriver

GARMIN_POINTS = {
    'gga' : {
        'utc':'utc',
        'lon':'longitude',
        'lat':'latitude',
        'fix':'fix_type',
        'sat':'num_satellites',
        'hdp':6,
        'alt':'altitude',
        'geo':'geodetical',
        'dgp':9,
    },
    'rmc' : {
        'lat':'latitude',
        'lon':'longitude',
        'spd':'speed',
        'cor':4,
        'utc':'utc',
        'utcd':'utc date',
        'mag':'magvar'


    },


}


GARMIN_UNITS = {
    'gga' : {
        'utc':'utc',
        'lon':'longitude',
        'lat':'latitude',
        'fix':'fix_type',
        'sat':'num_satellites',
        'hdp':6,
        'alt':'altitude',
        'geo':'geodetical',
        'dgp':9,
    },
    'rmc' : {
        'lat':'latitude',
        'lon':'longitude',
        'spd':'speed',
        'cor':4,
        'utc':5,
        'utcd':6,
        'mag':7,
    },


}

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


            print na
            # print "AA"
            # print args
            # print zip(('utc', 'lon', 'lat', 'fix', 'sat', 'hdp', 'alt', 'geo', 'dgp'), map(repr, args))
            # args=dict((y, x) for x, y in args)
            data={}
            data['utc']=na['utc']
            # data['fix']=na['fix']


            self.upload(data,"GGA")


        def handle_positiontime(self, *args):
            """"""
            # log.msg('positiontime:\n' +
            # '\n'.join(map(lambda n: '  %s = %s' % tuple(n), zip(('lat', 'lon', 'spd', 'cor', 'utc', 'utcd', 'mag'), map(repr, args)))))
            na=dict(zip(('lat', 'lon', 'spd', 'cor', 'utc', 'utcd', 'mag'), map(repr, args)))
            print na
            # print "AA"
            # print args
            # args=dict((y, x) for x, y in args)

            data={}
            # data['speed']=na['spd']
            data['utd']=na['utc']
            # data['utcd']=na['utcd']
            # data['magvar']=na['mag']

            self.upload(data,"RMC")


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


            # self.upload(data)


        def upload(self,data,reg):
            for k,v in data.iteritems():
                ts = int(time.time())
                val = float(v.replace("'",''))
                path = 'gps/'+k
                unit = "deg"

                if not self.inst.lookup(path):
                    self.inst.add_timeseries(path, unit, data_type='double')

                self.inst.add(path,ts,val)


            ### TODO: append
            for k,v in GARMIN_POINTS[reg].iteraitems():
              unit = GARMIN_UNITS[reg][data[0]]
              path = '%s/%s' % (point, k)
              if not self.inst.lookup(path):
                self.inst.add_timeseries(path,unit,data_type='double')

              val = float(data.get(v[0]))
              self.inst.add(path,ts,val)



             testGGA():

             testRMC():



        # def process(self, line):
        #     fields = line.split(',')
        #     reg = fields[0][1:]
        #     def proc_field(f):
        #         v = f.split('=')
        #         return (v[0], (v[1][:-1], v[1][-1]))
        #     data = dict(map(proc_field, fields[1:]))
        #
        #     if VAISALA_POINTS.has_key(reg):
        #         ts = int(time.time())
        #         point = VAISALA_POINTS[reg][0]
        #         # create the point in the smap tree if necessary
        #         for k,v in VAISALA_POINTS[reg][1].iteritems():
        #             unit = VAISALA_UNITS[reg][data[v[0]][1]]
        #             path = '/%s/%s' % (point, k)
        #             if not self.inst.lookup(path):
        #                 self.inst.add_timeseries(path, unit, data_type='double')
        #
        #             val_ = float(data.get(v[0])[0])
        #             min_ = data.get(v[1], None)
        #             if min_ != None: min_ = min_[0]
        #             max_ = data.get(v[2], None)
        #             if max_ != None: max_ = max_[0]
        #             self.inst.add(path, ts, val_)



    def setup(self, opts):
        self.port = opts.get('Port')
        self.log = logging.getLogger('GarminReader')
        self.set_metadata('/', {
            'Extra/Driver' : 'garmin.GarminSerial',
            'Instrument/Manufacturer' : 'Garmin',
            'Instrument/Model' : '' })


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

