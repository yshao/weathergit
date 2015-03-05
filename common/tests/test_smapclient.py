import urllib
import urllib2
from smap.archiver.client import SmapClient

host='192.168.1.120'
port='8079'

startTime="12-8-2014"
endTime="12-9-2014"

c = SmapClient("http://"+host+":"+port)

from smap.contrib import dtutil

start = dtutil.dt2ts(dtutil.strptime_tz(startTime, "%m-%d-%Y"))
end   = dtutil.dt2ts(dtutil.strptime_tz(endTime, "%m-%d-%Y"))

uuid = [
  "63f6eb56-9bf4-5356-845a-80a315909d75"
]
data = c.data_uuid(uuid, start, end)

# c.data

### test matplot
# from matplotlib import pyplot, dates
#
# for d in data:
#   pyplot.plot_date(dates.epoch2num(d[:, 0] / 1000), d[:, 1], '-',
#                    tz='America/Denver')
#
# pyplot.show()

# class DataClient(object):
#     def __init__(self,login):
#         """"""
#         self.c = SmapClient("http://%(host)s:%(port)s" % login)
#
#
#     def get_data(self,start,end,uuid):
#         start = dtutil.dt2ts(dtutil.strptime_tz(startTime, "%m-%d-%Y"))
#         end   = dtutil.dt2ts(dtutil.strptime_tz(endTime, "%m-%d-%Y"))
#         return self.c.data_uuid(uuid, start, end)

def test_backend():
    base='http://192.168.1.120:8079'
    q=''
    timeout=5
    d={}
    try:
        fp = urllib2.urlopen(base + '/api',
                             timeout=timeout)
        # rv = parser(fp.read())
    except urllib2.HTTPError:
        # log.err("Bad request running query: ""%s"" " % q)
        # raise SmapException()
        return False
    fp.close()

    return True

print test_backend()


# data_to_mat(data)