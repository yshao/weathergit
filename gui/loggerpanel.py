#!/usr/bin/env python
import sip
sip.setapi('QString', 2)
from gui.ui.ui_loggerpanel import Ui_loggerpanel



import json

from PyQt4 import QtGui,QtCore
import sys

# number of data points
from PyQt4.QtCore import QTimer, pyqtSignal
# from weathergit.gui.ui.ui_loggerpanel import Ui_loggerpanel
from weathergit.gui.commandconsolewidget import PythonConsoleWidget
from weathergit.gui.loggerwidget import LoggerWidget

POINTS = 300

class LoggerPanel(QtGui.QWidget):
    ""
    sig=pyqtSignal()
    ### connects widgets and signals ###
    def __init__(self, parent = None):
        super(LoggerPanel, self).__init__()
        self.ui = Ui_loggerpanel()
        self.ui.setupUi(self)
        self.layout().addWidget(PythonConsoleWidget())
        self.layout().addWidget(LoggerWidget())
        # self.ui.inCommand = PythonConsoleWidget()
        ### signals ###
        timer=QTimer()
        timer.timeout.connect(self.guiUpdate)
        timer.start(5*1000)


        self.init()
        self.guiUpdate()

    def init(self):
        ""
        # selList=["Query","Status","Plotter"]
        #
        # self.ui.inLeftViewSel.addItems(selList)
        # self.ui.inRightViewSel.addItems(selList)



    # @pyqt.Slot
    def guiUpdate(self):
        ""
        # self.ui.outLeftWView.load(QtCore.QUrl("http://192.168.1.120/status"))
        # self.ui.outRightWView.load(QtCore.QUrl("http://192.168.1.120/smap_query"))

    def guiUpdatePanel(self):
        ""
        # self.ui.outLat.setText("1000")
        # self.ui.outLong.setText("1000")


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = LoggerPanel()
    main.show()

    sys.exit(app.exec_())

