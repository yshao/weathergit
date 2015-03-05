import datetime

def hostListFolders():
    ""

def get_latest_folder():
    ""
    folders=hostListFolders()
    # folders=[]
    return max(folders)


def archive_files():
    agent=Archiver()
    st=get_latest_folder()
    end=datetime.datetime.now()
    agent.batch_store_files(st,end)

class Archiver(object):
    ""
    def __init__(self):
        ""



def get_zip_name(startdt,enddt):
    fmt='%Y/%m/%d %H:%M:%S %p'
    st=datetime.datetime.strptime(startdt,fmt)
    end=datetime.datetime.strptime(enddt,fmt)

    zip_fmt='%Y%m%d%H%M%S'

    sst=datetime.datetime.strftime(st,zip_fmt)
    send=datetime.datetime.strftime(end,zip_fmt)

    zip_filep='%s_%s' % (sst,send)

    # grp=retr_file_groups(st,end)

    lFiles=[]
    # for g in grp:
    #     for e in g:
    #         lFiles.append(e)


    # zip_file(zip_filep,lFiles)
    #
    # ###
    # move(zip_filep,dest_filep)

def zip_file(fname,lFiles):
    ""

def unzip_file(fname,targetp):
    ""


def move_file(src,dest):
    ""

st='2015/03/03 12:00:00 AM'
ed='2015/03/04 12:00:00 AM'

lFiles=['retr_stats.py']

dest_filep='test.tar.gz'
print get_zip_name(st,ed)

def batch_retr_files(st,end,destFilep):
    ""

    zipFilep=get_zip_name(st,end)
    unzip_file(zipFilep)
    move_file(zipFilep,destFilep)


def batch_store_files(st,end):
    destFilep=''
    zipFilep=get_zip_name(st,end)

    zip_file(zipFilep)

    move_file(zipFilep,destFilep)

# print datetime.time.mktime(datetime.datetime.now().timetuple()) * 1000