import json
from pprint import pprint

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/2/2015' '11:28 AM'

class JsonConfig(dict):
    ""
    def __init__(self,filep=None):
        ""
        if filep != None:
            self.load(filep)

    def parse(self):
        ""

    def load(self,filep):
        ""
        self=json.load(open(filep,'rb'))

    def save(self,filep):
        json.dump(self,open(filep,'wb'))



cfg=JsonConfig('test.json')
pprint(cfg)


