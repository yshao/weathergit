from fabric.context_managers import cd
from fabric.operations import *
from fabric.state import env
env.user="data"
env.password="data@best!"
env.hosts=['192.168.1.223']

def move_file(filep):
    with cd("store/images"):
        upload=put(filep)

    # Verify the upload
    return upload.succeeded