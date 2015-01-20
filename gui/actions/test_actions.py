# This is only needed for Python v2 but is harmless for Python v3.
import sip
sip.setapi('QString', 2)

from time import sleep
import unittest
from PyQt4.QtCore import QThread, QThreadPool
from PyQt4.QtGui import QApplication
import sys

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '1/19/2015' '4:39 PM'


class TaskThread(QThread):
    ""
    def __init__(self,parser):
        ""
        super(TaskThread, self).__init__()
        tid=self.currentThreadId()


    # @log
    def run(self):
        ""

class Test_actions(unittest.TestCase):
    ""
    def setUp(self):
        ""
        self.app = QApplication(sys.argv)


    def example(self):
        sleep(5)
        print "DONE"
        self.emit('DONE')
        return

    # def test_console(self):
    #     ""
    #     console.commandset == ['']

    def test_taskThread(self):
        ""
        def parse():
            ""

        q=QThread()
        q.start()
        print q.started()# assert

        mon = QThreadPool.globalInstance()
        print mon.activeThreadCount()
        # assert mon.activeThreadCount() == 1

