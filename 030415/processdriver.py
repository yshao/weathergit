from smap.archiver.client import SmapClient, RepublishClient
from smap.operators import OperatorDriver

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/4/2015' '11:16 AM'


HOST='http://192.168.1.120:8079'
source_ids=['']

class ProcessDriver(OperatorDriver):
    def setup(self,opts):
        ""

        restrict=opts.get('Restrict','')
        # client=SmapClient()
        client=SmapClient(HOST)
        source_ids=client.tags(restrict,'uuid, Properties/UnitofMeasure')
        for id in source_ids:
            ""
            uuid=str(id['uuid'])
            if not 'Properties/UnitofMeasure' in id:
                id['Properties/UnitofMeasure'] = ''
            if not uuid in self.operators:
                ""

        RepublishClient()


    def process(self):
        self.op='thetaprobe'


    def update(self):
        ""
