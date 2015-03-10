import tarfile
from fabric.operations import put, run
import os
import sys
from common.env import Env
from common.remote import Remote

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

        # cfg['smap_bbb_ip']
        # cfg['smap_bbb_pwd']
        #
        # cfg['webserver_ip']
        # cfg['webserver_pwd']

class DeployClient(object):
    def __init__(self):
        ""
        self.cfg=Env.get_config()

    def deploy_smap_server(self):
        ""
        cfg=self.cfg
        host='%s@%s' % (cfg['smap_server_username'],cfg['smap_server_host'])
        pwd=cfg['smap_server_pwd']
        d=dict(host_string=host,password=pwd)
        remote=Remote(d)

        indir='smapserver'
        pkg='server.tar.gz'
        make_tarfile(pkg,indir)

        remote.upload(pkg)
        run('tar -xf -C %s'%pkg)


    def deploy_smap_bbb(self):
        ""
        cfg=self.cfg
        host='%s@%s' % (cfg['smap_source_username'],cfg['smap_source_host'])
        pwd=cfg['smap_source_pwd']
        d=dict(host_string=host,password=pwd)
        remote=Remote(d)

        indir='smapsource'
        pkg='smapbbb.tar.gz'
        make_tarfile(pkg,indir)

        remote.upload_files(pkg)
        run('tar -xf %s'%pkg)

class WClient()