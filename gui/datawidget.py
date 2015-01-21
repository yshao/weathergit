from time import sleep

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Ping'
__created__ = '1/19/2015' '2:32 PM'

from PyQt4 import QtGui
import sys
from PyQt4.QtCore import pyqtSignal,pyqtSlot, QThread, QObject
from weathergit.gui.ui.ui_datawidget import Ui_datawidget



@pyqtSlot(int)
@pyqtSlot(str)
def download_data(s):
    ""
    print "method"+str(s)

class TThread(QThread):
    _sender=[]
    sigDone=pyqtSignal((str,))
    update=pyqtSignal((str,))
    def __init__(self,sender):
        ""
        super(TThread,self).__init__()
        print sender
        self.sigDone.connect(sender.handleDone)

    def add_senders(self,sender):
        self._sender.append(sender)

    def download_data(self,s):
        print "received"+s
        print "downloaded"
        self.sigDone.emit("DONE download data")
        self.update.emit("Updating")

    def run(self):
        for i in range(1,5):
            sleep(1)
            print i

        self.exit()




class DataWidget(QtGui.QWidget):
    ""
    sig=pyqtSignal((int,), (str,))
    ### connects widgets and signals ###
    def __init__(self, parent = None):
        super(DataWidget, self).__init__()
        self.ui = Ui_datawidget()
        self.ui.setupUi(self)
        self._init()
        self._guiUpdate()

        self._getGuiData()

        self.sig[str].emit("downloaded")
        self.sig.emit(20)



    def _init(self):
        ""
        self._guiUpdate()

        ### connect signals ###
        # self.ui.inDownload.clicked.connect(lambda: download_data)
        #
        #
        # self.sig.connect(download_data)
        # self.sig[str].connect(download_data)

        t=TThread(self)
        # self.ui.inDownload.clicked.connect(lambda: t.download_data("downloaded"))
        self.ui.inDownload.clicked.connect(lambda: t.start())
        # t.connectSlot()
        # print t.finished()
        t.finished.connect(self.done_download_data)
        t.update.connect(lambda: self.update_download_data("A"))

        self.sig.connect(download_data)
        self.sig[str].connect(download_data)

    def done_download_data(self):
        ""
        print "recv finished"

    @pyqtSlot(str)
    def update_download_data(self,s):
        print s


    def populate_uuid(self):
        ""

    def _getGuiData(self):
        d={}
        d['start_time']=self.ui.inStartTime.text()
        d['end_time']=self.ui.inEndTime.text()
        d['stream_limit']=self.ui.inStreamLimit.text()

        return d

    @pyqtSlot(str)
    def handleDone(self,s):
        ""
        print s



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
    main = DataWidget()
    main.show()

    sys.exit(app.exec_())

