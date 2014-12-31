import Adafruit_BBIO.ADC as ADC
from smaputil.driver import SmapDriver
from smaputil.util import periodicSequentialCall

class ThetaProbe(SmapDriver):
    def setup(self, opts):
        self.tz = opts.get('Timezone')
        self.rate = float(opts.get('Rate', 1))
        ADC.setup()

        self.add_timeseries('/humidityLO', 'V', data_type="double",timezone=self.tz)
        self.add_timeseries('/humidityHI', 'V', data_type="double",timezone=self.tz)

    def start(self):
        # call self.read every self.rate seconds
        periodicSequentialCall(self.read).start(self.rate)

    def read(self):

        voltageLO = ADC.read("AIN2") * 1.8 #1.8V
        voltageHI = ADC.read("AIN3") * 1.8 #1.8V

        # print voltage
        self.add('/humidityLO',voltageLO)
        self.add('/humidityHI',voltageHI)