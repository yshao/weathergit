# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui\datawidget.ui'
#
# Created: Wed Feb 25 14:08:42 2015
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

class Ui_datawidget(object):
    def setupUi(self, datawidget):
        datawidget.setObjectName(_fromUtf8("datawidget"))
        datawidget.resize(461, 328)
        self.gridLayout = QtGui.QGridLayout(datawidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(datawidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(datawidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.inEndTime = QtGui.QDateTimeEdit(datawidget)
        self.inEndTime.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 2, 10), QtCore.QTime(0, 0, 0)))
        self.inEndTime.setObjectName(_fromUtf8("inEndTime"))
        self.gridLayout.addWidget(self.inEndTime, 1, 2, 1, 2)
        self.inStartTime = QtGui.QDateTimeEdit(datawidget)
        self.inStartTime.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 2, 1), QtCore.QTime(0, 0, 0)))
        self.inStartTime.setObjectName(_fromUtf8("inStartTime"))
        self.gridLayout.addWidget(self.inStartTime, 0, 2, 1, 2)
        self.inExportType = QtGui.QComboBox(datawidget)
        self.inExportType.setObjectName(_fromUtf8("inExportType"))
        self.inExportType.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.inExportType, 8, 0, 1, 2)
        self.inUUIDList = QtGui.QTableView(datawidget)
        self.inUUIDList.setSortingEnabled(False)
        self.inUUIDList.setObjectName(_fromUtf8("inUUIDList"))
        self.gridLayout.addWidget(self.inUUIDList, 3, 0, 1, 4)
        self.actionDownload = QtGui.QPushButton(datawidget)
        self.actionDownload.setObjectName(_fromUtf8("actionDownload"))
        self.gridLayout.addWidget(self.actionDownload, 8, 2, 1, 1)
        self.inActionSQL = QtGui.QPushButton(datawidget)
        self.inActionSQL.setObjectName(_fromUtf8("inActionSQL"))
        self.gridLayout.addWidget(self.inActionSQL, 4, 0, 1, 1)
        self.outSql = QtGui.QTextBrowser(datawidget)
        self.outSql.setObjectName(_fromUtf8("outSql"))
        self.gridLayout.addWidget(self.outSql, 4, 2, 2, 2)
        self.outDataType = QtGui.QLineEdit(datawidget)
        self.outDataType.setEnabled(False)
        self.outDataType.setObjectName(_fromUtf8("outDataType"))
        self.gridLayout.addWidget(self.outDataType, 6, 2, 1, 1)
        self.outFilePath = QtGui.QLineEdit(datawidget)
        self.outFilePath.setEnabled(False)
        self.outFilePath.setObjectName(_fromUtf8("outFilePath"))
        self.gridLayout.addWidget(self.outFilePath, 7, 2, 1, 1)
        self.actionBrowseFolder = QtGui.QPushButton(datawidget)
        self.actionBrowseFolder.setObjectName(_fromUtf8("actionBrowseFolder"))
        self.gridLayout.addWidget(self.actionBrowseFolder, 7, 0, 1, 2)
        self.inStreamLimit = QtGui.QLineEdit(datawidget)
        self.inStreamLimit.setObjectName(_fromUtf8("inStreamLimit"))
        self.gridLayout.addWidget(self.inStreamLimit, 2, 2, 1, 1)
        self.label = QtGui.QLabel(datawidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.retranslateUi(datawidget)
        QtCore.QMetaObject.connectSlotsByName(datawidget)

    def retranslateUi(self, datawidget):
        datawidget.setWindowTitle(_translate("datawidget", "Form", None))
        self.label_5.setText(_translate("datawidget", "End", None))
        self.label_4.setText(_translate("datawidget", "Start", None))
        self.inExportType.setItemText(0, _translate("datawidget", "csv", None))
        self.actionDownload.setText(_translate("datawidget", "Download", None))
        self.inActionSQL.setText(_translate("datawidget", "SQL", None))
        self.outFilePath.setText(_translate("datawidget", "c:/local", None))
        self.actionBrowseFolder.setText(_translate("datawidget", "Browse Folder:", None))
        self.inStreamLimit.setText(_translate("datawidget", "100", None))
        self.label.setText(_translate("datawidget", "Stream Limit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    datawidget = QtGui.QWidget()
    ui = Ui_datawidget()
    ui.setupUi(datawidget)
    datawidget.show()
    sys.exit(app.exec_())

