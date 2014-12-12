# This is only needed for Python v2 but is harmless for Python v3.
import sip
from PyQt4.QtGui import QStandardItemModel, QStandardItem, QAbstractItemView
from gui.RTDispWidget import RTDispWidget
from gui.command.OpenDialogCmd import OpenDialogCmd
from gui.command.OpenToolCmd import OpenToolCmd
from gui.command.OpenVNCCmd import OpenVNCCmd
from gui.command.OpenWebCmd import OpenWebCmd
from gui.command.invoker import Invoker
from gui.tasks.TestServerConnectionTask import TestServerConnectionTask

sip.setapi('QString', 2)
import webbrowser
import os
import re
import sys
import threading

from PyQt4 import QtCore, QtGui

### ui files
from common.dataclient import DataClient
from weathergit.gui.plotterwidget import PlotterWidget
from common.dbconn import DbConn
from gui.matplotwidget import MatplotlibWidget
from gui.mplwidget import MplWidget
from weathergit.gui.ui_weatherclientmain import Ui_WeatherClientMain

# from weathergit.gui.configeditor import ConfigEditor

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


class ClientLogger:
    def __init__(self,gui_logger):
        self.gui_logger=gui_logger

    def info(self,txt):
        self.gui_logger.append(txt)
        # logger.info(txt)

    def error(self,txt):
        self.gui_logger.append(txt)
        # logger.error(txt)

    def warn(self,txt):
        self.gui_logger.append(txt)
        # logger.warn(txt)


class WeatherClient(QtGui.QMainWindow):
    invoker=Invoker()

    ### connects widgets and signals ###
    def __init__(self):
        """"""
        super(WeatherClient, self).__init__()
        self.ui = Ui_WeatherClientMain()
        self.ui.setupUi(self)
        self.ui.outSMAPStatus.setText("Unknown")


    def setConfig(self,config):
        """"""
        ### meta data connection
        # if config == None:
        #     config=Config(Env.getpath('HOME')+'/common/weatherplotter.conf')

        self.dbconn=DbConn()
        self.uuid=self.dbconn.get_uuid()
        self.datac=DataClient()

        ### init ###
        self.config = config
        self.initEnv()
        self.logger = ClientLogger(self.ui.outLogBrowser)





        ### gui init ###

        #--- inputs group ---
        self.ui.rightTab.addTab(PlotterWidget(self),"Plotter")
        self.ui.rightTab.addTab(RTDispWidget(self),"RT Display")

        self.ui.inTestConnection.clicked.connect(self.testServerConnection)
        self.initInvoker()
        # self.ui.actionConfig_Editor.triggered.connect(self.openConfigEditor)

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

        # exit=QtGui.QAction(self)

        self.populate_uuids()


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


    ### refresh methods ###
    def refreshEnv(self):
        #--- Config Group ---
        self.ui.outPort.setText(self.config["smap_server_port"])
        self.ui.outHost.setText(self.config["smap_server_host"])
        # self.evt_testServerConnect()
        self.ui.statusbar.showMessage("Config initialized")

    ### init methods ###
    def initEnv(self):
        """"""
        self.refreshEnv()

        # check postgre installed
        now = QtCore.QDateTime.currentDateTime()
        self.ui.inEndTime.setDateTime(now)


    def initInvoker(self):
        """"""
        path="C:/Program Files/PostgreSQL/9.3/bin/pgAdmin3.exe"
        self.ui.actionDatabase_Admin.triggered.connect(lambda: self.invoker.invoke(OpenToolCmd(path)))

        path="C:/Program Files/teraterm/ttermpro.exe"
        self.ui.actionServer_SSH_Client.triggered.connect(lambda: self.invoker.invoke(OpenToolCmd(path)))

        path="C:/Program Files/teraterm/ttermpro.exe"
        self.ui.actionSource_SSH_Client.triggered.connect(lambda: self.invoker.invoke(OpenToolCmd(path)))

        self.ui.actionSource_VNC.triggered.connect(lambda: self.invoker.invoke(OpenVNCCmd(path)))


        name="ConfigEditor"
        self.ui.actionConfig_Editor.triggered.connect(lambda: self.invoker.invoke(OpenDialogCmd(name)))

        self.ui.actionOpen_SMAP_Plotter.triggered.connect(
            lambda: self.invoker.invoke(OpenWebCmd(self.config['smap_plotter'])))

        self.ui.actionOpen_SMAP_Server.triggered.connect(
            lambda: self.invoker.invoke(OpenWebCmd(ip=self.config['smap_server'])))

        self.ui.actionOpen_SMAP_Monitor.triggered.connect(
            lambda: self.invoker.invoke(OpenWebCmd(self.config['smap_monitor'])))

        self.ui.actionSource_VNC.triggered.connect(lambda: self.invoker.invoke(OpenVNCCmd()))




    def openPostgre(self):
        ""
        # cmd=Command()
        # cmd.run()
        cmd="C:\\Program Files\\PostgreSQL\\9.3\\bin\\pgAdmin3.exe"
        subprocess.call([cmd])


    def openConfigEditor(self):
        ""

        # app1 = QtGui.QApplication(sys.argv)
        # configeditor=ConfigEditor()
        # configeditor.setWindowTitle("Config Editor")
        # configeditor.resize(400, 300)
        # configeditor.show()
        # sys.exit(app.exec_())

    def testServerConnection(self):
        ""
        task=TestServerConnectionTask(self,self.logger,self.ui.cSMAPServer)
        res=task.run()

        return res


    ### methods and algorithm ###

    def populate_uuids(self):
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



if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    weather = WeatherClient()
    weather.show()
    sys.exit(app.exec_())


