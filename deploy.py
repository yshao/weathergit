import tarfile
from fabric.operations import put, run
import os
import sys
from common.env import Env
from common.remote.remote import Remote

def untar_tarfile(fname):
    # if (fname.endswith("tar.gz")):
        tar = tarfile.open(fname)
        tar.extractall()
        tar.close()
        print "Extracted in Current Directory"
    # else:
    #     print "Not a tar.gz file: '%s '" % sys.argv[0]


def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

class DeployClient(object):
    def __init__(self):
        ""
        self.cfg=Env.get_config()

    def deploy_smap_server(self):
        ""
        host='%s@%s' % ("ubuntu","192.168.1.120")
        # print host
        pwd="reverse"
        d=dict(host_string=host,password=pwd)

        remote=Remote(d)
        remote.status()
        # print remote.execute("ls")

        ### deploy ###
        homep=Env().param['HOME']
        pkgDir='smapserver'
        indir=homep+'/'+pkgDir
        pkgFile='%s.tar.gz' % pkgDir
        make_tarfile(pkgFile,indir)
        remote.upload([pkgFile])
        remote.execute('tar -xf %s'%pkgFile)


    def deploy_smap_bbb(self):
        ""
        host='%s@%s' % ("ubuntu","192.168.1.120")
        # print host
        pwd="reverse"
        d=dict(host_string=host,password=pwd)

        remote=Remote(d)
        remote.status()
        # print remote.execute("ls")

        ### deploy ###
        homep=Env().param['HOME']
        pkgDir='smapource'
        indir=homep+'/'+pkgDir
        pkgFile='%s.tar.gz' % pkgDir
        make_tarfile(pkgFile,indir)
        remote.upload([pkgFile])
        remote.execute('tar -xf %s'%pkgFile)

if __name__ == '__main__':
        #TODO: change to config
        host='%s@%s' % ("ubuntu","192.168.1.120")
        print host
        pwd="reverse"
        d=dict(host_string=host,password=pwd)

        remote=Remote(d)
        remote.status()
        print remote.execute("ls")

        homep=Env().param['HOME']
        pkgDir='smapserver'
        indir=homep+'/'+pkgDir
        pkgFile='%s.tar.gz' % pkgDir
        make_tarfile(pkgFile,indir)
        remote.upload([pkgFile])
        remote.execute('tar -xf %s'%pkgFile)