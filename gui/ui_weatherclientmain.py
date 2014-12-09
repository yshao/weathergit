# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\weatherclientmain.ui'
#
# Created: Thu Nov 20 16:13:33 2014
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
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.outHost = QtGui.QLineEdit(self.groupBox)
        self.outHost.setEnabled(False)
        self.outHost.setObjectName(_fromUtf8("outHost"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.outHost)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_2)
        self.outPort = QtGui.QLineEdit(self.groupBox)
        self.outPort.setEnabled(False)
        self.outPort.setObjectName(_fromUtf8("outPort"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.outPort)
        self.inTestConnection = QtGui.QPushButton(self.groupBox)
        self.inTestConnection.setObjectName(_fromUtf8("inTestConnection"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.inTestConnection)
        self.inOpenPostgre = QtGui.QPushButton(self.groupBox)
        self.inOpenPostgre.setObjectName(_fromUtf8("inOpenPostgre"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.inOpenPostgre)
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.inStartTime = QtGui.QDateTimeEdit(self.tab)
        self.inStartTime.setObjectName(_fromUtf8("inStartTime"))
        self.gridLayout.addWidget(self.inStartTime, 1, 1, 1, 1)
        self.inUUIDList = QtGui.QListView(self.tab)
        self.inUUIDList.setObjectName(_fromUtf8("inUUIDList"))
        self.gridLayout.addWidget(self.inUUIDList, 1, 3, 3, 1)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.inEndTime = QtGui.QDateTimeEdit(self.tab)
        self.inEndTime.setObjectName(_fromUtf8("inEndTime"))
        self.gridLayout.addWidget(self.inEndTime, 2, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 2)
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.outLogBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.outLogBrowser.setObjectName(_fromUtf8("outLogBrowser"))
        self.verticalLayout.addWidget(self.outLogBrowser)
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
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(WeatherClientMain)

    def retranslateUi(self, WeatherClientMain):
        WeatherClientMain.setWindowTitle(_translate("WeatherClientMain", "BEST WeatherStation Client", None))
        self.groupBox.setTitle(_translate("WeatherClientMain", "SMAP Server", None))
        self.label.setText(_translate("WeatherClientMain", "IP", None))
        self.outHost.setText(_translate("WeatherClientMain", "192.168.1.108", None))
        self.label_2.setText(_translate("WeatherClientMain", "Port", None))
        self.outPort.setText(_translate("WeatherClientMain", "8080", None))
        self.inTestConnection.setText(_translate("WeatherClientMain", "Test Connection", None))
        self.inOpenPostgre.setText(_translate("WeatherClientMain", "Open Postgre", None))
        self.label_3.setText(_translate("WeatherClientMain", "uuid", None))
        self.label_4.setText(_translate("WeatherClientMain", "start", None))
        self.label_5.setText(_translate("WeatherClientMain", "end", None))
        self.pushButton.setText(_translate("WeatherClientMain", "Plot", None))
        self.label_6.setText(_translate("WeatherClientMain", "uuid", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("WeatherClientMain", "UUID", None))
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

