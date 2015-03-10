import Adafruit_BBIO.ADC as ADC
from smap.driver import SmapDriver
from smap.util import periodicSequentialCall

class Omega(SmapDriver):
    def setup(self, opts):
        self.tz = opts.get('Timezone', 'America/Denver')
        self.rate = float(opts.get('Rate', 1))
        ADC.setup()

        self.add_timeseries('/tempLO', 'mV', data_type="double")
        self.add_timeseries('/tempHI', 'mV', data_type="double")


    def start(self):
        # call self.read every self.rate seconds
        periodicSequentialCall(self.read).start(self.rate)

    def read(self):
        voltageHI = ADC.read("AIN0") * 1800 #1.8V
        voltageLO = ADC.read("AIN1") * 1800 #1.8V

        # print voltage
        self.add('/tempLO',voltageLO)
        self.add('/tempHI',voltageHI)