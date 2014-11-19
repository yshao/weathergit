from smap.archiver.client import SmapClient
from smap.contrib import dtutil

from matplotlib import pyplot
from matplotlib import dates


host="192.168.1.146"
port="8142"

### write exception
addr=host+":"+port

# make a client
c = SmapClient(addr)

# start and end values are Unix timestamps
start = dtutil.dt2ts(dtutil.strptime_tz("11-11-2014", "%m-%d-%Y"))
end   = dtutil.dt2ts(dtutil.strptime_tz("11-12-2014", "%m-%d-%Y"))

# hard-code the UUIDs we want to download
oat = [
  "c2fdfc5c-2c5a-11e1-b1bc-0001c007cd3a",
]

# perform the download
data = c.data_uuid(oat, start, end)

# plot all the data
#  use the epoch2num to convert to pylab date formats
for d in data:
  pyplot.plot_date(dates.epoch2num(d[:, 0] / 1000), d[:, 1], '-',
                   tz='America/Los_Angeles')

pyplot.show()