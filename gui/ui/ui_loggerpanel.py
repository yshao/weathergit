# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui\loggerpanel.ui'
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

class Ui_loggerpanel(object):
    def setupUi(self, loggerpanel):
        loggerpanel.setObjectName(_fromUtf8("loggerpanel"))
        loggerpanel.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(loggerpanel)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboBox = QtGui.QComboBox(loggerpanel)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.inCommand = QtGui.QLineEdit(loggerpanel)
        self.inCommand.setObjectName(_fromUtf8("inCommand"))
        self.gridLayout.addWidget(self.inCommand, 0, 1, 1, 1)
        self.outResult = QtGui.QTextBrowser(loggerpanel)
        self.outResult.setObjectName(_fromUtf8("outResult"))
        self.gridLayout.addWidget(self.outResult, 1, 0, 1, 2)

        self.retranslateUi(loggerpanel)
        QtCore.QMetaObject.connectSlotsByName(loggerpanel)

    def retranslateUi(self, loggerpanel):
        loggerpanel.setWindowTitle(_translate("loggerpanel", "Command Console", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    loggerpanel = QtGui.QWidget()
    ui = Ui_loggerpanel()
    ui.setupUi(loggerpanel)
    loggerpanel.show()
    sys.exit(app.exec_())

