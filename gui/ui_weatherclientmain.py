# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\weatherclientmain.ui'
#
# Created: Wed Dec 10 11:25:00 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_WeatherClientMain(object):
    def setupUi(self, WeatherClientMain):
        WeatherClientMain.setObjectName(_fromUtf8("WeatherClientMain"))
        WeatherClientMain.resize(800, 600)
        self.centralwidget = QtGui.QWidget(WeatherClientMain)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.leftTab = QtGui.QTabWidget(self.centralwidget)
        self.leftTab.setObjectName(_fromUtf8("leftTab"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.inStartTime = QtGui.QDateTimeEdit(self.tab)
        self.inStartTime.setObjectName(_fromUtf8("inStartTime"))
        self.gridLayout.addWidget(self.inStartTime, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.inEndTime = QtGui.QDateTimeEdit(self.tab)
        self.inEndTime.setObjectName(_fromUtf8("inEndTime"))
        self.gridLayout.addWidget(self.inEndTime, 2, 1, 1, 1)
        self.inUUIDList = QtGui.QListView(self.tab)
        self.inUUIDList.setObjectName(_fromUtf8("inUUIDList"))
        self.gridLayout.addWidget(self.inUUIDList, 4, 0, 1, 2)
        self.leftTab.addTab(self.tab, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.leftTab, 1, 0, 1, 1)
        self.rightTab = QtGui.QTabWidget(self.centralwidget)
        self.rightTab.setMinimumSize(QtCore.QSize(388, 0))
        self.rightTab.setObjectName(_fromUtf8("rightTab"))
        self.gridLayout_2.addWidget(self.rightTab, 1, 1, 1, 1)
        self.cSMAP = QtGui.QGroupBox(self.centralwidget)
        self.cSMAP.setObjectName(_fromUtf8("cSMAP"))
        self.gridLayout_3 = QtGui.QGridLayout(self.cSMAP)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label = QtGui.QLabel(self.cSMAP)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.cSMAP)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 0, 2, 1, 1)
        self.inTestConnection = QtGui.QPushButton(self.cSMAP)
        self.inTestConnection.setObjectName(_fromUtf8("inTestConnection"))
        self.gridLayout_3.addWidget(self.inTestConnection, 3, 0, 1, 1)
        self.outHost = QtGui.QLineEdit(self.cSMAP)
        self.outHost.setEnabled(False)
        self.outHost.setObjectName(_fromUtf8("outHost"))
        self.gridLayout_3.addWidget(self.outHost, 0, 1, 1, 1)
        self.outPort = QtGui.QLineEdit(self.cSMAP)
        self.outPort.setEnabled(False)
        self.outPort.setObjectName(_fromUtf8("outPort"))
        self.gridLayout_3.addWidget(self.outPort, 0, 3, 1, 1)
        self.inOpenPostgre = QtGui.QPushButton(self.cSMAP)
        self.inOpenPostgre.setObjectName(_fromUtf8("inOpenPostgre"))
        self.gridLayout_3.addWidget(self.inOpenPostgre, 3, 3, 1, 1)
        self.outSMAPStatus = QtGui.QLabel(self.cSMAP)
        self.outSMAPStatus.setObjectName(_fromUtf8("outSMAPStatus"))
        self.gridLayout_3.addWidget(self.outSMAPStatus, 3, 1, 1, 1)
        self.gridLayout_2.addWidget(self.cSMAP, 0, 0, 1, 2)
        self.outLogBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.outLogBrowser.setObjectName(_fromUtf8("outLogBrowser"))
        self.gridLayout_2.addWidget(self.outLogBrowser, 2, 0, 1, 2)
        WeatherClientMain.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(WeatherClientMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        WeatherClientMain.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(WeatherClientMain)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        WeatherClientMain.setStatusBar(self.statusbar)
        self.actionConfig_Editor = QtGui.QAction(WeatherClientMain)
        self.actionConfig_Editor.setObjectName(_fromUtf8("actionConfig_Editor"))
        self.actionDatabase_Admin = QtGui.QAction(WeatherClientMain)
        self.actionDatabase_Admin.setObjectName(_fromUtf8("actionDatabase_Admin"))
        self.menuTools.addAction(self.actionConfig_Editor)
        self.menuTools.addAction(self.actionDatabase_Admin)
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(WeatherClientMain)
        self.leftTab.setCurrentIndex(0)
        self.rightTab.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(WeatherClientMain)

    def retranslateUi(self, WeatherClientMain):
        WeatherClientMain.setWindowTitle(_translate("WeatherClientMain", "BEST WeatherStation Client", None))
        self.label_6.setText(_translate("WeatherClientMain", "uuid", None))
        self.label_4.setText(_translate("WeatherClientMain", "start", None))
        self.label_5.setText(_translate("WeatherClientMain", "end", None))
        self.leftTab.setTabText(self.leftTab.indexOf(self.tab), _translate("WeatherClientMain", "UUID", None))
        self.cSMAP.setTitle(_translate("WeatherClientMain", "SMAP Server", None))
        self.label.setText(_translate("WeatherClientMain", "IP", None))
        self.label_2.setText(_translate("WeatherClientMain", "Port", None))
        self.inTestConnection.setText(_translate("WeatherClientMain", "Test Connection", None))
        self.outHost.setText(_translate("WeatherClientMain", "192.168.1.108", None))
        self.outPort.setText(_translate("WeatherClientMain", "8080", None))
        self.inOpenPostgre.setText(_translate("WeatherClientMain", "Open Postgre", None))
        self.outSMAPStatus.setText(_translate("WeatherClientMain", "Unknown", None))
        self.menuTools.setTitle(_translate("WeatherClientMain", "Tools", None))
        self.actionConfig_Editor.setText(_translate("WeatherClientMain", "Config Editor", None))
        self.actionDatabase_Admin.setText(_translate("WeatherClientMain", "Database Admin", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WeatherClientMain = QtGui.QMainWindow()
    ui = Ui_WeatherClientMain()
    ui.setupUi(WeatherClientMain)
    WeatherClientMain.show()
    sys.exit(app.exec_())

