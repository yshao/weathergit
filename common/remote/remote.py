import os
import re
from fabric.context_managers import cd, settings
from fabric.operations import put, get, run
from remoteexec import remote_exec

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/9/2015' '2:10 PM'

class Remote(object):
    def __init__(self,d,base):
        ""
        self.d=d
        self.upload('remote_api.py',base)

    def pexec(self,cmd,*args):
        ""
        d=self.d
        with settings(host_string=d['host_string'],password=d['password']):
            run('python remote_api.py %s %s' % (cmd,args))

    def upload(self,lFiles,dir):
        ""
        d=self.d
        l=[]
        with settings(host_string=d['host_string'],password=d['password']):
            with cd(dir):
                for f in lFiles:
                    res=put(f)
                    if res.success:
                        l.append()
        return l

    def download(self,lFiles,local):
        d=self.d
        l=[]
        with settings(host_string=['host_string'],password=d['password']):
            with cd(dir):
                for f in lFiles:
                    res=get(f)
                    if res.success:
                        l.append()
        return l

    def execute(self,cmd):
        with settings(host_string=['host_string'],password=d['password']):
            with cd(dir):
                run(cmd)

    def pexec(self,cmd):
        remote_exec()

    def ls(self):
        self.pexec("""
        import fileutils

        """
        )

    def move(self,):
        self.pexec(

        )


class Remote():
    def __init__(self,d):
        ""


    def ls(self):
        ""
        return ['111.jpg','222.jpg','333.png','12444.png','12443.png']

    def listfilter(self,l,regex):
        ""
        # l=self.ls()
        lFiles = [f for f in l if re.match(regex, f)]
        return lFiles

    def listByExt(self,l,ext):
        lFiles = [f for f in l if re.match(r'[0-9]+.*\.%s' % ext, f)]
        return lFiles

    def list_folders(self,path):
        ""
        dirs = [x[0] for x in os.walk(path)]
        dirs.pop(0)
        return dirs

    def filterByList(self,l1,l2):
        from fnmatch import fnmatch
        # l1 = ['test1', 'test2', 'test3', 'test4', 'test5']
        l2 = set(['*%s*'%e for e in l2])
        # l2 = set(['*t1*', '*t4*'])
        res=[x for x in l1 if any(fnmatch(x, p) for p in l2)]
        return res

    def mv(self,lFiles,dir):
        ""

    def rm(self,lFiles):
        ""

    def mkdir(self,dir):
        ""

    def cd(self,dir):
        ""

    def pexec(self):
        ""
    def cmd(self):
        ""

    def glob_files(self):
        ""