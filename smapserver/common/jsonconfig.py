import json
from pprint import pprint

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/2/2015' '11:28 AM'

class JsonConfig():
    ""
    def __init__(self,filep=None):
        ""
        if filep != None:
            self.load(filep)

    def parse(self):
        ""

    def load(self,filep):
        ""
        self.d=json.load(open(filep,'rb'))
        # print self

    def save(self,filep):
        json.dump(self.d,open(filep,'wb'))

    def get_config(self):
        return self.d


if __name__ == '__main__':
    cfg=JsonConfig('test.json')
    pprint(cfg)


