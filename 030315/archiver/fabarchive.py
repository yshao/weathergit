import os
from common.fileutils import list_files, list_files_ext
from common.utils import get_timestamp

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/3/2015' '10:35 AM'

import shutil as sl

def archive_files():
    ""
    def get_fidx():
        ""

    def get_idx_mock():
        ""
        p=os.curdir()
        return list_files_ext(p,'png')


    fidx=get_fidx_mock()


    curr_dt=get_timestamp()
    for f in fidx:
        sl.move(f,curr_dt)


p=os.getcwd()
print p



import os
import re

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