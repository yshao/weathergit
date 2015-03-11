import datetime
from common.env import Env
from common.event.supervisory import Supervisory
from common.remote.remote import Remote
from common.smaputils import SmapUtils
from disk_usage import diskmain
from actions.notify import send_event_email
from smapserver.sysutils import run_command

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

cfg=Env().getConfig()

def update_status():
    txt1='\n'.join(diskmain())

    super=Supervisory()
    txt2='\n'.join((super.get_all_pids()))

    content='\n'.join([txt1,txt2])
    send_event_email(content)


def watchdog():
    ### check network is up ###
    if not check_network():
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

    ### check for frozen instruments ###
    # d=find_frozen_measurements()
    #     ""
    #
    # ### check disk level ###
    # if disk_level():
    #     flush_smap_disk()
    #     send_event_email('Disk buffer flushed')

    ### send report ###
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

### check actions ###
def check_network():
    def is_connected(d):
        if 'Unreachable' in d or 'unreachable' in d:
            return False
        else:
            return True

    l=[cfg['smap_server_host'],cfg['smap_source_host'],cfg['data_server_host']]
    for link in l:
        d=run_command('ping %s' % link)
        is_connected(d)


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

