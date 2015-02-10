__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Ping'
__created__ = '1/19/2015' '2:32 PM'

from PyQt4 import QtGui
import sys
from PyQt4.QtCore import pyqtSignal,pyqtSlot, QThread, QObject
from weathergit.gui.ui.ui_datawidget import Ui_datawidget

from time import sleep
from PyQt4.QtGui import QStandardItemModel, QStandardItem, QAbstractItemView, QFileDialog
from weathergit.common.dbconn import DbConn
from weathergit.common.guiutils import *
from weathergit.gui.handlers.datawidgethandler import datawidgetHandler


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


    handler=datawidgetHandler()

    UUIDList=[]

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


        ### demo
        self.ui.actionBrowseFolder.clicked.connect(lambda: self.ui.outFilePath.setText(selectFile()))
        self.ui.actionDownload.clicked.connect(lambda: download_data(self.UUIDList,self.ui.outFilePath.text()))
        self.ui.inActionSQL.clicked.connect(lambda: self.ui.outSql.setText(self._guiGet_parse2sql()))



    # def _guiGet_uuid(self):
    #     for idx in self.ui.inUUIDList.selectedIndexes():
    #         item=self.ui.inUUIDList.indexAt(idx)
    #         item.

    # def on_tblItemChanged(self,current,previous):
    #     print(current.data().toString())

    def _guiGet_parse2sql(self):
        ""
        d={}
        d['start_time']=self.ui.inStartTime.text()
        d['end_time']=self.ui.inEndTime.text()
        d['stream_limit']=self.ui.inStreamLimit.text()
        d['uuid']=self.UUIDList


        sql = "select data start %(start_time)s end %(end_time)s streamlimit %(stream_limit)s where uuid like '%(uuid)s'" %d

        return sql


    def _init(self):
        ""
        # ### connect gui signals ###
        # # self.ui.inUUIDList.selectionModel().currentChanged.connect(self.on_tblItemChanged)
        #
        #
        # self._guiUpdate()
        #
        # ### connect signals ###


    def done_download_data(self):
        ""
        print "recv finished"

    @pyqtSlot(str)
    def _updateGui(self,s):
        self.ui.outSql.setText(s)

    @pyqtSlot(str)
    def update_download_data(self,s):
        print s


    def populate_uuid(self):
        ""
        self.dbconn=DbConn()
        self.uuid=self.dbconn.get_uuid()
        keys=self.uuid.keys()

        model=QStandardItemModel()
        model.setHorizontalHeaderItem(0,QStandardItem("UUID"))
        model.setHorizontalHeaderItem(1,QStandardItem("Path"))

        def on_item_changed():
            i = 0
            list=[]
            while model.item(i):
                if not model.item(i,0).checkState():
                    ""
                    # return
                else:
                    # print model.item(i,0).text()
                    list.append(model.item(i,0).text())
                i += 1

            self.UUIDList=list


        for key in keys:
            name=self.uuid[key]['Path']
            item1 = QStandardItem(key)
            item2 = QStandardItem(name)
            item1.setCheckable(True)

            model.appendRow([item1,item2])

        model.itemChanged.connect(lambda: on_item_changed())

        self.ui.inUUIDList.setModel(model)
        self.ui.inUUIDList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.inUUIDList.sortByColumn(1)
        self.ui.inUUIDList.resizeColumnsToContents()

    def _getGuiData(self):
        # print self.UUIDList
        d={}
        d['start_time']=self.ui.inStartTime.text()
        d['end_time']=self.ui.inEndTime.text()
        d['stream_limit']=self.ui.inStreamLimit.text()
        d['paths']=self.UUIDList
        d['export_type']=self.ui.inExportType.currentText()

        return d

    @pyqtSlot(str)
    def handleDone(self,s):
        ""
        print s


    @pyqtSlot(str)
    def _guiUpdate(self):
        ""

        self.populate_uuid()
        # self.ui.outLeftWView.load(QtCore.QUrl("http://192.168.1.120/status"))
        # self.ui.outRightWView.load(QtCore.QUrl("http://192.168.1.120/smap_query"))
        # self.ui.outSql.setText()

    def guiUpdatePanel(self):
        ""
        # self.ui.outLat.setText("1000")
        # self.ui.outLong.setText("1000")


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = DataWidget()
    main.show()

    sys.exit(app.exec_())

