from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSlot, pyqtSignal, QUrl
import sys
from gui.ui.ui_streameditorwidget import Ui_streameditorwidget

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '1/21/2015' '2:11 PM'

class StreamEditorWidget(QtGui.QWidget):
    ""
    sig=pyqtSignal((int,), (str,))
    # handler=streameditorwidgetHandler()

    UUIDList=[]

    ### connects widgets and signals ###
    def __init__(self, parent = None):
        super(StreamEditorWidget, self).__init__()
        self.ui = Ui_streameditorwidget()
        self.ui.setupUi(self)
        self._init()
        # self._guiUpdate()

        # self._getGuiData()

        self.sig[str].emit("opened")
        self.sig.emit(20)



    # def on_tblItemChanged(self,current,previous):
    #     print(current.data().toString())

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



        ### connect signals ###
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

    def __guiUpdateWView(self):
        ""
        self.ui.webView.load(QUrl("http://192.168.1.120/status"))

    def __guiUpdateTree(self):
        ""
        # self.config=Config(self.filep)
        self.ui.treeEditor()

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

