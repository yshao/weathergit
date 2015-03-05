from fabric.context_managers import settings
from fabric.operations import put, run
import psutil


def run_remote(lam):
    with settings(host_string='data@192.168.1.120',password='reverse'):
        put('remote_api.py')
        run('python remote_api.py l%s'%lam)



from remote_api import get_scheduler_status

run_remote('get_scheduler_status')

