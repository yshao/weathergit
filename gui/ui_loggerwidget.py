# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\loggerwidget.ui'
#
# Created: Wed Dec 31 11:18:51 2014
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

class Ui_loggerwidget(object):
    def setupUi(self, loggerwidget):
        loggerwidget.setObjectName(_fromUtf8("loggerwidget"))
        loggerwidget.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(loggerwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboBox = QtGui.QComboBox(loggerwidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(loggerwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.outLogger = QtGui.QTextBrowser(loggerwidget)
        self.outLogger.setObjectName(_fromUtf8("outLogger"))
        self.gridLayout.addWidget(self.outLogger, 0, 0, 1, 2)

        self.retranslateUi(loggerwidget)
        QtCore.QMetaObject.connectSlotsByName(loggerwidget)

    def retranslateUi(self, loggerwidget):
        loggerwidget.setWindowTitle(_translate("loggerwidget", "Form", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    loggerwidget = QtGui.QWidget()
    ui = Ui_loggerwidget()
    ui.setupUi(loggerwidget)
    loggerwidget.show()
    sys.exit(app.exec_())

