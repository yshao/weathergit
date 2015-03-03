from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSlot, pyqtSignal, QUrl
import sys
from PyQt4.QtGui import QStandardItemModel, QStandardItem, QAbstractItemView, QTreeWidgetItem, QTableWidgetItem
from weathergit.common.dbconn import DbConn
from weathergit.gui.ui.ui_streameditorwidget import Ui_streameditorwidget

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '1/21/2015' '2:11 PM'

class StreamEditorWidget(QtGui.QWidget):
    ""
    sig=pyqtSignal((int,), (str,))
    # handler=streameditorwidgetHandler()

    UUIDList=[]
    # jc = Javascript()

    ### connects widgets and signals ###
    def __init__(self, parent = None):
        super(StreamEditorWidget, self).__init__()
        self.ui = Ui_streameditorwidget()
        self.ui.setupUi(self)
        self._init()
        # self._guiUpdate()

        # self._getGuiData()

        # self.sig[str].emit("opened")
        # self.sig.emit(20)
        ### demo
        # self.model.itemChanged.connect(lambda: on_item_changed())

        self.ui.inUUIDList.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.ui.metaEditor.setE


        # map(self.model.itemChanged.connect, [lambda: on_item_changed(), lambda: self._on_itemSelected()])
        # map(self.ui.inUUIDList.itemChanged.connect, [lambda: self._on_itemSelected()])

        self.ui.inUUIDList.clicked.connect(lambda: self._guiUpdate_metaTable(self.on_itemSelected()))

        self.ui.inActionCommit.clicked.connect(lambda: self.update_meta())


    def update_metadata(self):
        ""
        print self.metamodel

    sigItemSelected=pyqtSignal()

    @pyqtSlot()
    def on_itemSelected(self):
        d=self._getGuiData()
        print d
        self.ui.outUUID.setText(d['uuid'])
        self.ui.outPath.setText(d['path'])
        # self.ui.out
        self.sigItemSelected.emit()
        self._guiUpdate_metaTable(d['uuid'])
        return d


    def _guiUpdate_metaTable(self,uuid):
        dbconn=DbConn()
        meta=dbconn.get_meta_kv()

        stream=meta[str(uuid)]
        print stream

        model=QStandardItemModel()
        model.setHorizontalHeaderItem(0,QStandardItem("Attribute"))
        model.setHorizontalHeaderItem(1,QStandardItem("Value"))


        while model.rowCount() > 0:
            model.removeRow(0)

        for k in stream.keys():
            name=stream[k]
            # print name
            # print k
            item1 = QStandardItem(k)
            item2 = QStandardItem(name)
            # item=QTableWidgetItem()
            # item.setText(1,name)
            # item.setText(2,k)
            # self.ui.metaEditor
            # model.appendRow([item1,item2])
            # self.ui.metaEditor.appendI
            model.appendRow([item1,item2])
        self.ui.metaEditor.setModel(model)

        # self.ui.metaEditor.addTopLevelItem(item)
        # self.ui.metaEditor.

        # model.itemChanged.connect(lambda: on_item_changed())

        self.metamodel=model

        # self.ui.met
        self.ui.metaEditor.setModel(model)
        # self.ui.metaEditor.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.ui.metaEditor.sortByColumn(1)
        self.ui.metaEditor.resizeColumnsToContents()



    def _init(self):
        ""

        self._guiUpdateWView()

        ### connect gui signals ###
        # self._guiUpdate()

        ### connect signals ###
        # self.ui.inDownload.clicked.connect(lambda: download_data)
        #
        #
        # self.sig.connect(download_data)
        # self.sig[str].connect(download_data)



        ### connect signals ###
        #TODO: select signal carrying index
        # self.ui.metaEditor.currentChanged(lambda: self._guiUpdateWView())
        # self.ui.metaEditor.currentChanged(lambda: self._guiUpdateTree())

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

        self._guiUpdate_UUID()



    def done_download_data(self):
        ""
        print "recv finished"

    @pyqtSlot(str)
    def _updateGui(self,s):
        ""

    @pyqtSlot(str)
    def update_download_data(self,s):
        print s


    def _getGuiData(self):
        d={}
        # print 'data'

        idx=self.ui.inUUIDList.currentIndex()
        row=idx.row()
        uuid= self.ui.model.index(row,0).data().toString()
        path= self.ui.model.index(row,1).data().toString()

        d['uuid']=uuid
        d['path']=path

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
    def _guiUpdateWView(self):
        ""
        uuid=self.ui.metaEditor.selectedIndexes()

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


    def _guiUpdate_UUID(self):
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
            # item1.setCheckable(True)

            model.appendRow([item1,item2])

        model.itemChanged.connect(lambda: on_item_changed())

        self.ui.model=model

        self.ui.inUUIDList.setModel(model)
        self.ui.inUUIDList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.inUUIDList.sortByColumn(1)
        self.ui.inUUIDList.resizeColumnsToContents()


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

    main = StreamEditorWidget()
    # main.load(filep)

    main.show()

    sys.exit(app.exec_())

