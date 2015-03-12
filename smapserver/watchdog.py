import datetime
import time
import re
from common.env import Env
from supervisory import Supervisory
from remote import Remote
from common.smaputils import SmapUtils
from event.disk_usage import diskmain
from event.notify import send_event_email
from common.sysutils import run_command

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/2/2015' '5:14 PM'

import pickle

class Watchdog():
    def __init__(self):
        ""
        # print "Initializing"
        self.cfg=Env().getConfig()
        # self.update_status()
        # print "Done Initializing"

    def update_status(self):
        self.watchdog()

        print "updating"
        txt1='\n'.join(diskmain())
        print txt1
        super=Supervisory()
        txt2='\n'.join((super.get_all_pids()))
        print txt2
        content='\n'.join([txt1,txt2])
        print content
        send_event_email(content)




    def watchdog(self):
        ### check network is up ###
        # if not self.check_network():
        #     ""
        #     send_event_email('Network Down %s')


        ### find all the service is running
        super=Supervisory()
        d=super.get_all_pids()
        l=['trendnet.ini','weather.ini','scheduler.ini']
        for e in l:
            if not e in d.keys():
                super.restart(e)
                send_event_email('Restart service %s' % e)


        if not self.check_measurements('weather.ini'):
            ""
            super.restart('weather.ini')
            send_event_email('Restart service %s' % 'weather.ini')

        if not self.check_measurements('trendnet.ini'):
            ""
            super.restart('trendnet.ini')
            send_event_email('Restart service %s' % 'trendnet.ini')

        if not self.check_disk():
            ""
            send_event_email('Flushing Disk')




    ### check actions ###
    def check_network(self):
        def is_connected(d):
            if 'Unreachable' in d or 'unreachable' in d:
                return False
            else:
                return True
#
        l=[self.cfg['smap_server_host'],self.cfg['smap_source_host'],self.cfg['data_server_host'],'192.168.1.121']
        for link in l:
            print 'ping %s' % link
            d=run_command('ping %s' % link)
            is_connected(d)

    def check_measurements(self,target):
        ""
        ### get current values###
        su=SmapUtils()
        lines=su.get_smap_time(target)
        d={}
        for l in lines:
            sl=re.split(r' *', l)
            d[sl[1]]={}
            d[sl[1]]['time']=sl[0]
            d[sl[1]]['mea']=sl[2]
        import datetime
        ###calc time diff###
        for k in d.keys():
            date_str=d[k]['time']
            # print date_str
            nd=date_str[0:-6]
            td=date_str[-5:]

            naive_dt = datetime.datetime.strptime(nd, '%Y-%m-%dT%H:%M:%S')
            mea_tm= time.mktime(naive_dt.timetuple())
            now_tm= time.mktime(datetime.datetime.now().timetuple())
            if abs(now_tm - mea_tm) > 420:
                return False

        return True

    def check_disk(self):
        ''
        return True


if __name__ == '__main__':
    dog=Watchdog()
    dog.watchdog()
    # dog.check_measurements('weather.ini')
    # dog.check_measurements('trendnet.ini')
    dog.check_network()


# def disk_level():
#   """
#
#   flush,notify
#   """
#
#   d=diskmain()
#   if d['space']:
#     return True
#   else:
#     flush_smap_disk()
#
# ############ disk_level #########
# def flush_smap_disk():
#     ""
#     remote=Remote()
#     remote.execute('','/')
#
#
#     ### check for frozen instruments ###
#     # d=find_frozen_measurements()
#     #     ""
#     #
#     # ### check disk level ###
#     # if disk_level():
#     #     flush_smap_disk()
#     #     send_event_email('Disk buffer flushed')
#
#     ### send report ###
#     # update_status()
#
