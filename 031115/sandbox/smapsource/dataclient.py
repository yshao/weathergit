from smap.archiver.client import SmapClient
from smap.contrib import dtutil

class DataClient(object):
    def __init__(self,login):
        """"""
        self.c = SmapClient("http://%(host)s:%(port)s" % login)


    def get_data(self,uuid,start,end,limit=-1):
        # print start
        # print end
        startTime = dtutil.dt2ts(dtutil.strptime_tz(start, "%m/%d/%Y %H:%M:%S %p" ))
        endTime   = dtutil.dt2ts(dtutil.strptime_tz(end, "%m/%d/%Y %H:%M:%S %p"))
        return self.c.data_uuid(uuid, startTime, endTime,True,limit)