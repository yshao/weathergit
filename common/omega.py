import Adafruit_BBIO.ADC as ADC
from smap.driver import SmapDriver
from smap.util import periodicSequentialCall

class Omega(SmapDriver):
    def setup(self, opts):
        self.tz = opts.get('Timezone', 'America/Denver')
        self.rate = float(opts.get('Rate', 1))
        ADC.setup()

        self.add_timeseries('/soil_temp', 'V', data_type="double")
        self.add_timeseries('/supply_volt', 'V', data_type="double")

    def start(self):
        # call self.read every self.rate seconds
        periodicSequentialCall(self.read).start(self.rate)

    def read(self):
        temp = ADC.read("AIN2") * 1.8
        supply= ADC.read("AIN3") * 1.8

        self.add('/soil_temp',temp)
        self.add('/supply_volt',supply)