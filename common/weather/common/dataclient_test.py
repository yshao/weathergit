from common.config import Config
from common.dataclient import DataClient
import datetime

# Get a date object
today = datetime.date.today()

start="12-8-2014"
end=today.strftime("%m-%d-%Y").__str__()

# print datetime.date.today.strftime("%m-%d-%Y")

uuid = [
  "63f6eb56-9bf4-5356-845a-80a315909d75"
]

config= Config("weatherplotter.conf")
login={}
login['host']=config['smap_server_host']
login['port']=config["smap_server_port"]

d=DataClient(login)

data = d.get_data(uuid, start, end)
# print data
assert data.__sizeof__() > 0

# c.data

from matplotlib import pyplot, dates

for d in data:
  pyplot.plot_date(dates.epoch2num(d[:, 0] / 1000), d[:, 1], '-',
                   tz='America/Denver')

pyplot.show()