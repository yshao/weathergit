from time import sleep
import unittest
from PyQt4.QtGui import QApplication
import sys

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '1/21/2015' '9:53 AM'

class Test_TaskThread(unittest.TestCase):
    ""
    def setUp(self):
        ""
        self.app = QApplication(sys.argv)

    def run(self):

        return ("Ok",0,0)

    def example(self):
        sleep(5)
        print "DONE"
        self.emit('DONE')
        return


    def test_run(self):
        self.assertEquals()