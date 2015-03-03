#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time

from PyQt4 import QtCore, QtGui

class timerThread(QtCore.QThread):
    timeElapsed = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super(timerThread, self).__init__(parent)
        self.timeStart = None

    def start(self, timeStart):
        self.timeStart = timeStart

        return super(timerThread, self).start()

    def run(self):
        while self.parent().isRunning():
            self.timeElapsed.emit(time.time() - self.timeStart)
            time.sleep(1)


class myThread(QtCore.QThread):
    timeElapsed = QtCore.pyqtSignal(int)
    def __init__(self, parent=None):
        super(myThread, self).__init__(parent)

        self.timerThread = timerThread(self)
        self.timerThread.timeElapsed.connect(self.timeElapsed.emit)

    def run(self):
        self.timerThread.start(time.time())

        iterations = 3
        while iterations:
            print "Running {0}".format(self.__class__.__name__)
            iterations -= 1
            time.sleep(2)        


class myWindow(QtGui.QWidget):    
    def __init__(self):
        super(myWindow, self).__init__() 

        self.button = QtGui.QPushButton(self)
        self.button.setText("Start Threading!")
        self.button.clicked.connect(self.on_button_clicked)

        self.label = QtGui.QLabel(self)

        self.layout = QtGui.QVBoxLayout(self)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)

        self.myThread = myThread(self)
        self.myThread.timeElapsed.connect(self.on_myThread_timeElapsed)
        self.myThread.finished.connect(self.on_myThread_finished)

    @QtCore.pyqtSlot()
    def on_button_clicked(self):
        self.myThread.start()

    @QtCore.pyqtSlot(int)
    def on_myThread_timeElapsed(self, seconds):
        self.label.setText("Time Elapsed: {0}".format(seconds))

    @QtCore.pyqtSlot()
    def on_myThread_finished(self):
        print "Done"

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('myWindow')

    main = myWindow()
    main.show()

    sys.exit(app.exec_())