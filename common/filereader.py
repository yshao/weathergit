from smap.driver import FetchDriver

class SimpleDriver(FetchDriver):
 def setup(self, opts):
     FetchDriver.setup(self, opts)
     self.add_timeseries('/data', 'C')

 def process(self, data):
     self.add('/data', float(data))



