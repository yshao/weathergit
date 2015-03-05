import numpy as np

from smap import operators
from smap.archiver.client import RepublishClient, SmapClient
from smap.ops.filters import SubsampleOperator, MovingAverageOperator

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/4/2015' '10:35 AM'

op=MovingAverageOperator()


op=SubsampleOperator()


def thetaprobe(inputs):
    """

    T[i]= HI - LOW * 100

    :param inputs:
    :return:
    """

    if len(inputs) == 0:
        return null

    for i in xrange(1,len(inputs)):

        inputs = np.array(inputs, dtype=float)
        #HI
        HI=inputs[i][0]
        #LOW
        LOW=inputs[i][1]

        (HI - LOW) * 100

    print inputs




    return inputs



class ProcessOperator(operators.ParallelSimpleOperator):
    base_operator = staticmethod(thetaprobe)
    name = 'movingavg-'
    operator_name = 'movingavg'
    operator_constructors = [(),
                             (int,)]
    def __init__(self, inputs, lag=10):
        self.name = 'movingavg-' + str(lag)
        operators.ParallelSimpleOperator.__init__(self, inputs, lag=lag)


### test ###
c=SmapClient()
inputs=c.data_uuid()

# hist=null
inputs = np.array(inputs, dtype=float)
data = np.vstack(inputs)


nd=thetaprobe(inputs)

RepublishClient()