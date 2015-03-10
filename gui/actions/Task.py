from PyQt4.QtCore import QThread, pyqtSlot

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '2/3/2015' '12:37 PM'

import multiprocessing as mp



class Task(QThread,mp.Process):
    def __init__(self):
        ""



    def run(self):
        ""
        def parse():
            ""

        res=""

        return res


class TaskImpl(Task):
    @pyqtSlot(msg)
    def run(self):
        ""

        def parse():
            res= self._get_return(msg)




        return res


    def _get_return(msg):
        ""
        t=()
        t.append(msg)
        return t


class TestTask(TaskImpl):
    ""

class FabricTask(TaskImpl):
    ""

class ShellTask(TaskImpl):
    ""

class SmapUtilTask(TaskImpl):
    ""

class ConnTask(TaskImpl):
    ""

class OperatorTask(TaskImpl):
    ""

class FtpTask(TaskImpl):
    ""

    def run(self):
        ""


ftask=Task(run=fc.client.fetch,params=())

pyqtSlot()
guiUpdate(get_data())