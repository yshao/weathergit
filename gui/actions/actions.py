from time import sleep
import unittest
from PyQt4 import QtGui
import inspect
from PyQt4.QtCore import QThread, QObject, QThreadPool
import sys
from PyQt4.QtGui import QApplication

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '1/19/2015' '2:42 PM'

# command=Command()

def log(logger):
    ""
    logger.log()

    logger.log()


class TaskThread(QThread):
    ""
    def __init__(self,parser):
        ""
        tid=self.currentThreadId()


    @log
    def run(self):
        ""


#TODO: add xlwings API methods here
def save_to_file():
    ""

class Handler(QObject):
    ""


class datawidgetHandler(Handler):
    def __init__(self):
        ""



    def on_download_data(win):

        params=win.getGuiData()
        sql = "select data %s %s where uuid like ''"
        return sql



class test_handler(unittest.TestCase,datawidgetHandler):
    ""
    def setUp(self):
        ""
        self.data={
            'start_time':1,
            'end_time':2,
            'stream_limit':1,
            'paths':['']
        }
        # win=DataWidget()


    def test_on_download_data(self):
        assert self.on_download_data(self.data) == 'select data 1 2 streamlimit 1 where uuid like '1''

def download_data(sql):

    print(inspect.stack()[0][0].f_code.co_name)
    print(inspect.stack()[0][3])
    print(inspect.currentframe().f_code.co_name)
    # print(sys._getframe().f_code.co_name)

    mname=inspect.currentframe().f_code.co_name


    # logger.log(" : ".join[mname,tid,"start"])
    # q=TaskThread(command.run())
    # mon.connect(q.started)
    # q.run()
    # logger.log(" : ".join[mname,tid,"result",res])



# @log
# def open_window():
#     ""
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mon = QThreadPool.globalInstance()
    print mon.activeThreadCount()

    sys.exit(app.exec_())




