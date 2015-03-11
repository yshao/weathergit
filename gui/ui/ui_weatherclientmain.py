# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui\weatherclientmain.ui'
#
# Created: Wed Feb 25 14:08:46 2015
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
        WeatherClientMain.resize(912, 600)
        self.centralwidget = QtGui.QWidget(WeatherClientMain)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.rightTab = QtGui.QTabWidget(self.centralwidget)
        self.rightTab.setMinimumSize(QtCore.QSize(388, 0))
        self.rightTab.setObjectName(_fromUtf8("rightTab"))
        self.gridLayout_2.addWidget(self.rightTab, 0, 1, 1, 1)
        self.leftTab = QtGui.QTabWidget(self.centralwidget)
        self.leftTab.setMinimumSize(QtCore.QSize(500, 350))
        self.leftTab.setObjectName(_fromUtf8("leftTab"))
        self.gridLayout_2.addWidget(self.leftTab, 0, 0, 1, 1)
        WeatherClientMain.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(WeatherClientMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 912, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuWeb_Portal = QtGui.QMenu(self.menubar)
        self.menuWeb_Portal.setObjectName(_fromUtf8("menuWeb_Portal"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        WeatherClientMain.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(WeatherClientMain)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        WeatherClientMain.setStatusBar(self.statusbar)
        self.actionConfig_Editor = QtGui.QAction(WeatherClientMain)
        self.actionConfig_Editor.setObjectName(_fromUtf8("actionConfig_Editor"))
        self.actionDatabase_Admin = QtGui.QAction(WeatherClientMain)
        self.actionDatabase_Admin.setObjectName(_fromUtf8("actionDatabase_Admin"))
        self.actionOpen_SMAP_Monitor = QtGui.QAction(WeatherClientMain)
        self.actionOpen_SMAP_Monitor.setObjectName(_fromUtf8("actionOpen_SMAP_Monitor"))
        self.actionOpen_SMAP_Plotter = QtGui.QAction(WeatherClientMain)
        self.actionOpen_SMAP_Plotter.setObjectName(_fromUtf8("actionOpen_SMAP_Plotter"))
        self.actionOpen_SMAP_Server = QtGui.QAction(WeatherClientMain)
        self.actionOpen_SMAP_Server.setObjectName(_fromUtf8("actionOpen_SMAP_Server"))
        self.actionTime_Series_DB = QtGui.QAction(WeatherClientMain)
        self.actionTime_Series_DB.setObjectName(_fromUtf8("actionTime_Series_DB"))
        self.actionSource_SSH_Client = QtGui.QAction(WeatherClientMain)
        self.actionSource_SSH_Client.setObjectName(_fromUtf8("actionSource_SSH_Client"))
        self.actionServer_SSH_Client = QtGui.QAction(WeatherClientMain)
        self.actionServer_SSH_Client.setObjectName(_fromUtf8("actionServer_SSH_Client"))
        self.actionSource_VNC = QtGui.QAction(WeatherClientMain)
        self.actionSource_VNC.setObjectName(_fromUtf8("actionSource_VNC"))
        self.actionOpen_Cam = QtGui.QAction(WeatherClientMain)
        self.actionOpen_Cam.setObjectName(_fromUtf8("actionOpen_Cam"))
        self.menuTools.addAction(self.actionConfig_Editor)
        self.menuTools.addAction(self.actionDatabase_Admin)
        self.menuTools.addAction(self.actionTime_Series_DB)
        self.menuTools.addAction(self.actionSource_SSH_Client)
        self.menuTools.addAction(self.actionServer_SSH_Client)
        self.menuTools.addAction(self.actionSource_VNC)
        self.menuWeb_Portal.addAction(self.actionOpen_SMAP_Monitor)
        self.menuWeb_Portal.addSeparator()
        self.menuWeb_Portal.addAction(self.actionOpen_SMAP_Plotter)
        self.menuWeb_Portal.addAction(self.actionOpen_SMAP_Server)
        self.menuWeb_Portal.addSeparator()
        self.menuWeb_Portal.addAction(self.actionOpen_Cam)
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuWeb_Portal.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(WeatherClientMain)
        self.rightTab.setCurrentIndex(-1)
        self.leftTab.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(WeatherClientMain)

    def retranslateUi(self, WeatherClientMain):
        WeatherClientMain.setWindowTitle(_translate("WeatherClientMain", "BEST WeatherStation Client", None))
        self.menuTools.setTitle(_translate("WeatherClientMain", "Tools", None))
        self.menuWeb_Portal.setTitle(_translate("WeatherClientMain", "Web Portal", None))
        self.menuHelp.setTitle(_translate("WeatherClientMain", "Help", None))
        self.actionConfig_Editor.setText(_translate("WeatherClientMain", "Config Editor", None))
        self.actionDatabase_Admin.setText(_translate("WeatherClientMain", "Database Admin", None))
        self.actionOpen_SMAP_Monitor.setText(_translate("WeatherClientMain", "Open SMAP Monitor", None))
        self.actionOpen_SMAP_Plotter.setText(_translate("WeatherClientMain", "Open SMAP Plotter", None))
        self.actionOpen_SMAP_Server.setText(_translate("WeatherClientMain", "Open SMAP Server", None))
        self.actionTime_Series_DB.setText(_translate("WeatherClientMain", "Time Series DB", None))
        self.actionSource_SSH_Client.setText(_translate("WeatherClientMain", "Source SSH Client", None))
        self.actionServer_SSH_Client.setText(_translate("WeatherClientMain", "Server SSH Client", None))
        self.actionSource_VNC.setText(_translate("WeatherClientMain", "Source VNC", None))
        self.actionOpen_Cam.setText(_translate("WeatherClientMain", "Open Cam", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WeatherClientMain = QtGui.QMainWindow()
    ui = Ui_WeatherClientMain()
    ui.setupUi(WeatherClientMain)
    WeatherClientMain.show()
    sys.exit(app.exec_())

