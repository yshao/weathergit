import datetime

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/2/2015' '5:14 PM'

def frozen_measurements():
  """
  Check if encounters measurements not updating
  Restart
  """
  def convert_time():
      ""


  curr=convert_time([])
  if curr_measurements['time'] - datetime.dateime.now() > 5
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


def unable_to_read_status():
  """
  Check for network connectivity.
  Notify
  """

  if ():
    return True
  else
    return False


def disk_level():
  """

  flush,notify
  """

  d=show_disk()
  if d['space']:
    return True
  else:
    return False

############ disk_level #########
def flush_smap_disk():
    ""
    remote=Remote()
    remote.execute('','/')

