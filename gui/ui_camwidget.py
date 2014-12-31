# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\camwidget.ui'
#
# Created: Wed Dec 31 11:18:50 2014
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

class Ui_camwidget(object):
    def setupUi(self, camwidget):
        camwidget.setObjectName(_fromUtf8("camwidget"))
        camwidget.resize(549, 409)
        self.gridLayout = QtGui.QGridLayout(camwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(camwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.label = QtGui.QLabel(camwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.outLong = QtGui.QLineEdit(camwidget)
        self.outLong.setEnabled(False)
        self.outLong.setObjectName(_fromUtf8("outLong"))
        self.gridLayout.addWidget(self.outLong, 1, 1, 1, 1)
        self.outLat = QtGui.QLineEdit(camwidget)
        self.outLat.setEnabled(False)
        self.outLat.setObjectName(_fromUtf8("outLat"))
        self.gridLayout.addWidget(self.outLat, 1, 3, 1, 1)
        self.outCamView = QtWebKit.QWebView(camwidget)
        self.outCamView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.outCamView.setObjectName(_fromUtf8("outCamView"))
        self.gridLayout.addWidget(self.outCamView, 0, 0, 1, 4)

        self.retranslateUi(camwidget)
        QtCore.QMetaObject.connectSlotsByName(camwidget)

    def retranslateUi(self, camwidget):
        camwidget.setWindowTitle(_translate("camwidget", "Form", None))
        self.label_2.setText(_translate("camwidget", "Latitude:", None))
        self.label.setText(_translate("camwidget", "Longitude:", None))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    camwidget = QtGui.QWidget()
    ui = Ui_camwidget()
    ui.setupUi(camwidget)
    camwidget.show()
    sys.exit(app.exec_())

