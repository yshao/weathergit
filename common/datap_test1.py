### testing numpy with data from smap server ###

from common.config import Config
from common.dataclient import DataClient
import datetime


def movingaverage(values,window):
    weigths = np.repeat(1.0, window)/window
    #including valid will REQUIRE there to be enough datapoints.
    #for example, if you take out valid, it will start @ point one,
    #not having any prior points, so itll be 1+0+0 = 1 /3 = .3333
    smas = np.convolve(values, weigths, 'valid')
    return smas # as a numpy array

# Get a date object
today = datetime.date.today()

start="12/8/2014 12:00:00 AM"
end=today.strftime("%m/%d/%Y %H:%M:%S %p").__str__()

# print datetime.date.today.strftime("%m-%d-%Y")


uuid = ['e0dcdc20-a6ae-5137-8d77-d728c2f565d2',
        '7afaaaac-9eb6-5882-8818-268b53a90925']



config= Config("weatherplotter.conf")
login={}
login['host']=config['smap_server_host']
login['port']=config["smap_server_port"]

dc=DataClient(login)

data = dc.get_data(uuid, start, end)

import numpy as np
print uuid[0]
print data[0]

print uuid[1]
print data[1]



d0=np.array(data[0])
d1=np.array(data[1])

print "combined"

D0=d0.astype(float)
D1=d1.astype(float)


print D0.shape
print D1.shape
print D0[:,1]
print D1[:,1]

row=D0.shape[1]

### convert to hum percentage
Dx=D0[:,0]
Dy=D0[:,1] - D1[:72861,1]
Dy= Dy * 100

unit='%'

#Will print out a 3MA for our dataset
WIN_SIZE=5
Dy=movingaverage(Dy,WIN_SIZE)
Dx=movingaverage(Dx,WIN_SIZE)

print Dx
print Dy

### convert to temp reading
R_CURRENT=1.8

Dx=D0[:,0]
Dy=D0[:,1] - D1[:72861,1]
Dy= Dy / R_CURRENT

print Dy

unit='C'





### RTD conversion chart ###
