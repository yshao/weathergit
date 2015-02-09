from PyQt4 import QtGui


### logs status
from PyQt4.QtCore import pyqtSlot

import logging


class LoggerWidget(QtGui.QTextBrowser):
    def __init__(self,parent=None):
        super(LoggerWidget, self).__init__(parent)

        self.logger=logging.getLogger()


        # self.logger=logger()
        #
        # self.connect(SIGNAL=,self.print)

    @pyqtSlot(str)
    def update(self):
        ""
        self.log

    def finish(self):
        ""

    def start(self):
        ""

