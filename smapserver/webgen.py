import os
import re
from common.env import Env
from common.smaputils import SmapUtils
from remote import Remote


def update_webpage():
    ""
    d=Env().getConfig()

    url=dict(url=d['smap_source_mon'])
    # print args
    # smaputils=SmapUtils()

    su=SmapUtils()
    d=su.get_smap_time_dict('weather.ini')


    GENDIR='generate'
    with open('%s/panel.txt'%GENDIR,'wb') as f:
        for k in d.keys():
            line='%s %s %s' % (k,d[k]['time'],d[k]['mea'])
            f.write(line)

    # get image from database
    # d=su.get_smap_time_dict('trendnet.ini')
    # print d
    # filep=d['/trendnet0/time']['mea']
    # d=Remote.gen_login('webserver')
    # dataserver=Remote(d)
    # dataserver.download('%s.png'%filep,GENDIR)

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
    print "Updating webpage"
    update_webpage()