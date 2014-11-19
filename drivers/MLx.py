import sys
import logging
import time
import socket
import os

from twisted.python import log

import smap.driver as driver
import smap.util as util
import Adafruit_BBIO.ADC as ADC

class IseriesSteam(driver.SmapDriver):
    def setup(self, opts):
        self.host = opts.get("Host", "10.0.50.119")
        self.rate = int(opts.get("Rate", 30))
        self.add_timeseries("/0", "ga/min", data_type='double')
        self.add_timeseries("/1", "ga", data_type='double')
        self.set_metadata("/", {
            'Instrument/ModelName' : 'ThetaProbe MLx'
            })

    def start(self):
        self.last_add = 0
        self.accum = 0
        self.last_time = None
        self.s = None
        util.periodicSequentialCall(self.update).start(1)

    # def connect(self):
    #     if self.s: return
    #     self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     try:
    #         self.s.settimeout(5)
    #         self.s.connect((self.host, 1000))
    #     except IOError:
    #         log.err()
    #         self.s = None

    def update(self):
        val=self.many_read_adc()
        self.filter(val)



    def test_setup_adc(self):
        ADC.setup()

        files = os.listdir('/sys/devices')
        ocp = '/sys/devices/'+[s for s in files if s.startswith('ocp')][0]
        files = os.listdir(ocp)
        helper_path = ocp+'/'+[s for s in files if s.startswith('helper')][0]

        assert os.path.exists(helper_path + "/AIN1")
        #ADC.cleanup()



    def test_many_read_adc(self):
        import time

        ADC.setup()
        value=[]

        for x in range(0,10000):
            start = time.time()
            value[x] = ADC.read("AIN1")
            assert value[x] != -1

        return value


    def filter(self,val):
      ""


    def update(self, cmd="*01X01"):
        self.connect()
        if not self.s:
            return

        try:
            self.s.send(cmd + "\r")
            reply = self.s.recv(1024)
            self.s.close()
            self.s = None
        except IOError, e:
            log.err()
            return 
        else:
            if reply.startswith(cmd[1:]):
                val = float(reply[len(cmd) - 1:-1])
                # log.msg("read: " + str(val))
                if val == None:
                   time.sleep(0.5)
                   log.err("Failed to update reading")
                   return
            else:
                return
        this_time = util.now()

        # accumulate readings
        if self.last_time:
            self.accum += (self.last_time[1] + val) * ((this_time - self.last_time[0]) / 60.) * 0.5
            
        # and output a reading ever RATE seconds
        if this_time - self.last_add > self.rate:
            self.add('/0', this_time, float(val))
            self.add('/1', this_time, float(self.accum))
            self.last_add = this_time
        self.last_time = (this_time, val)
