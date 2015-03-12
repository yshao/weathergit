import datetime
from common.smaputils import SmapUtils
from remote import Remote

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/11/2015' '6:10 PM'

def archive_pngs():
    ""
    ""
    # def get_fidx():
    #     ""
    #
    # def get_idx_mock():
    #     ""
    #     p=os.curdir()
    #     return list_files_ext(p,'png')
    #

    # fidx=get_fidx_mock()
    # fidx=[]


    # curr_dt=get_timestamp()
    # for f in fidx:
    #     sl.move(f,curr_dt)

    tm=get_current_time()
    remote=Remote(Remote.gen_login('dataserver'))
    remote.execute('mkdir %s'%tm)

def get_current_time():
    import time
    su=SmapUtils()
    d=su.get_smap_time_dict('trendnet.ini')
    tm=d['/trendnet0/time']
    date_str=tm
    # print date_str
    nd=date_str[0:-6]
    td=date_str[-5:]
    naive_dt = datetime.datetime.strptime(nd, '%Y-%m-%dT%H:%M:%S')
    mea_tm= time.mktime(naive_dt.timetuple())
    print mea_tm

if __name__ == '__main__':
    get_current_time()