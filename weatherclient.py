# This is only needed for Python v2 but is harmless for Python v3.
import sip
from PyQt4.QtGui import QStandardItemModel

sip.setapi('QString', 2)
import webbrowser
import os
import re
import sys
import threading

from PyQt4 import QtCore, QtGui
# from PyQt4.QtCore import QString

### ui files
from weathergit.gui.ui_weatherclientmain import Ui_WeatherClientMain
from best.daqmanager.gui.plotterwidget import PlotterWidget
from weathergit.gui.configeditor import ConfigEditor

from best.common.utils import *
from best.common.fileutils import *
from best.common.netutils import *

### py files
# from weathergit.gui.tasks.taskutils import *

### setup ###
script_name = re.sub('\..*','',os.path.basename(sys.argv[0]))
starting_dir = os.getcwd()

start_message="DataMan"
logger=create_logger(script_name,start_message)

DATA_DIR="c:/test_station/Demo/Data"

class ClientLogger:
    def __init__(self,gui_logger):
        self.gui_logger=gui_logger

    def log_info(self,txt):
        self.gui_logger.append(txt)
        # logger.info(txt)

    def log_error(self,txt):
        self.gui_logger.append(txt)
        # logger.error(txt)

    def log_warn(self,txt):
        self.gui_logger.append(txt)
        # logger.warn(txt)


LOGGER=""
### main gui ###
# class DAQManager(QtGui.QMainWindow):
#     ### connects widgets and signals ###
#     def __init__(self):
#         super(DAQManager, self).__init__()
#         self.ui = Ui_DAQManager()
#         self.ui.setupUi(self)


class WeatherClient(QtGui.QMainWindow):
    ### connects widgets and signals ###
    def __init__(self):
        super(WeatherClient, self).__init__()
        self.ui = Ui_WeatherClientMain()
        self.ui.setupUi(self)

        ### init ###
        self.initEnv()
        self.logger = ClientLogger(self.ui.outLogBrowser)
        self.config = Config("common/data.conf")

        port = self.config.get("SMAP_SERVER_PORT")
        host = self.config.get("SMAP_SERVER_HOST")

        ### gui init ###
        #--- Config Group ---
        # self.ui.outServiceOn.setText("Off")
        # self.ui.outSize.setText("Size of folder: "+ str(self.folder_calc_size()))
        self.ui.outPort.setText(port)
        self.ui.outHost.setText(host)
        # self.evt_testServerConnect()
        self.ui.statusbar.showMessage("Config initialized")

        #--- inputs group ---
        self.ui.tabWidget.addTab(PlotterWidget(),"Plotter")

        self.ui.inTestConnection.clicked.connect(self.evt_testServerConnection)
        self.ui.actionDatabase_Admin.triggered.connect(self.openPostgre)
        self.ui.actionConfig_Editor.triggered.connect(self.openConfigEditor)

        ### connect signals to commands ###
        # self.ui.inServiceOn.clicked.connect(self.gui_start_mirroring)
        # self.ui.inPlot.clicked.connect(self.gui_visualizing)
        # self.ui.inSendConfig.clicked.connect(self.gui_send_config)
        # self.ui.inUpdateSoftware.clicked.connect(self.gui_update_software)
        # self.ui.inOpenRawDirFolder.clicked.connect(self.openFolder)

        # self.ui.inSetDB.clicked.connect(self.selectFile)
        # self.ui.inSetRawDir.clicked.connect(self.selectFile)

        # self.ui.inEnableSynchronizing.checked(self.gui_start_mirroring)
        # self.ui.inEnableProcessing.checked(self.gui_start_processing)
        # self.ui.buttonSendCommand.clicked.connect(self.send_command)
        # self.ui.buttonSync.clicked.connect(self.sync)


        exit=QtGui.QAction(self)

    def selectFile(self,*items):   #Open a dialog to locate the sqlite file and some more...
        path = QtGui.QFileDialog.getOpenFileName(None,QtCore.QString.fromLocal8Bit("Select database:"),"*.sqlite")
        if path:
            for i in items.iteritems():
                i = path # To make possible cancel the FileDialog and continue loading a predefined db
        self.openDBFile()


    def closeEvent(self,event):
        reply=QtGui.QMessageBox.question(self,'Message',"Are you sure to quit?",QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
        if reply==QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



    ### event handler methods###
    def initEnv(self):
        """"""
        # check postgre installed



    def openPostgre(self):
        ""
        # cmd=Command()
        # cmd.run()
        cmd="C:\\Program Files\\PostgreSQL\\9.3\\bin\\pgAdmin3.exe"
        subprocess.call([cmd])


    def openConfigEditor(self):
        ""

        # app1 = QtGui.QApplication(sys.argv)
        configeditor=ConfigEditor()
        configeditor.setWindowTitle("Config Editor")
        configeditor.resize(400, 300)
        configeditor.show()
        # sys.exit(app.exec_())

    def evt_testServerConnection(self):
        ""

        return True

    ### methods and algorithm ###

    def populate_uuids(self):
        ""
        uuidList=[]
        for i in self.config["uuid"].iteritems():
            uuidList.append(i)

        model=QStandardItemModel(uuidList)
        self.ui.inUUIDList.setModel(model)


if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    weather = WeatherClient()
    weather.show()
    sys.exit(app.exec_())


