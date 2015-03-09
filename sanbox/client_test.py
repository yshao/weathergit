from smap.archiver.client import SmapClient
from smap.contrib import dtutil

from matplotlib import pyplot
from matplotlib import dates


host="192.168.1.120"
port="8079"

### write exception
addr=host+":"+port

# make a client
c = SmapClient(addr)

# start and end values are Unix timestamps
start = dtutil.dt2ts(dtutil.strptime_tz("11-18-2014", "%m-%d-%Y"))
end   = dtutil.dt2ts(dtutil.strptime_tz("11-19-2014", "%m-%d-%Y"))

# hard-code the UUIDs we want to download
oat = [
  "0049d709-eb70-50b5-8349-859ab8b9c9f8",
  "ab56dd4e-87ce-550c-a765-de80338d1843"
]

# perform the download
data = c.data_uuid(oat, start, end)

# plot all the data
#  use the epoch2num to convert to pylab date formats
for d in data:
  pyplot.plot_date(dates.epoch2num(d[:, 0] / 1000), d[:, 1], '-',
                   tz='America/Los_Angeles')

pyplot.show()