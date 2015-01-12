class FileDriver(driver.SmapDriver):
    """Driver which creates a single point backed by a file.  You
    could use this, for instance, to expose flags in /proc"""
    def setup(self, opts):
        filename = opts.pop('Filename', '~/FileActuatorFile')
        self.add_actuator('/point0', 'Switch Position',
                          FileActuator, setup={'filename': filename})





# create the file
echo 1 > ~/smap-actuator.txt

# get the current value
curl http://localhost:8080/data/actuator0/point0
{"Properties": {"Timezone": "America/Los_Angeles", "UnitofMeasure": "Switch Position", "ReadingType": "long"}, "Actuate": {"Model": "binary"}, "uuid": "7afaa0a6-7719-5c1b-ae38-0f03b6d35256", "Readings": [[1354064481000, 0]]}

# change the state
curl  -XPUT localhost:8080/data/actuator0/point0?state=1
{"Properties": {"Timezone": "America/Los_Angeles", "UnitofMeasure": "Switch Position", "ReadingType": "long"}, "Actuate": {"Model": "binary"}, "uuid": "7afaa0a6-7719-5c1b-ae38-0f03b6d35256", "Readings": [[1354064507000, 1]]}