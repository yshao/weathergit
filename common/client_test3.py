from smap.archiver.client import SmapClient
c = SmapClient("http://192.168.1.114:8079")

from smap.contrib import dtutil

start = dtutil.dt2ts(dtutil.strptime_tz("12-5-2014", "%m-%d-%Y"))
end   = dtutil.dt2ts(dtutil.strptime_tz("12-8-2014", "%m-%d-%Y"))

oat = [
  "e0dcdc20-a6ae-5137-8d77-d728c2f565d2"
]
data = c.data_uuid(oat, start, end)

data2=c.query("select distinct Metadata/SourceName where Metadata/Instrument/Manufacturer like 'BEST%'")

print data2

from matplotlib import pyplot, dates

for d in data:
  pyplot.plot_date(dates.epoch2num(d[:, 0] / 1000), d[:, 1], '-',
                   tz='America/Denver')

pyplot.show()

