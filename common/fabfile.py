from functools import wraps
from fabric.api import *
from fabric.context_managers import cd
from fabric.network import disconnect_all
from fabric.operations import *
from fabric.state import env
env.user="debian"
env.password="temppwd"
env.hosts=['192.168.1.146']
# env.user="hngv.password"="password"
# env.parallel=True


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

def auto_comment(func):
    @wraps(func)
    def wraper(*args, **kws):
        _stdout = sys.stdout
        buffered = sys.stdout = Buffered(_stdout)
        ret = func(*args, **kws)
        if buffered.buf:
            # only pick last 500 lines is good enough
            echo_result = "".join(buffered.buf[-500:])
            # filter the colored results
            echo_result = re.sub("\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]", "", echo_result)
            # using the result as you want
        sys.stdout = _stdout
        return ret
    return wraper

@auto_comment
def hello(who="world"):
   print "Hello {who}!".format(who=who)
   print("Executing on %s as %s" % (env.host, env.user))

SMAP_SOURCE_DISK_MAX=100
def get_version():
    res=run("cat /proc/version")
    return res

def get_server_disk():
    res=run("df -h | grep sda1")
    return res

def get_date():
    res=run("date '+%D %T'")
    return res

def get_disk():
    res=run("df -h | grep rootfs")
    return res

def is_log_full():
    res=sudo('du -hx --max-depth=1 /var/log | grep M')
    pat=re.compile('[0-9]*M')
    if int(pat.findall(res)[0].rstrip('M')) > SMAP_SOURCE_DISK_MAX:
        return True
    else:
        return False

def _get_smap_id():
    with settings(warning_only=True):
        try:
            res=run("pgrep twistd")
            if res.return_code != 0:
                return False
            else:
                return int(res)
        except:
            return False

def is_smap_running():
    if _get_smap_id() != False:
        return True

def restart_smap():
    if is_smap_running():
        pid=_get_smap_id()
        sudo('kill %i' % pid)

    with settings(warning_only=True):
        with cd('Desktop/weather/common'):
            res=sudo('twistd -n smap weather.ini')
            print res



def get_server_id():
    """"""
    with settings(warning_only=True):
        res=run("pgrep twistd")
        if res.return_code != 0:
            return False
        else:
            return res

def is_camera_running():
    """"""
    res=run("pgrep twistd")


def put_config_files():
    with cd("Desktop/weather/"):
        upload=put("ipcam.ini")

    # Verify the upload
    return upload.succeeded

def run_smap():
    if not is_smap_running():
        run('./home/debian/Desktop/weather')


def host_type():
    run('uname -s')


def get_uptime():
    res = run('cat /proc/uptime')
    print res

# def combo():
#     host_type()
#     list()
#     get_logs()

# Download some logs
def get_smap_config():
    get(remote_path="/home/debian/Desktop/weather/common/weather.ini", local_path="c:/tests")


# The *cd* context manager makes enwrapped command's
# execution relative to the stated path (i.e. "/tmp/trunk")
def list():
    with cd("/tmp"):
        items = sudo("ls -l")

def disconnect():
    disconnect_all()


# @roles('webserver')
@parallel
def pcmd(cmd):
    run(cmd)


