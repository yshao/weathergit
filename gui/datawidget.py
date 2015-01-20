__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Ping'
__created__ = '1/19/2015' '2:32 PM'

from PyQt4 import QtGui
import sys
from PyQt4.QtCore import pyqtSignal
from weathergit.gui.ui.ui_datawidget import Ui_datawidget



class DataWidget(QtGui.QWidget):
    ""
    sig=pyqtSignal()
    ### connects widgets and signals ###
    def __init__(self, parent = None):
        super(DataWidget, self).__init__()
        self.ui = Ui_datawidget()
        self.ui.setupUi(self)
        self._init()
        self._guiUpdate()

        self._getGuiData()



    def _init(self):
        ""
        self._guiUpdate()

        ### connect signals ###
        self.ui.inDownload.clicked.connect(download_data)


    def populate_uuid(self):

    def _getGuiData(self):
        d['start_time']=self.ui.
        d[]

        return d

    # @pyqt.Slot
    def _guiUpdate(self):
        ""
        self.populate_uuid()
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

