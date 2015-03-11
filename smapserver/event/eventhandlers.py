import datetime
from common.env import Env
from common.remote.remote import Remote
from common.smaputils import SmapUtils

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/2/2015' '5:14 PM'

import pickle

server_service=list(
    'trendnet.ini'
    'webserver.py'
)

smap_service=list(
    'weather.ini'
)

def watchdog():
    if unable_to_connect():
        ""
        send_event_email('Network Down %s')
    ### find all the service is running
    remote=Remote(Remote.gen_login('smapsource'))
    pid=remote.get_pids()
    for s in server_service:
        if s not in pid.keys():
            remote.daemon()

    remote=Remote(Remote.gen_login('smapserver'))
    for s in server_service:
        if !check_pid(s)
            start()

    if frozen_measurements():
        ""


    if disk_level():
        flush_smap_disk()
        send_event_email('Disk buffer flushed')

    update_status()

def compareUpdate(l1,l2):
    def convert_tm(tm):
        return datetime.timedelta

    for k in l1.keys():
        if convert_tm(l1.get(k)) - convert_tm(l2.get(k)) > 0:
            return False

    return True

def frozen_measurements():
  """
  Check if encounters measurements not updating
  Restart
  """

  d=Env().getConfig()
  args=dict(url=d['smap_server_host'])
  smaputils=SmapUtils(args)
  mon=smaputils.get_smap_monitor()

  prev=pickle.load('z1')
  timeval=mon
  pickle.dump('z1',timeval)

  #action
  if compareUpdate(prev,timeval):
    return True
  else:
    return False



# def handle_instruments():
#     read=su.curr_readings()
#     read_old=open('instruments.buf','rb').read()
#     res=compare_readings(read,read_old)
#     if res
#         return res
#         print 'readings good'
#     else:
#         restart_smap()
#         print 'readings bad'


def unable_to_connect():
  """
  Check for network connectivity.
  Notify
  """

  if ():
    return True
  else:
    return False


def disk_level():
  """

  flush,notify
  """

  d=diskmain()
  if d['space']:
    return True
  else:
    flush_smap_disk()

############ disk_level #########
def flush_smap_disk():
    ""
    remote=Remote()
    remote.execute('','/')

