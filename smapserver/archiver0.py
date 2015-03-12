from fabric.context_managers import cd
from remote import Remote
import os
import re

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/3/2015' '10:35 AM'

import shutil as sl
import os
from common.fileutils import list_files_ext
from common.utils import get_timestamp
from fabric.operations import run, env
### operate from server to data server ###
def hostMove(files,tdir):
    run('mv %(files)s %(tdir)s' % files,tdir)

def hostMkdir(tdir):
    run('mkdir %(tdir)s' %tdir)

def hostListFiles(tdir_=None):
    """returns a list of files in a directory (dir_) as absolute paths"""

    dir_ = tdir_ or env.cwd
    with cd(dir_):
        string_ = run("for i in %s*; do echo $i; done" % dir_)
        lFiles = string_.replace("\r","").split("\n")

    return lFiles


def archive_files():
    ""
    def get_fidx():
        ""

    def get_idx_mock():
        ""
        p=os.curdir()
        return list_files_ext(p,'png')


    # fidx=get_fidx_mock()
    fidx=[]


    curr_dt=get_timestamp()
    for f in fidx:
        sl.move(f,curr_dt)

    tm=get_timestamp()
    remote=Remote(Remote.gen_login('dataserver'))
    remote.execute('mkdir %s'%tm)


# p=os.getcwd()
# print p
#

def grep(path, regex):
    regObj = re.compile(regex)
    res = []
    for root, dirs, fnames in os.walk(path):
        for fname in fnames:
            if regObj.match(fname):
                res.append(os.path.join(root, fname))
    return res

# print grep('.', r'my?(reg|ex)')



# print list_files_ext(p,'py')

