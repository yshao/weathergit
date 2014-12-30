from common.config import Config
from common.sourceclient import SourceClient


def update_status():
    ""

# class SourceClient(object):


COMMAND=dict(CMD_RESTART="shutdown -r now",CMD_DATE="date '+%D %T'",CMD_DISKSPACE="df -h | grep rootfs")

COMMAND=dict()

config=Config("weatherplotter.conf")
login=dict(hostname=config['smap_source_host'], key_filename=config['smap_source_keyfile'],
           username=config['smap_source_user'],password=config['smap_source_password'])

sc=SourceClient(login)
res=sc.send("smap-tool -l http://localhost:8079")

for ln in res:
    print ln

res=sc.send("df -h")

for ln in res:
    print ln


### restart twist
res=sc.send("pgrep twistd")
pid=0
for ln in res:
    i=int(ln)


sc.send('kill %i' % pid)

sc.send('twistd -n smap weather.ini')



### update config
sc.connectSFTP()

sc.get("")
sc.put()

### get raw files
