__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '1/19/2015' '4:39 PM'

from time import sleep
import unittest
from PyQt4.QtCore import QThread, QThreadPool
from PyQt4.QtGui import QApplication
import sys


class TaskThread(QThread):
    ""
    def __init__(self,parser):
        ""
        tid=self.currentThreadId()


    @log
    def run(self):
        ""

class Test_actions(unittest.TestCase):
    ""
    def setUp(self):
        ""
        self.app = QApplication(sys.argv)
        mon = QThreadPool.globalInstance()

    def example(self):
        sleep(5)
        return

    # def test_console(self):
    #     ""
    #     console.commandset == ['']

    def test_taskThread(self):
        ""
        q=TaskThread()
        q.run(self.example)
        assert