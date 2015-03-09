from fabfile import *
from fabric.context_managers import settings

with settings(host_string='debian@192.168.1.146'):
    res= hello("root")
    host_type()
    print is_smap_running()

    is_log_full()
    print get_disk()
    print get_version()
    print get_date()
    put_config_files()
    get_uptime()
    # put_dir('')


    with cd('/media/C062-FF78'):
        upload=put("ipcam.ini")

    print upload.succed

