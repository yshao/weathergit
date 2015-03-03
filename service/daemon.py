import threading
import psutil
from common.logger import Logger
from weathergit.common.jsonconfig import JsonConfig
from weathergit.event import Event

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/2/2015' '2:36 PM'

class EventSystem(object):
    def __init__(self):
        config=JsonConfig('event.json')
        self.pid=[]
        self.l=Logger('weatherevent')

        for c in config:
            evt= Event(c)
            t=threading.Thread(evt,time=evt['interval'])
            self.pid.append(t)
            t.start()

    def status(self):
        d={}
        for p in self.pid:
            d[p]={}
            d[p]['running']=psutil.find(p)



if __name__ == '__main__':
    main=EventSystem()
    daemon=daemonize(main)
    daemon.start()