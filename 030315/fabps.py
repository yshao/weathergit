__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/3/2015' '11:03 AM'

import psutil


def get_disk_partitions():
    ""
    return psutil.disk_partitions()

def get_stats():
    ""

def get_ps():
    ""

def get_net_connections():
    ""
    return psutil.net_connections()

def get_up_time():
    ""
    return psutil.boot_time()

def get_pids():
    ""
    return psutil.pids()

###
PROCNAME='python'

for proc in psutil.process_iter():
    if proc.name() == PROCNAME:
        print proc

print get_pids()

def start_webpage_server():
    ""
    if psutil.pid_exists():
        ''
    else:
        ''



def start_smap_bbb():
    ''
    if psutil.pid_exists():
        ''
    else:
        ''

def start_smap_trendnet():
    ''
    if psutil.pid_exists():
        ''
    else:
        ''

def get_smap_status():
    l=[]
    for p in psutil.pids():
        if p == 'smap_bbb':
            l.append(dict(smap_bbb='on'))
        else:
            l.append(dict(smap_bbb='off'))

        if p == 'smap_trendnet':
            l.append(dict(smap_trendet='on'))
        else:
            l.append(dict(smap_trendnet='off'))

    return l