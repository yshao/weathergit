# smaptool get longitude, latitude, time
from time import sleep
from weathergit.common.smaputils import SmapUtils


args=dict(url="192.168.1.146")
smaputils=SmapUtils(args)
lon=smaputils.get_curr_val('/garmin0/longitude')
lat=smaputils.get_curr_val('/garmin0/latitude')
utc=smaputils.get_curr_val('/garmin0/utc')

# get image from database
filep=smaputils.get_image('/trendnet0/timestamp')


def get_smap_values():
    ""