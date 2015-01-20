# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui\datawidget.ui'
#
# Created: Mon Jan 19 16:59:57 2015
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
        datawidget.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(datawidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(datawidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.inEndTime = QtGui.QDateTimeEdit(datawidget)
        self.inEndTime.setObjectName(_fromUtf8("inEndTime"))
        self.gridLayout.addWidget(self.inEndTime, 1, 1, 1, 2)
        self.inUUIDList = QtGui.QTableView(datawidget)
        self.inUUIDList.setSortingEnabled(False)
        self.inUUIDList.setObjectName(_fromUtf8("inUUIDList"))
        self.gridLayout.addWidget(self.inUUIDList, 3, 0, 1, 3)
        self.inDownload = QtGui.QPushButton(datawidget)
        self.inDownload.setObjectName(_fromUtf8("inDownload"))
        self.gridLayout.addWidget(self.inDownload, 6, 0, 1, 1)
        self.label = QtGui.QLabel(datawidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.inStreamLimit = QtGui.QLineEdit(datawidget)
        self.inStreamLimit.setObjectName(_fromUtf8("inStreamLimit"))
        self.gridLayout.addWidget(self.inStreamLimit, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(datawidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.outSql = QtGui.QTextBrowser(datawidget)
        self.outSql.setObjectName(_fromUtf8("outSql"))
        self.gridLayout.addWidget(self.outSql, 5, 0, 1, 3)
        self.label_4 = QtGui.QLabel(datawidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.inStartTime = QtGui.QDateTimeEdit(datawidget)
        self.inStartTime.setObjectName(_fromUtf8("inStartTime"))
        self.gridLayout.addWidget(self.inStartTime, 0, 1, 1, 2)

        self.retranslateUi(datawidget)
        QtCore.QMetaObject.connectSlotsByName(datawidget)

    def retranslateUi(self, datawidget):
        datawidget.setWindowTitle(_translate("datawidget", "Form", None))
        self.label_5.setText(_translate("datawidget", "End", None))
        self.inDownload.setText(_translate("datawidget", "Download", None))
        self.label.setText(_translate("datawidget", "Stream Limit", None))
        self.label_2.setText(_translate("datawidget", "TextLabel", None))
        self.label_4.setText(_translate("datawidget", "Start", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    datawidget = QtGui.QWidget()
    ui = Ui_datawidget()
    ui.setupUi(datawidget)
    datawidget.show()
    sys.exit(app.exec_())

