from fabric.api import *
from fabric.context_managers import cd
from fabric.network import disconnect_all
from fabric.operations import *
from fabric.state import env
env.user="data"
env.password="data@best!"
env.hosts=['192.168.1.223']

class Buffered:
    def __init__(self, stream):
        self.stream = stream
        self.buf = []
    def write(self, data):
        self.buf.append(data)
        self.stream.write(data)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)



fp=os.pathname.basename(p_file)
p_remotefile=p_remote_file+'/'+fp

def move_file(p_file,p_remote_file):
    res = put(p_file,p_remote_file)
    return res.success