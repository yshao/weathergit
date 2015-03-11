import re
import tarfile
from fabric.operations import put, run
import os
import sys
from common.env import Env
from common.remote.remote import Remote

def extract_tarfile(fname):
    # if (fname.endswith("tar.gz")):
        tar = tarfile.open(fname)
        tar.extractall()
        tar.close()
        print "Extracted in Current Directory"
    # else:
    #     print "Not a tar.gz file: '%s '" % sys.argv[0]


def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

class DeployClient(object):
    def __init__(self):
        ""
        self.cfg=Env().getConfig()

    def deploy_smap_server(self):
        ""
        d=self.cfg
        host='%s@%s' % (d["smap_server_username"],d["smap_server_host"])
        # print host
        pwd=d['smap_server_password']
        base_dir='smapserver'
        d=dict(host_string=host,password=pwd,base_dir=base_dir)

        remote=Remote(d)

        ### deploy ###
        homep=Env().param['HOME']
        pkgDir='smapserver'
        indir=homep+'/'+pkgDir
        pkgFile='%s.tar.gz' % pkgDir

        print homep,pkgDir,indir,pkgFile

        make_tarfile(pkgFile,indir)
        remote.upload([pkgFile])
        remote.execute('tar -xf %s'%pkgFile)


    def deploy_smap_source(self):
        ""
        d=self.cfg
        host='%s@%s' % (d["smap_source_username"],d["smap_source_host"])
        # print host
        pwd=d['smap_source_password']
        base_dir='smapsource'

        d=dict(host_string=host,password=pwd,base_dir=base_dir)

        remote=Remote(d)

        ### deploy ###
        homep=Env().param['HOME']
        pkgDir='smapsource'
        indir=homep+'/'+pkgDir
        pkgFile='%s.tar.gz' % pkgDir
        make_tarfile(pkgFile,indir)
        remote.upload([pkgFile])
        remote.execute('tar -xf %s'%pkgFile)

    def deploy_webserver(self):
        d=self.cfg
        host='%s@%s' % (d["smap_server_username"],d["smap_server_host"])
        # print host
        pwd=d['smap_server_password']
        base_dir='webserver'
        d=dict(host_string=host,password=pwd,base_dir=base_dir)

        remote=Remote(d)

        ### deploy ###
        homep=Env().param['HOME']
        pkgDir='webserver'
        indir=homep+'/'+pkgDir
        pkgFile='%s.tar.gz' % pkgDir
        make_tarfile(pkgFile,indir)
        remote.upload([pkgFile])
        remote.execute('tar -xf %s'%pkgFile)


    def run_webserver(self):
        ""
        d=self.cfg
        host='%s@%s' % (d["smap_server_username"],d["smap_server_host"])
        # print host
        pwd=d['smap_server_password']
        base_dir='smapserver'
        d=dict(host_string=host,password=pwd,base_dir=base_dir)

        remote=Remote(d)
        # remote.status()
        res=remote.pexec('start_daemon',['scheduler'])

    def run_scheduler(self):
        ""
        d=self.cfg
        host='%s@%s' % (d["smap_server_username"],d["smap_server_host"])
        # print host
        pwd=d['smap_server_password']
        base_dir='smapserver'
        d=dict(host_string=host,password=pwd,base_dir=base_dir)

        remote=Remote(d)
        # remote.status()
        res=remote.pexec('start_daemon',['scheduler'])


if __name__ == '__main__':
        ## init remote
        d=Env().getConfig()
        host='%s@%s' % (d["smap_server_username"],d["smap_server_host"])
        pwd=d['smap_server_password']
        base_dir='smapserver'
        d=dict(host_string=host,password=pwd,base_dir=base_dir)
        print 'test',d

        remote=Remote(d)

        #deploy projects
        c=DeployClient()
        c.deploy_smap_server()
        c.deploy_webserver()
        c.deploy_smap_source()


