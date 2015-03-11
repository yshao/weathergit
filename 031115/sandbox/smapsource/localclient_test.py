from smap.archiver.client import SmapClient

c = SmapClient("http://www.openbms.org/backend")

from smap.contrib import dtutil

start = dtutil.dt2ts(dtutil.strptime_tz("6-12-2014", "%m-%d-%Y"))
end   = dtutil.dt2ts(dtutil.strptime_tz("11-13-2014", "%m-%d-%Y"))

oat = [
  "395005af-a42c-587f-9c46-860f3061ef0d",
  "9f091650-3973-5abd-b154-cee055714e59",
  "5d8f73d5-0596-5932-b92e-b80f030a3bf7",
  "ec2b82c2-aa68-50ad-8710-12ee8ca63ca7",
  "d64e8d73-f0e9-5927-bbeb-8d45ab927ca5"
]
data = c.data_uuid(oat, start, end)

from matplotlib import pyplot, dates

for d in data:
  pyplot.plot_date(dates.epoch2num(d[:, 0] / 1000), d[:, 1], '-',
                   tz='America/Denver')

pyplot.show()






# start= mon.ui.inStartDate.getText()
# end= mon.ui.inEndDate.getText()
#
# start = dtutil.dt2ts(dtutil.strptime_tz(start, "%m-%d-%Y"))
# end   = dtutil.dt2ts(dtutil.strptime_tz(end, "%m-%d-%Y"))

