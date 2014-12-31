#!/usr/bin/env python
import sip
sip.setapi('QString', 2)

import json

from PyQt4 import QtGui,QtCore
import sys

# number of data points
from PyQt4.QtCore import QTimer, pyqtSignal
from weathergit.gui.ui_smapviewerwidget import Ui_smapviewerwidget

POINTS = 300

# conf_json="""
#
#      """
#
# conf=json.load(conf_json)

class SmapViewerWidget(QtGui.QWidget):
    ""
    sig=pyqtSignal()
    ### connects widgets and signals ###
    def __init__(self, parent = None):
        super(SmapViewerWidget, self).__init__()
        self.ui = Ui_smapviewerwidget()
        self.ui.setupUi(self)

        ### signals ###
        timer=QTimer()
        timer.timeout.connect(self.guiUpdate)
        timer.start(5*1000)


        self.init()
        self.guiUpdate()

    def init(self):
        selList=["Query","Status","Plotter"]

        self.ui.inLeftViewSel.addItems(selList)
        self.ui.inRightViewSel.addItems(selList)



    # @pyqt.Slot
    def guiUpdate(self):
        self.ui.outLeftWView.load(QtCore.QUrl("http://192.168.1.120/status"))
        self.ui.outRightWView.load(QtCore.QUrl("http://192.168.1.120/smap_query"))

    def guiUpdatePanel(self):
        self.ui.outLat.setText("1000")
        self.ui.outLong.setText("1000")


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = SmapViewerWidget()
    main.show()

    sys.exit(app.exec_())

