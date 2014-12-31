### testing numpy with data from smap server ###

from weathergit.common.config import Config
from weathergit.common.dataclient import DataClient
import datetime


print datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
print datetime.datetime.utcnow()

def movingaverage(values,window):
    weigths = np.repeat(1.0, window)/window
    #including valid will REQUIRE there to be enough datapoints.
    #for example, if you take out valid, it will start @ point one,
    #not having any prior points, so itll be 1+0+0 = 1 /3 = .3333
    smas = np.convolve(values, weigths, 'valid')
    return smas # as a numpy array

# Get a date object
today = datetime.date.today()

start="12/20/2014 12:00:00 AM"
end=today.strftime("%m/%d/%Y %H:%M:%S %p").__str__()
print start
print end

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
# print data[0]

print uuid[1]
# print data[1]



d0=np.array(data[0])
d1=np.array(data[1])

D0=d0.astype(float)
D1=d1.astype(float)


print D0.shape
print D1.shape
print D0[:,1]
print D1[:,1]

row=D0.shape[0]

### convert to moisture percentage
Dx=D0[:,0]
Dy=D0[:row-1,1] - D1[:row,1]
Dy= Dy * 100

unit='%'

#Will print out a 3MA for our dataset
WIN_SIZE=5
Dy=np.round(movingaverage(Dy,WIN_SIZE),2)
Dx=movingaverage(Dx,WIN_SIZE)

print Dx
print Dy

### convert to temp reading
uuid = ['efc84c16-a470-549f-92d3-4324e2bf1864', #HI
        '62a74dc0-d3c1-5986-aefa-953bf7a616e7'] #LO

data = dc.get_data(uuid, start, end)
d0=np.array(data[0])
d1=np.array(data[1])
D0=d0.astype(float)
D1=d1.astype(float)

print D0.shape
print D1.shape


row=D0.shape[0]

R_CURRENT=0.95

Dtx=D0[:,0]
Dty=d0[:row-2,1] - D1[:row,1]
Rty= Dty / R_CURRENT
# unit='C'
# 0.00385 ohm/ohm/deg. C
print Rty * 0.00385
#


