__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '2/10/2015' '10:18 AM'

from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSignal, pyqtSlot
from PyQt4.QtGui import QStandardItemModel, QStandardItem, QAbstractItemView
import sys
from weathergit.common.dbconn import DbConn

from weathergit.gui.ui.ui_streamtablewidget import Ui_streamtablewidget

class StreamTableWidget(QtGui.QWidget):
    ""
    sig=pyqtSignal((int,), (str,))
    # handler=streameditorwidgetHandler()

    UUIDList=[]
    # jc = Javascript()

    ### connects widgets and signals ###
    def __init__(self, parent = None):
        super(StreamTableWidget, self).__init__()
        self.ui = Ui_streamtablewidget()
        self.ui.setupUi(self)
        self._init()
        # self._guiUpdate()

        # self._getGuiData()

        # self.sig[str].emit("opened")
        # self.sig.emit(20)
        ### demo
        # self.model.itemChanged.connect(lambda: on_item_changed())


        # map(self.model.itemChanged.connect, [lambda: on_item_changed(), lambda: self._on_itemSelected()])
        # map(self.model.itemChanged.connect, [lambda: self._on_itemSelected()])

        self.ui.actionStreamJsonCommit.clicked.connect(lambda: self.update_metadata(self._guiUpdate_table()))


    def update_metadata(self,d):
        ""

    def _guiUpdate_table(self):
        ""


    sigItemSelected=pyqtSignal()

    @pyqtSlot()
    def on_itemSelected(self):
        self.sigItemSelected.emit()


    def _init(self):
        ""
        # self._guiUpdate_table()
        # self._guiUpdateWView()

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

        # self._guiUpdate_UUID()



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
        uuid=self.ui.metaeditor.selectedIndexes()

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


    def _guiUpdate_table(self,uuid):
        ""
        self.dbconn=DbConn()
        # self.uuid=self.dbconn.get_uuid()
        uuid=''
        self.meta=self.dbconn.get_meta_kv()[uuid]


        keys=self.meta.keys()

        model=QStandardItemModel()
        model.setHorizontalHeaderItem(0,QStandardItem("Attribute"))
        model.setHorizontalHeaderItem(1,QStandardItem("Value"))

        for k in keys:
            name=self.meta[k]['Attribute']
            item1 = QStandardItem(k)
            item2 = QStandardItem(name)
            item1.setCheckable(True)

            model.appendRow([item1,item2])

        # model.itemChanged.connect(lambda: on_item_changed())

        self.model=model

        self.ui.metaeditor.setModel(model)
        self.ui.metaeditor.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.metaeditor.sortByColumn(1)
        self.ui.metaeditor.resizeColumnsToContents()


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

    main = StreamTableWidget()
    # main.load(filep)

    main.show()

    sys.exit(app.exec_())
