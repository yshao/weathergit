# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\smapviewerwidget.ui'
#
# Created: Wed Dec 31 11:18:52 2014
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

class Ui_smapviewerwidget(object):
    def setupUi(self, smapviewerwidget):
        smapviewerwidget.setObjectName(_fromUtf8("smapviewerwidget"))
        smapviewerwidget.resize(658, 522)
        self.gridLayout = QtGui.QGridLayout(smapviewerwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.outRightWView = QtWebKit.QWebView(smapviewerwidget)
        self.outRightWView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.outRightWView.setObjectName(_fromUtf8("outRightWView"))
        self.gridLayout.addWidget(self.outRightWView, 1, 1, 1, 1)
        self.outLeftWView = QtWebKit.QWebView(smapviewerwidget)
        self.outLeftWView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.outLeftWView.setObjectName(_fromUtf8("outLeftWView"))
        self.gridLayout.addWidget(self.outLeftWView, 1, 0, 1, 1)
        self.inLeftViewSel = QtGui.QComboBox(smapviewerwidget)
        self.inLeftViewSel.setObjectName(_fromUtf8("inLeftViewSel"))
        self.gridLayout.addWidget(self.inLeftViewSel, 0, 0, 1, 1)
        self.inRightViewSel = QtGui.QComboBox(smapviewerwidget)
        self.inRightViewSel.setObjectName(_fromUtf8("inRightViewSel"))
        self.gridLayout.addWidget(self.inRightViewSel, 0, 1, 1, 1)

        self.retranslateUi(smapviewerwidget)
        QtCore.QMetaObject.connectSlotsByName(smapviewerwidget)

    def retranslateUi(self, smapviewerwidget):
        smapviewerwidget.setWindowTitle(_translate("smapviewerwidget", "Form", None))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    smapviewerwidget = QtGui.QWidget()
    ui = Ui_smapviewerwidget()
    ui.setupUi(smapviewerwidget)
    smapviewerwidget.show()
    sys.exit(app.exec_())

