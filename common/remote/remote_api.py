from fabric.context_managers import settings
import psutil
from common.env import Env

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '2/25/2015' '1:50 PM'


env=Env()
cfg=env.getConfig()

print cfg

host='%s@%s' %(cfg['smap_server_username'],cfg['smap_server_host'])
pwd=cfg['smap_server_password']
print host,pwd

def get_scheduler_status():
    with settings(host_string='data@192.168.1.120',password='reverse'):
        p=psutil.Process()
        d= p.get_connections()

    return d


get_scheduler_status()