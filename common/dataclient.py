from smap.archiver.client import SmapClient
from smap.contrib import dtutil
from weathergit.common.config import Config
from weathergit.common.env import Env


class DataClient(object):
    def __init__(self,login=None):
        """"""

        if login == None:
            login={}
            config=Config(Env.getpath('HOME')+'/common/weatherplotter.conf')
            login['host']=config['smap_server_host']
            login['port']=config["smap_server_port"]
            self.login=login
        else:
            self.login=login

        print "http://%(host)s:%(port)s" % self.login
        self.c = SmapClient("http://%(host)s:%(port)s" % self.login)




    def get_data(self,uuid,start,end,limit=-1):
        # print start
        # print end
        startTime = dtutil.dt2ts(dtutil.strptime_tz(start, "%m/%d/%Y %H:%M:%S %p" ))
        endTime   = dtutil.dt2ts(dtutil.strptime_tz(end, "%m/%d/%Y %H:%M:%S %p"))
        return self.c.data_uuid(uuid, startTime, endTime,True,limit)