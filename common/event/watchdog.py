import datetime
from common.env import Env
from supervisory import Supervisory
from remote import Remote
# from common.smaputils import SmapUtils
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
        print "Initializing"
        self.cfg=Env().getConfig()
        self.update_status()
        print "Done Initializing"

    def update_status(self):
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
        if not self.check_network():
            ""
            send_event_email('Network Down %s')


        ### find all the service is running
        super=Supervisory()
        d=super.get_all_pids()
        l=['trendnet.ini','weather.ini','scheduler.py']
        for e in l:
            if not e in d.keys():
                super.restart(e)
                send_event_email('Restart service %s' % e)


        if not self.check_measurements():
            ""
            for e in l:
                super.restart(e)
                send_event_email('Restart service %s' % e)

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
            d=run_command('ping %s' % link)
            is_connected(d)

    def check_measurements(self):
        ""
        return True

    def check_disk(self):
        ''
        return True
#
#
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

#
# def frozen_measurements():
#   """
#   Check if encounters measurements not updating
#   Restart
#   """
#
#   d=Env().getConfig()
#   args=dict(url=d['smap_server_host'])
#   smaputils=SmapUtils(args)
#   mon=smaputils.get_smap_monitor()
#
#   prev=pickle.load('z1')
#   timeval=mon
#   pickle.dump('z1',timeval)
#
#   #action
#   if compareUpdate(prev,timeval):
#     return True
#   else:
#     return False

# def compareUpdate(l1,l2):
#     def convert_tm(tm):
#         return datetime.timedelta
#
#     for k in l1.keys():
#         if convert_tm(l1.get(k)) - convert_tm(l2.get(k)) > 0:
#             return False
#
#     return True



# # def handle_instruments():
# #     read=su.curr_readings()
# #     read_old=open('instruments.buf','rb').read()
# #     res=compare_readings(read,read_old)
# #     if res
# #         return res
# #         print 'readings good'
# #     else:
# #         restart_smap()
# #         print 'readings bad'