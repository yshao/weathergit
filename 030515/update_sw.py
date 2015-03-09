### edit files ###
### instructions ###

###
from functools import wraps
import marshal
import pickle
from fabric.decorators import task
import psutil
from remoteexec import remote_exec

config=JsonConfig('')
###
def update_server_sw():
    ""
    with host=cf['smap_server_ip'],password=cf['smap_server_pwd']:


def update_bbb_sw():
    ""
    with host=cf['smap_bbb_ip'],password=cf['smap_bbb_pwd']:
        with cd()
            put
            run('unzip ')


def run_scheduler():
    ""
    smap()

    def start_bbb_smap():
        ""
        fabps_

    def start_ip_smap():
        ""

    def stop_bbb_smap():
        ""

###fabps###


from fabric.operations import _execute, run


# def rpc(f):
#     @wraps(f)
#     def wrapper(*l, **kw):
#         c = 'python -c "import marshal,pickle,types;types.FunctionType(marshal.loads(%r),globals(),%r)(*pickle.loads(%r),**pickle.loads(%r))"'
#         c = c % (marshal.dumps(f.func_code),f.func_name,pickle.dumps(l),pickle.dumps(kw))
#         run(c)
#     return wrapper
#
#
# @task
# @rpc
# def check_pid(f):
#     print 'new f%s' %f

# def copy_fabps_if_not():
#     ""
#
# def Remote_check_pid():
#     copy_fabps_if_not()
#     check_pid()


def handle_webgen():
    ""
    remote_exec(
        """
        from webgenutils import gen_web
        gen_web()
        """
    )


def smap_bbb():
    ""

def smap_server():
    ""

@smap_server
def check_pid(cfg):
    ""
    remote_exec(cfg['host'],cfg['password'],
    """
     import sys, os
     import psutil
     p=psutil.Process()
     p.get_pids()
""")

def check_disk_status(cfg):
    ""
    remote_exec(cfg['host'],cfg['password'],
    """
     import sys, os
     channel.send((sys.platform, tuple(sys.version_info), os.getpid()))
""")

@smap_server
def start_smap():
    ""


def handle_connect():
    ""
    cfg=Env.getConfig()
    pingparser(cfg['smap_server_ip'])
    pingparser(cfg['smap_bbb_ip'])
    pingparser(cfg['smap_data_server_ip'])
    dbconn.status()
    urlopen(cfg['smap_server_backend'])
    urlopen(cfg['smap_bbb_monitor'])

def handle_smap_bbb_disk():
    ""
    cfg=Env.getConfig()
    remote_exec(cfg['host'],cfg['password'],
    """
    import fileutils
    rm_dir()
""")


def handle_instruments():
    read=su.curr_readings()
    read_old=open('instruments.buf','rb').read()
    res=compare_readings(read,read_old)
    if res
        return res
        print 'readings good'
    else:
        restart_smap()
        print 'readings bad'


def handle_daemon():
    res=check_pid(dict(host=config[''],password=config['']))
    if res:
        return res
        print "daemon good"
    else:
        restart_daemon()
        print "daemon restarted"



def check_smap_status():
    ""

### actions ###
def restart_daemon():
    ""

def restart_smap():
    ""

###
