#!/usr/bin/env python

from PyQt4 import QtGui,QtCore
import sys

# number of data points
from weathergit.gui.ui_camwidget import Ui_camwidget

POINTS = 300

class CamWidget(QtGui.QWidget):
    """Matplotlib wxFrame with animation effect"""
    ### connects widgets and signals ###
    def __init__(self, parent = None):
        super(CamWidget, self).__init__()
        self.ui = Ui_camwidget()
        self.ui.setupUi(self)

        self.update()



    def update(self):

        curl.time.get()


        self.ui.outLat.setText("1000")
        self.ui.outLong.setText("1000")
        self.ui.outCamView('http://')


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = CamWidget()
    main.show()

    sys.exit(app.exec_())

