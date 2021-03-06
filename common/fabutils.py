from weathergit.common.utils import get_timestamp
from fabfile import *
from fabric.context_managers import settings

__author__ = 'Ping'

def get_status():
    """

    :return:
    """

def show_smap_status():
    """


    :return: dict
    """

    def parse(lines):
        d={}
        for ln in lines:
           d['abc']='abc'



        return d

    out=[]
    with settings(host_string='debian@192.168.1.146'):
        out.append(get_uptime())
        out.append(get_version())



    with settings(host_string='ubuntu@192.168.1.120',password='reverse'):
        out.append(get_uptime())
        out.append(get_version())

    print out


    # res=parse(out)
    return out

def show_disk_size():
    out=[]
    with settings(host_string='debian@192.168.1.146'):
        out.append(get_disk())

    with settings(host_string='ubuntu@192.168.1.120',password='reverse'):
        out.append(get_server_disk())

    return out

def smap_connected():
    ""

def show_time():
    ""
    out=[]
    with settings(host_string='debian@192.168.1.146'):
        out.append(get_time())

    with settings(host_string='ubuntu@192.168.1.120',password='reverse'):
        out.append(get_time())

    out.append(get_timestamp())

    return out


def sync_time():
    ""

def take_snapshot(outfilep):
    ""
    def parse():
        ""

    out=[]

    with settings(host_string='ubuntu@192.168.1.120',password='reverse'):
        out.append(ipcam_take_snapshot(outfilep))


    d=out

    return d


def get_snapshot_files(lfile_idx,localp):
    with settings(host_string='data@192.168.1.223',password='data@best!'):
        # out.append(get_time())

        with cd("/home/data"):
            upload=get(lfile_idx,localp)

        # Verify the upload
        return upload.succeeded





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

### insert snapshot

# INSERT INTO app(p_id, the_geom)
# VALUES(2, ST_GeomFromText('POINT(-71.060316 48.432044)', 4326));
# config=dict(hostname=,password=,dbname=,)
# conn=DbConn()
# cur = conn.cursor()
# cur.executemany("""INSERT INTO bar(first_name,last_name) VALUES (%(first_name)s, %(last_name)s)""", namedict)
### check storage is getting snapshots
#query(time)

#sv.get_data()[0]
#header == 'recent'


### check disp is running with gps and cam updates

### cam.sig.

if __name__ == '__main__':
    ""
    # with settings(host_string='ubuntu@192.168.1.120',password='reverse'):
    #     print get_server_disk()
    #     print take_snapshot("11111111.png")
    #
    # with settings(host_string='data@192.168.1.223',password='data@best!'):
    #     get_snapshot_files('11111111.png','c:/images')

    #test snapshot
    # take_snapshot("11111111.png")
    # get_snapshot_files('11111111.png','c:/images')