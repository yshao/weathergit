#!/usr/bin/python
'''Test cases for QThread'''

import unittest
from PyQt4.QtCore import QThread, QCoreApplication, QObject, SIGNAL, QMutex, QTimer
from PyQt4.QtCore import QEventLoop

# from helper import UsesQCoreApplication
from PyQt4.QtGui import QApplication
import sys

mutex = QMutex()

class Dummy(QThread):
    '''Dummy thread'''
    def __init__(self, *args):
        super(Dummy, self).__init__(*args)
        self.called = False

    def run(self):
        #Start-quit sequence
        mutex.lock()
        self.called = True
        mutex.unlock()

class QThreadSimpleCase(unittest.TestCase):

    def setUp(self):
        self.app = QApplication(sys.argv)
        # UsesQCoreApplication.setUp(self)
        self.called = False

    # def tearDown(self):
        # UsesQCoreApplication.tearDown(self)

    def testThread(self):
        #Basic QThread test
        obj = Dummy()
        obj.start()
        obj.wait()

        self.assert_(obj.called)

    def cb(self, *args):
        self.called = True
        #self.exit_app_cb()

    def abort_application(self):
        self._thread.terminate()
        self.app.quit()

    def testSignalFinished(self):
        #QThread.finished() (signal)
        obj = Dummy()
        QObject.connect(obj, SIGNAL('finished()'), self.cb)
        mutex.lock()
        obj.start()
        mutex.unlock()

        self._thread = obj
        QTimer.singleShot(1000, self.abort_application)
        self.app.exec_()

        self.assert_(self.called)

    def testSignalStarted(self):
        #QThread.started() (signal)
        obj = Dummy()
        QObject.connect(obj, SIGNAL('started()'), self.cb)
        obj.start()

        self._thread = obj
        QTimer.singleShot(1000, self.abort_application)
        self.app.exec_()

        self.assert_(self.called)

if __name__ == '__main__':
    unittest.main()