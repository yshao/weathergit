import os
from common.env import Env
from common.smaputils import SmapUtils
from remote import Remote


def update_webpage():
    ""

    d=Env().getConfig()

    args=dict(url=d['smap_source_host'])
    smaputils=SmapUtils(args)

    gen={}
    gen['lon']=smaputils.get_curr_val('/garmin0/longitude')
    gen['lat']=smaputils.get_curr_val('/garmin0/latitude')
    gen['alt']=smaputils.get_curr_val('/garmin0/altitude')

    GENDIR='generate'
    with open('%s/panel.txt'%GENDIR,'wb') as f:
        f.write(gen)

    # get image from database
    filep=smaputils.get_curr_val('/trendnet0/timestamp')
    d=Remote.gen_login('webserver')
    dataserver=Remote(d)
    dataserver.download('%s.png'%filep,GENDIR)

    # get plots
    paths=[
        '/thetaprobe0/soil_moistureHI',
        '/omega0/soil_tempHI',
        '/vaisala0/pth/pressure',
        '/vaisala0/pth/temperature',
        '/vaisala0/pth/humidity'
    ]
    for p in paths:
        ""
        gen_plot(p)


    # upload all to webserver
    d=Remote.gen_login('webserver')
    remote=Remote(d)

    lFiles=os.list(GENDIR)
    remote.upload(lFiles)

def gen_plot(p):
    name=p.replace('/','_')
    with open(name,'wb') as fh:
        fh.write('b')


if __name__ == '__main__':
    update_webpage()