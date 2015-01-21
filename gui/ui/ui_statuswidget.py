# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui\statuswidget.ui'
#
# Created: Wed Jan 21 14:30:42 2015
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

class Ui_statuswidget(object):
    def setupUi(self, statuswidget):
        statuswidget.setObjectName(_fromUtf8("statuswidget"))
        statuswidget.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(statuswidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(statuswidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtGui.QLabel(statuswidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(statuswidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.retranslateUi(statuswidget)
        QtCore.QMetaObject.connectSlotsByName(statuswidget)

    def retranslateUi(self, statuswidget):
        statuswidget.setWindowTitle(_translate("statuswidget", "Form", None))
        self.label_2.setText(_translate("statuswidget", "Receiver Temp.", None))
        self.label.setText(_translate("statuswidget", "Brightness Temp.", None))
        self.label_3.setText(_translate("statuswidget", "CurrentFileStamp", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    statuswidget = QtGui.QWidget()
    ui = Ui_statuswidget()
    ui.setupUi(statuswidget)
    statuswidget.show()
    sys.exit(app.exec_())

