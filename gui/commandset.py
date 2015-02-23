import inspect
import datetime
import webbrowser
from weathergit.common.sysutils import run_command
from weathergit.common.fabutils import *

class CommandSet(object):
    def __init__(self):
        ""

        a=[]
        lis=inspect.getmembers(self, inspect.ismethod)
        for item in lis:
            a.append(item[0])

        self.cmdset=a
        # smap=SmapUtils()
        # fab=FabUtils()
        self.cmdset.remove('__init__')


    @classmethod
    def run(self,b):
        print b

    @classmethod
    def add(self,a,b):
        print a+b

    @classmethod
    def get_data(self):
        ""

    @classmethod
    def add_stream(self,csvfilep):
        ""
        # smap.load_csv(csvfilep)

    @classmethod
    def del_stream(self):
        ""
    @classmethod
    def show_streams(self):
        ""
    @classmethod
    def take_snapshot(self,outfilep):
        ""
        take_snapshot(outfilep)


    @classmethod
    def show_time(self):
        return show_time()

    @classmethod
    def get_snapshot_files(self,lFiles,localp):
        print "get files"
        get_snapshot_files(lFiles,localp)

    # @classmethod
    @classmethod
    def today(self):
        a = datetime.datetime.today()
        return a

    @classmethod
    def smap_connected(self):
        ""

    @classmethod
    def show_smap_stautus(self):
        ""
        res=show_smap_status()
        # res=run_command("ping 192.168.1.146")

        # res=res+run_command("ping 192.168.1.120")
        return res

    @classmethod
    def show_disk_size(self):
        ""
        res=show_disk_size()

        return res

    @classmethod
    def sync_time(self):
        ""

    @classmethod
    def open_cam(self):
        webbrowser.open ('http://192.168.1.121')
        'http://192.168.1.121/doc/page/home_basic.asp?1421084323538'

    # @classmethod
