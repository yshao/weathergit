import Adafruit_BBIO.ADC as ADC
from smap.driver import SmapDriver
from smap.util import periodicSequentialCall

class ThetaProbe(SmapDriver):
    def setup(self, opts):
        self.tz = opts.get('Timezone', 'America/Los_Angeles')
        self.rate = float(opts.get('Rate', 1))
        ADC.setup()

        self.add_timeseries('/humidity', 'V', data_type="double")

    def start(self):
        # call self.read every self.rate seconds
        periodicSequentialCall(self.read).start(self.rate)

    def read(self):
        value = ADC.read("AIN1")
        voltage = value * 1.8 #1.8V

        print voltage
        self.add('/humidity',voltage)