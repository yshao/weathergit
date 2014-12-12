# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

class Find_Dialog(QtGui.QDialog):
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent)
        
        self.label = QtGui.QLabel("Enter search query:")
        self.lineedit = QtGui.QLineEdit()
        
        self.checkBox_case = QtGui.QCheckBox("Case sensitive")
        self.checkBox_whole = QtGui.QCheckBox("Whole words")
        
        self.buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Cancel)
        self.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self, QtCore.SLOT("accept()"))
        self.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self, QtCore.SLOT("reject()"))
        
        self.layout = QtGui.QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.lineedit)
        self.layout.addWidget(self.checkBox_case)
        self.layout.addWidget(self.checkBox_whole)
        self.layout.addWidget(self.buttonBox)
        
        self.setLayout(self.layout)
        self.setWindowTitle("Search")



        