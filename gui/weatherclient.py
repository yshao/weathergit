# This is only needed for Python v2 but is harmless for Python v3.
import sip


sip.setapi('QString', 2)
from weathergit.gui.webview import WebView
from PyQt4.QtCore import QUrl
from PyQt4.QtGui import QWidget
from weathergit.common.env import Env
from weathergit.gui.instrumentwidget import InstrumentWidget
from weathergit.gui.datawidget import DataWidget
from weathergit.gui.streameditorwidget import StreamEditorWidget
from weathergit.camviewwidget import CamviewWidget
from weathergit.gui.snapshotmanwidget import SnapshotManWidget
from weathergit.gui.statuscontrolwidget import StatusControlWidget
from weathergit.gui.rtdispwidget import RTDispWidget

from weathergit.gui.command.OpenToolCmd import OpenToolCmd
from weathergit.gui.command.OpenVNCCmd import OpenVNCCmd
from weathergit.gui.command.OpenWebCmd import OpenWebCmd
from weathergit.gui.command.OpenWidgetCmd import OpenWidgetCmd
from weathergit.gui.command.invoker import Invoker

from PyQt4 import QtCore, QtGui

### ui files
from weathergit.common.dataclient import DataClient
from weathergit.common.dbconn import DbConn

from weathergit.gui.ui.ui_weatherclientmain import Ui_WeatherClientMain

from best.common.utils import *
from best.common.fileutils import *
from best.common.netutils import *
from weathergit.common.config import Config




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
        # self.ui.outSMAPStatus.setText("Unknown")
        self.setConfig()


    def setConfig(self,config=None):
        """"""
        ### meta data connection
        if config == None:
            config=Config(Env.getpath('HOME')+'/common/weatherplotter.conf')

        self.dbconn=DbConn()
        self.uuid=self.dbconn.get_uuid()
        self.datac=DataClient()

        ### init ###
        self.config = config
        self.initEnv()
        # self.logger = ClientLogger(self.ui.outLogBrowser)


        ### gui init ###

        #--- inputs group ---
        # self.ui.actionAbout.triggered.connect(open_dialog(LogoView()))

        self.ui.leftTab.addTab(StatusControlWidget(self),'Status')
        self.ui.leftTab.addTab(StreamEditorWidget(self),'Stream')
        self.ui.leftTab.addTab(DataWidget(self),'Data')
        self.ui.leftTab.addTab(SnapshotManWidget(self),'Cam')
        self.ui.leftTab.addTab(InstrumentWidget(self),'Instrument')
        # self.ui.leftTab.addTab(EventWidget(self),'Connection')

        # self.ui.rightTab.addTab(PlotterWidget(self),"Plotter")
        self.ui.rightTab.addTab(RTDispWidget(self),"RTDisplay")
        w=WebView("CamView",'http://192.168.1.212')
        self.ui.rightTab.addTab(w,w.objectName())

        # self.ui.rightTab.addTab(CamviewWidget(self),"Cam")
        w=WebView("WebView",'http://localhost:8000')
        self.ui.rightTab.addTab(w,w.objectName())


        browser= self.ui.rightTab.currentWidget()
        browser.load_view('')



        # self.ui.inTestConnection.clicked.connect(self.testServerConnection)
        # self.initInvoker()
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

        # self.populate_uuids()


    def closeEvent(self,event):
        reply=QtGui.QMessageBox.question(self,'Message',"Are you sure to quit?",QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
        if reply==QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



    ### event handler methods###


    ### refresh methods ###
    def refreshEnv(self):
        ""
        #--- Config Group ---
        # self.ui.outPort.setText(self.config["smap_server_port"])
        # self.ui.outHost.setText(self.config["smap_server_host"])
        # self.evt_testServerConnect()
        # self.ui.statusbar.showMessage("Config initialized")

    ### init methods ###
    def initEnv(self):
        """"""
        self.refreshEnv()

        # check postgre installed
        # now = QtCore.QDateTime.currentDateTime()
        # self.ui.inEndTime.setDateTime(now)


    def initMenu(self):
        """"""
        path="C:/Program Files/PostgreSQL/9.3/bin/pgAdmin3.exe"
        self.ui.actionDatabase_Admin.triggered.connect(lambda: self.invoker.invoke(OpenToolCmd(path)))

        path="C:/Program Files/teraterm/ttermpro.exe"
        self.ui.actionServer_SSH_Client.triggered.connect(lambda: self.invoker.invoke(OpenToolCmd(path)))

        path="C:/Program Files/teraterm/ttermpro.exe"
        self.ui.actionSource_SSH_Client.triggered.connect(lambda: self.invoker.invoke(OpenToolCmd(path)))

        self.ui.actionSource_VNC.triggered.connect(lambda: self.invoker.invoke(OpenVNCCmd(path)))


        name="ConfigEditor"
        self.ui.actionConfig_Editor.triggered.connect(lambda: self.invoker.invoke(OpenWidgetCmd(name)))

        self.ui.actionOpen_SMAP_Plotter.triggered.connect(
            lambda: self.invoker.invoke(OpenWebCmd(self.config['smap_plotter'])))

        self.ui.actionOpen_SMAP_Server.triggered.connect(
            lambda: self.invoker.invoke(OpenWebCmd(ip=self.config['smap_server'])))

        self.ui.actionOpen_SMAP_Monitor.triggered.connect(
            lambda: self.invoker.invoke(OpenWebCmd(self.config['smap_monitor'])))

        self.ui.actionOpen_SMAP_Monitor.triggered.connect(
            lambda: self.invoker.invoke(OpenWebCmd(self.config['ip_trendnet'])))

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

    # def testServerConnection(self):
    #     ""
    #     task=TestServerConnectionTask(self,self.logger,self.ui.cSMAPServer)
    #     res=task.run()
    #
    #     return res


    ### methods and algorithm ###


def check_network():
    def is_connected(d):
        if 'unreachable' in d:
            print 'offline'
        else:
            print 'online'

    d=run_command('ping 192.168.1.146')
    is_connected(d)
    d=run_command('ping 192.168.1.120')
    is_connected(d)
    d=run_command('ping 192.168.1.223')
    is_connected(d)

if __name__ == '__main__':
    check_network()
    import sys
    app = QtGui.QApplication(sys.argv)
    weather = WeatherClient()
    weather.show()
    sys.exit(app.exec_())
