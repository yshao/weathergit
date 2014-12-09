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


from matplotlib import pyplot, dates

for d in data:
  pyplot.plot_date(dates.epoch2num(d[:, 0] / 1000), d[:, 1], '-',
                   tz='America/Denver')

pyplot.show()