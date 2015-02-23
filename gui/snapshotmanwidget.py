import os
from common.utils import get_timestamp
from gui.commandset import CommandSet

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '2/9/2015' '10:24 AM'

import sip
sip.setapi('QString', 2)
from PyQt4.QtGui import QStandardItemModel, QStandardItem, QAbstractItemView
from weathergit.common.dbconn import DbConn
from weathergit.common.ProcessPool import ProcessPool
from common.guiutils import selectFile
from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSlot, pyqtSignal, QUrl
import sys

from gui.ui.ui_snapshotmanwidget import Ui_snapshotmanwidget
from weathergit.common.fabutils import *


class SnapshotManWidget(QtGui.QWidget):
    ""
    sig=pyqtSignal((int,), (str,))
    # handler=streameditorwidgetHandler()

    UUIDList=[]
    # jc = Javascript()

    ### connects widgets and signals ###
    def __init__(self, parent = None):
        super(SnapshotManWidget, self).__init__()
        self.ui = Ui_snapshotmanwidget()
        self.ui.setupUi(self)
        self._init()
        self.dbconn=DbConn()
        self.uuid=self.dbconn.get_uuid()





        # self._getGuiData()

        # self.sig[str].emit("opened")
        # self.sig.emit(20)

        ### demo
        self.ui.actionBrowseFolder.clicked.connect(lambda: self.ui.outFilePath.setText(selectFile()))
        # self.ui.actionSnapshot.clicked.connect(lambda: ProcessPool.gen_task_cmd("take_snapshot"))
        # self.ui.actionGetFiles.clicked.connect(lambda: ProcessPool.gen_task_cmd("get_"))
        self.ui.actionSnapshot.clicked.connect(lambda: self.snapshot())
        self.ui.actionGetFiles.clicked.connect(lambda: self.get_files())


    def snapshot(self):
        filename=get_timestamp()+'.png'
        self.ui.outFilename.setText(filename)
        # cmd=CommandSet()
        # cmd.take_snapshot(filename)
        take_snapshot(filename)



    def get_files(self):
        # cmd=CommandSet()
        file=os.path.basename(self.ui.outFilename.text())
        outfile=self.ui.outFilePath.text()+"/"+file

        print file
        print outfile
        get_snapshot_files(file,outfile)


    def _init(self):
        ""

        self.__guiUpdateWView()

        ### connect gui signals ###
        # self._guiUpdate()

        ### connect signals ###
        # self.ui.inDownload.clicked.connect(lambda: download_data)
        #
        #
        # self.sig.connect(download_data)
        # self.sig[str].connect(download_data)

        # TODO: connect to rtdisp
        # self.connect()



        ### connect signals ###
        #TODO: select signal carrying index
        # self.ui.metaEditor.currentChanged(lambda: self.__guiUpdateWView())
        # self.ui.metaEditor.currentChanged(lambda: self.__guiUpdateTree())

        # self.ui.inActionAdd.clicked.connect(self.add)
        # self.ui.inActionDone.clicked.connect(self.save_config)
        # self.ui.inActionAddSection.clicked.connect(self.add_section)
        # self.ui.inActionRemove.clicked.connect(self.remove)
        # self.ui.inActionFilePathSelect.clicked.connect(self.handler.on_action_file_path_selct)


        # t.connectSlot()
        # print t.finished()
        # t.finished.connect(self.done_download_data)
        # t.update.connect(lambda: self.update_download_data("A"))

        # self.sig.connect(download_data)
        # self.sig[str].connect(download_data)

        ### connect slots ###
        # self.handler.sigSql[str].connect(self._updateGui)


    def _guiInit(self):
        ""
        keys=self.uuid.keys()
        # self.selUUIDList=[]

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

    def done_download_data(self):
        ""
        print "recv finished"




    @pyqtSlot(str)
    def _guiUpdate_status(self,data):
        ""

        # model=QStandardItemModel()
        # model.setHorizontalHeaderItem(0,QStandardItem("attribute"))
        # model.setHorizontalHeaderItem(1,QStandardItem("status"))
        #
        # for key in data.keys():
        #     value=data[key]
        #     item1 = QStandardItem(key)
        #     item2 = QStandardItem(value)
        #     # item1.setCheckable(True)
        #
        #     model.appendRow([item1,item2])
        #
        # self.ui.outStatus.setModel(model)
        # self.ui.outStatus.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.ui.outStatus.sortByColumn(1)

    @pyqtSlot(str)
    def update_download_data(self,s):
        print s


    def _getGuiData(self):
        d={}


        return d

    @pyqtSlot(str)
    def handleDone(self,s):
        ""
        print s


    @pyqtSlot(str)
    def _guiUpdateFilePath(self):
        ""

        self.ui.inFilePathLine.setText(self.filep)
        # self.ui.outLeftWView.load(QtCore.QUrl("http://192.168.1.120/status"))
        # self.ui.outRightWView.load(QtCore.QUrl("http://192.168.1.120/smap_query"))
        # self.ui.outSql.setText()

        self.__guiUpdateTree()

    @pyqtSlot()
    def __guiUpdateWView(self):
        ""
        # uuid=self.ui.metaEditor.selectedIndexes()

        # self.ui.webView.load(QUrl("http://192.168.1.120/status"))
        # self.ui.webView.setGeometry(400,400,600,245)
        # self.ui.webView.baseSize(100)
        # self.ui.webView.scroll(300,10)


        # TODO: unittest signal
        # uuid = self.ui.metaeditor.selected()
        # self.jc.update()



    # @pyqtSignal()
    def __guiUpdateTree(self):
        ""
        uuid=self.ui.metaEditor.selectedIndexes()

        # self.config=Config(self.filep)
        self.ui.treeEditor()

        # TODO: unittest
        res=self.su.smap_query("select * where uuid like '%s'" % uuid)
        for row in res:
            print row


    ### gui methods ###
    def add(self):
        ""

    def add_section(self):
        ""

    def remove(self):
        ""

    def save_config(self):
        ""

        self.config.save()

    ### methods ###

    def save(self,filep=None):
        if filep == None:
            filep=self.filep

        self.config.write(filep)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = SnapshotManWidget()
    # main.load(filep)

    main.show()

    sys.exit(app.exec_())