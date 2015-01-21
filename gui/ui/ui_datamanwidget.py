# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui\datamanwidget.ui'
#
# Created: Wed Jan 21 14:30:41 2015
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

class Ui_datamanwidget(object):
    def setupUi(self, datamanwidget):
        datamanwidget.setObjectName(_fromUtf8("datamanwidget"))
        datamanwidget.resize(400, 300)
        self.gridLayout_2 = QtGui.QGridLayout(datamanwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_13 = QtGui.QLabel(datamanwidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)
        self.inEditConn_2 = QtGui.QPushButton(datamanwidget)
        self.inEditConn_2.setObjectName(_fromUtf8("inEditConn_2"))
        self.gridLayout_2.addWidget(self.inEditConn_2, 0, 1, 1, 1)
        self.label_19 = QtGui.QLabel(datamanwidget)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_2.addWidget(self.label_19, 1, 0, 1, 1)
        self.inUpdateInterval_2 = QtGui.QLineEdit(datamanwidget)
        self.inUpdateInterval_2.setObjectName(_fromUtf8("inUpdateInterval_2"))
        self.gridLayout_2.addWidget(self.inUpdateInterval_2, 1, 1, 1, 1)
        self.inUpdateDataset_2 = QtGui.QPushButton(datamanwidget)
        self.inUpdateDataset_2.setObjectName(_fromUtf8("inUpdateDataset_2"))
        self.gridLayout_2.addWidget(self.inUpdateDataset_2, 2, 0, 1, 2)
        self.groupBox_2 = QtGui.QGroupBox(datamanwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.label_17 = QtGui.QLabel(self.groupBox_2)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_9.addWidget(self.label_17, 0, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.groupBox_2)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_9.addWidget(self.label_18, 1, 0, 1, 1)
        self.inFormulaList_2 = QtGui.QListView(self.groupBox_2)
        self.inFormulaList_2.setObjectName(_fromUtf8("inFormulaList_2"))
        self.gridLayout_9.addWidget(self.inFormulaList_2, 2, 0, 1, 2)
        self.inTimeSegmentSize_2 = QtGui.QTimeEdit(self.groupBox_2)
        self.inTimeSegmentSize_2.setCurrentSection(QtGui.QDateTimeEdit.HourSection)
        self.inTimeSegmentSize_2.setObjectName(_fromUtf8("inTimeSegmentSize_2"))
        self.gridLayout_9.addWidget(self.inTimeSegmentSize_2, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 3, 0, 1, 2)

        self.retranslateUi(datamanwidget)
        QtCore.QMetaObject.connectSlotsByName(datamanwidget)

    def retranslateUi(self, datamanwidget):
        datamanwidget.setWindowTitle(_translate("datamanwidget", "Form", None))
        self.label_13.setText(_translate("datamanwidget", "connectString", None))
        self.inEditConn_2.setText(_translate("datamanwidget", "Edit Connection", None))
        self.label_19.setText(_translate("datamanwidget", "Update Interval", None))
        self.inUpdateDataset_2.setText(_translate("datamanwidget", "Update Dataset - Disabled", None))
        self.groupBox_2.setTitle(_translate("datamanwidget", "Processing Parameters", None))
        self.label_17.setText(_translate("datamanwidget", "Time Segment Size:", None))
        self.label_18.setText(_translate("datamanwidget", "Conversion:", None))
        self.inTimeSegmentSize_2.setDisplayFormat(_translate("datamanwidget", "h:mm:ss", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    datamanwidget = QtGui.QWidget()
    ui = Ui_datamanwidget()
    ui.setupUi(datamanwidget)
    datamanwidget.show()
    sys.exit(app.exec_())

