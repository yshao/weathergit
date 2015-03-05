__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '2/9/2015' '11:30 AM'

import sip
sip.setapi('QString', 2)
from PyQt4.QtGui import QStandardItemModel, QStandardItem, QAbstractItemView
from weathergit.common.dbconn import DbConn

from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSlot, pyqtSignal, QUrl
import sys

from gui.ui.ui_camviewwidget import Ui_camviewwidget


class CamviewWidget(QtGui.QWidget):
    ""
    sig=pyqtSignal((int,), (str,))

    ### connects widgets and signals ###
    def __init__(self, parent = None):
        super(CamviewWidget, self).__init__()
        self.ui = Ui_camviewwidget()
        self.ui.setupUi(self)
        self._guiInit()

    def _guiInit(self):
        ""
        addQView("http://192.168.1.212")



def addQView(url):
    ""

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = CamviewWidget()
    main.show()

    sys.exit(app.exec_())


