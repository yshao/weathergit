import Adafruit_BBIO.ADC as ADC
from smap.driver import SmapDriver
from smap.util import periodicSequentialCall

class ThetaProbe(SmapDriver):
    def setup(self, opts):
        #self.tz = opts.get('Properties/Timezone', 'America/Denver')
	#self.tz = 'America/Denver'
        self.rate = float(opts.get('Rate', 1))
        ADC.setup()

        self.add_timeseries('/soil_moistureLO', 'V', data_type="double")
        self.add_timeseries('/soil_moistureHI', 'V', data_type="double")

    def start(self):
        # call self.read every self.rate seconds
        periodicSequentialCall(self.read).start(self.rate)

    def read(self):

        voltageLO = ADC.read("AIN2") * 1.8 #1.8V
        voltageHI = ADC.read("AIN3") * 1.8 #1.8V

        # print voltage
        self.add('/soil_moistureLO',voltageLO)
        self.add('/soil_moistureHI',voltageHI)
