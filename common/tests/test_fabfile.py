import re
import requests
from weathergit.common.fabfile import *
from fabric.context_managers import settings

__author__ = 'Ping'


with settings(host_string='debian@192.168.1.146',password='temppwd'):
    get_smap_config()


with settings(host_string='ubuntu@192.168.1.120',password='reverse'):
    # list()
    rdb_query("select *")

### restart smap
# with settings(host_string='debian@192.168.1.146'):
#     restart_smap()


### check html returns has monitor running X
# r=requests.get("http://192.168.1.146:8079/data")
#
# pat=re.compile('BEST')
# if r.status_code == 200:
#     print r.text
#     res=pat.findall(r.text)
#     assert res[0] == 'BEST'





### check df -h on smap source
# with settings(host_string='debian@192.168.1.146'):
#     res= hello("root")
#     host_type()
#     print is_smap_running()
#
#     is_log_full()
#     print get_disk()
#     print get_version()
#     print get_date()
#     put_config_files()
#     uptime()




### pygui logs serial logger running SKIP


### open smap souce for cam


### run query through rdb
# with settings(host_string='ubuntu@192.168.1.120',password='reverse'):
#     res= hello("server")
#     host_type()
#     # print is_smap_running()
#
#     # is_log_full()
#     print get_server_disk()
#     print get_version()
#     print get_date()
#     put_config_files()
#     uptime()

