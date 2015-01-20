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

command=Command()

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




def download_data(sql):

    params=win.getGuiData()
    sql = "select data %s %s where uuid like ''"

    print(inspect.stack()[0][0].f_code.co_name)
    print(inspect.stack()[0][3])
    print(inspect.currentframe().f_code.co_name)
    # print(sys._getframe().f_code.co_name)

    mname=inspect.currentframe().f_code.co_name


    logger.log(" : ".join[mname,tid,"start"])
    q=TaskThread(command.run())
    mon.connect(q.started)
    q.run()
    logger.log(" : ".join[mname,tid,"result",res])

# @log
# def open_window():
#     ""
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mon = QThreadPool.globalInstance()
    print mon.activeThreadCount()

    sys.exit(app.exec_())




