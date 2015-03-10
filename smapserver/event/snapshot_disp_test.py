# smaptool get longitude, latitude, time
from time import sleep
from weathergit.common.smaputils import SmapUtils


args=dict(url="192.168.1.146")
smaputils=SmapUtils(args)

gen={}
gen['lon']=smaputils.get_curr_val('/garmin0/longitude')
gen['lat']=smaputils.get_curr_val('/garmin0/latitude')
gen['alt']=smaputils.get_curr_val('/garmin0/altitude')
# utc=smaputils.get_curr_val('/garmin0/utc')

with open('panel','wb') as f:
    f.write(gen)

# get image from database
filep=smaputils.get_image('/trendnet0/timestamp')

# get plots
paths=['']
for p in paths:
    ""

def get_smap_values():
    ""