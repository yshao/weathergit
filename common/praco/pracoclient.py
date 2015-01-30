__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '1/28/2015' '10:58 AM'


import configparser

class TelnetClient():
    ""
    def __init__(self):
        ""

class ConfigIni():
    def __init__(self,filep):
        ""
        parser=configparser.ConfigParser()
        self.config=parser.read(filep)

    def __getattr__(self, item):
        return self.config(item[0],item[1])


class FileClient(object):
    def __init__(self):
        ""
        self.config=ConfigIni('praco.ini')
        self.fc=TelnetClient()

    def enable_filesync(self):
        ""
        self.syncEnabled=True


    def is_filsync_running(self):
        ""
        return self.syncEnabled


    def get_status(self):
        d={}
        d['filesync']=self.syncEnabled
        d['num_files_remaining']=self.fc.send("list")
        d['num_files_moved']=self.fileCount
        return d


    @pyqtSlot()
    def handle_moved(self,msg):
        ""
        def parse(msg):
            ""


        files_moved = parse(msg)
        self.fileCount += files_moved
        print msg



class PracoClient(object):
    def __init__(self):
        ""
        self.fc=FileClient()

    def send(self,cmd):
        if cmd == "":
            ""
        elif cmd == "":
            ""