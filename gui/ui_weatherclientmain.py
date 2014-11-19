# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\weatherclientmain.ui'
#
# Created: Tue Nov 18 16:39:33 2014
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
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.outIP = QtGui.QLineEdit(self.groupBox)
        self.outIP.setEnabled(False)
        self.outIP.setObjectName(_fromUtf8("outIP"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.outIP)
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
        self.verticalLayout.addWidget(self.groupBox)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(30, 210, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
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
        QtCore.QMetaObject.connectSlotsByName(WeatherClientMain)

    def retranslateUi(self, WeatherClientMain):
        WeatherClientMain.setWindowTitle(_translate("WeatherClientMain", "BEST WeatherStation Client", None))
        self.groupBox.setTitle(_translate("WeatherClientMain", "SMAP Server", None))
        self.label.setText(_translate("WeatherClientMain", "IP", None))
        self.outIP.setText(_translate("WeatherClientMain", "192.168.1.108", None))
        self.label_2.setText(_translate("WeatherClientMain", "Port", None))
        self.outPort.setText(_translate("WeatherClientMain", "8080", None))
        self.inTestConnection.setText(_translate("WeatherClientMain", "Test Connection", None))
        self.inOpenPostgre.setText(_translate("WeatherClientMain", "Open Postgre", None))
        self.pushButton.setText(_translate("WeatherClientMain", "Plot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("WeatherClientMain", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("WeatherClientMain", "Tab 2", None))
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

