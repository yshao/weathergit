import inspect
from PyQt4.QtCore import QThread, QObject

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '1/19/2015' '2:42 PM'

command=Command()

def log(logger):
    ""
    logger.log()

    logger.log()



def show_running_threads():
    ""


class ThreadMon(QObject):
    ""

class TaskThread(QThread):
    ""
    def __init__(self,parser):
        ""
        tid=self.currentThreadId()


    @log
    def run():
        ""


mon=ThreadMon()

def download_data(sql):
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


