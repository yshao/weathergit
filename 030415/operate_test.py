from smap import smapconf
from smap.archiver.client import SmapClient
from smap.operators import CompositionOperator, OperatorDriver
from smap.ops.filters import SubsampleOperator


class ProcessSampler(CompositionOperator):
    name = 'process'
    operator_constructors=[()]

    oplist = [



    ]

BACKEND='http://192.168.1.120:8079'

class SampleDriver(OperatorDriver):
    def setup(self, opts):
        """
        Set up what streams are to be processed.
        """
        restrict = opts.get("Restrict",
                            "has Path and (not has Metadata/Extra/SourceStream)")
        OperatorDriver.setup(self, opts, shelveoperators=False, raw=True,
                             inherit_metadata=False)
        # client = SmapClient(smapconf.BACKEND)
        client= SmapClient(BACKEND)
        source_ids = client.tags(restrict, 'uuid, Properties/UnitofMeasure')
        for new in source_ids:
            id = str(new['uuid'])
            if not 'Properties/UnitofMeasure' in new:
                new['Properties/UnitofMeasure'] = ''
            if not id in self.operators:
                o1 = SubsampleOperator([new], 300)
                self.add_operator('/%s/%s' % (id, o1.name), o1)
                o2 = SubsampleOperator([new], 3600)
                self.add_operator('/%s/%s' % (id, o2.name), o2)
        log.msg("Done setting up subsample driver; " + str(len(source_ids)) + " ops")