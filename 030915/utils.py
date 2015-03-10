import re
import time
import datetime
from remoteexec import remote_exec, os
from common.utils import get_timestamp

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/9/2015' '11:21 AM'

def tm_to_epoch(dt):
    pattern='%Y%m%d %H:%M:%S %p'
    # tm=time.strptime(,dt)
    epoch = int(time.mktime(time.strptime(dt, pattern)))
    return epoch


def get_localtime():
    # print datetime.datetime.now()
    tm=datetime.datetime.now().timetuple()
    return time.strftime("%Y%m%d %H:%M:%S %p",tm)

def day_now():
    tm=datetime.datetime.now().timetuple()
    # time.struct_time
    # tm.tm_hour=0
    # tm.tm_min=0
    # tm.tm_sec=0
    return time.strftime("%Y%m%d %H:%M:%S %p",tm)

def day_before():
    d=datetime.datetime.now() - datetime.timedelta(days=1)
    tm=d.timetuple()
    return time.strftime("%Y%m%d %H:%M:%S %p",tm)

tmp=get_localtime()
# print tmp
tm_to_epoch(tmp)

if __name__ == '__main__':
    print tm_to_epoch('20150309 12:00:00 AM')
    print tm_to_epoch('20150308 12:00:00 AM')
    print tm_to_epoch('20150305 12:00:00 AM')
    print tm_to_epoch('20150304 12:00:00 AM')
    print tm_to_epoch('20150303 12:00:00 AM')
    print tm_to_epoch('20150302 12:00:00 AM')
    print tm_to_epoch('20150301 12:00:00 AM')
    print tm_to_epoch('20150227 12:00:00 AM')

def get_file_index():
    print day_now()
    print day_before()


def create_folder():
    tm=tm_to_epoch(get_localtime())
    # remote_exec()
    #TODO: (mkdir %s) % tm
    # l=remote.list_flies()

    remote=Remote()
    l=remote.ls()
    l=remote.listByExt(l,'png')
    # print remote.list_folders('.')
    # fIndex=get_file_index()
    fIndex=['12444']

    # print l
    l=remote.filterByList(l,fIndex)
    # print l
    # print remote.listfilter(l,r'12[0-9]+.*\.')
    print l

create_folder()
get_file_index()
d = datetime.datetime.now() - datetime.timedelta(days=1)

print datetime.date.today()

# time.struct_time()
d=datetime.date.today() - datetime.timedelta(days=1)

#today
print tm_to_epoch(datetime.date.today().strftime('%Y%m%d %H:%M:%S %p'))
print tm_to_epoch(d.strftime('%Y%m%d %H:%M:%S %p'))

# create folder
# create range
# get file index
# move files

def get_timerange_lFils(st,et):
    # stm=tm_to_epoch(st)
    # etm=tm_to_epoch(et)
    # list_folders
    stm=st
    etm=et
    lFolders=['100','123','145','200','300']
    folders = [f for f
                   in lFolders
                   if int(stm) <= int(f) <= int(etm)
                  ]

    ### finds the nearest future folder of the st and end index
    folders.sort()
    lastidx=folders[-1]
    lastFolder=lFolders.index(lastidx) + 1
    folders.pop(0)
    folders.append(lFolders[lastFolder])
    print folders

    ### get files and filter by list ###
    lFiles=[]
    for f in folders:
        lFiles+=list_files(f)

    lFileIndex=[]
    remote=Remote()
    remote.filterByList(lFiles,lFileIndex)

get_timerange_lFils('111','190')

#get files