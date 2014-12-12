# This is only needed for Python v2 but is harmless for Python v3.
import sip
sip.setapi('QString', 2)
import webbrowser
from PyQt4 import QtCore, QtGui, QtXml
### ui files
from PyQt4.QtGui import QApplication
from ui_plotterwidget import Ui_PlotterWidget
from best.common.utils import *
from best.common.guiutils import *
from mplwidget import MplWidget


class PlotterWidget(QtGui.QWidget):
    ### connects widgets and signals ###
    def __init__(self, parent = None):
        super(PlotterWidget, self).__init__(parent)
        self.ui = Ui_PlotterWidget()
        self.ui.setupUi(self)
        self.asyncUiControl=asyncUiControl()

        ### init ###
        # self.logger = ClientLogger(self.ui.outLogBrowser)
        # self.config = Config('C:/Users/Ping/Workspace/DAQ/test/common/config.xml')
        # print self.config.get("IP_ENCODER")
        # self.config.read("daqmanager.log")
        self.mpl = MplWidget()

        ### signal init ###

        ### gui init ###
        #--- Config Group ---
        # self.ui.outSize.setText("Size of folder: "+ str(self.folder_calc_size()))

        #--- inputs group ---
        self.ui.inPlot.clicked.connect(self.guiPlot)

        #--- output group ---
        #self.ui.buttonSendCommand.setEnabled(0)

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


    def selectFile(self,gui_disp):   #Open a dialog to locate the sqlite file and some more...
        path = QtGui.QFileDialog.getOpenFileName(None,"Select database:","*.db")
        if path:
            self.database = DaqDB(path) # To make possible cancel the FileDialog and continue loading a predefined db
            self.ui.inDataSourceLine = path


        # self.openDBFile()


    def closeEvent(self,event):
        reply=QtGui.QMessageBox.question(self,'Message',"Are you sure to quit?",QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
        if reply==QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    ### event handler methods###
    def guiPlot(self):
        ""
        def index_containing_substring(the_list, substring):
            for i, s in enumerate(the_list):
                if substring in str(s):
                    idx=i
                    break

            return the_list[idx]



        # db=DaqDB(self.ui.inDataSourceLine)
        client=index_containing_substring( QApplication.topLevelWidgets(),"weatherclient")


        start=str(client.ui.inStartTime.text())
        end= str(client.ui.inEndTime.text())
        uuid=client.UUIDList

        # for i in xrange(len(uuid)):
        #     sub=str(uuid[i])
        #     m=re.search('([0-9]|[a-f]|-)*',sub)
        #     uuid[i] = m.group(0).rstrip(' -')
        client.logger.info(" ".join(uuid))


        try:
            data = client.datac.get_data(uuid, start, end)

        except Exception,e:
            print e

        ### update display
        num_points = len(data)
        title=self.ui.inTitle.text()
        xLabel=self.ui.inXLabel.text()
        yLabel=self.ui.inYLabel.text()

        ### plot data task
        self.mpl.update_labels(title,xLabel,yLabel)


        from matplotlib import pyplot, dates

        marker='-'
        tzone='America/Denver'
        for d in data:
            self.mpl.plot_date(dates.epoch2num(d[:, 0] / 1000), d[:, 1], marker,
                           tz=tzone)
        # self.mpl.plot_date(data)
        self.mpl.show()


    def on_plotting_done(self,result):
        ""
        self.logger.log_info("-".join(["RESULT",result]))

    def parse_plotting(self,s):
        ""
        result={}

        pattern = re.compile(r"""\|\s*                 # opening bar and whitespace
                                 '(?P<name>.*?)'       # quoted name
                                 \s*\|\s*(?P<n1>.*?)   # whitespace, next bar, n1
                                 \s*\|\s*(?P<n2>.*?)   # whitespace, next bar, n2
                                 \s*\|""", re.VERBOSE)
        match = pattern.match(s)

        name = match.group("name")
        n1 = float(match.group("n1"))
        n2 = float(match.group("n2"))


        result.update({'datasets_plotted': n1})
        return result

    ### builtin methods ###
    def openFolder(self):
        self.logger.log_info("Open Folder")
        webbrowser.open ('file://'+ self.ui.inDataFolder.text())

