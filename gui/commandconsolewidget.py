#!/usr/bin/env python

"""
pythonconsolewidget.py

A Python console custom widget for Qt Designer.

Copyright (C) 2006 David Boddie <david@boddie.org.uk>
Copyright (C) 2005-2006 Trolltech ASA. All rights reserved.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
import inspect
import unittest

from PyQt4 import QtCore, QtGui
import datetime
# from weathergit.common.smaputils import SmapUtils
# from gui.loggerhandler import logger

# from projexui.widgets.xfilepathedit import XFilepathEdit
# import projexui
from PyQt4.QtGui import QStringListModel, QCompleter
from weathergit.common.ProcessPool import ProcessPool
from weathergit.gui.commandset import CommandSet
from weathergit.common.fabutils import *
import sys
# current_module = sys.modules[__name__]
import inspect
from pprint import pprint

cmd=CommandSet()


class CommandLineEdit(QtGui.QLineEdit):
    def __init__(self,parent=None):
        super(QtGui.QLineEdit, self).__init__(parent)

        model = QStringListModel()
        completer = QCompleter()
        completer.setModel(model)
        model.setStringList(cmd.cmdset)

        self.setCompleter(completer)



class PythonConsoleWidget(CommandLineEdit):

    """PythonConsoleWidget(QtGui.QLineEdit)
    
    Provides a custom widget to accept Python expressions and emit output
    to other components via a custom signal.
    """

    def add_logger(self,w):
        self.w=w

    pythonOutput = QtCore.pyqtSignal(str)
    
    def __init__(self, parent=None):
    
        super(PythonConsoleWidget, self).__init__(parent)
        self.history = []
        self.current = -1
        
        self.returnPressed.connect(self.execute)
    
    def keyReleaseEvent(self, event):
    
        if event.type() == QtCore.QEvent.KeyRelease:
        
            if event.key() == QtCore.Qt.Key_Up:
                current = max(0, self.current - 1)
                if 0 <= current < len(self.history):
                    self.setText(self.history[current])
                    self.current = current
                
                event.accept()
            
            elif event.key() == QtCore.Qt.Key_Down:
                current = min(len(self.history), self.current + 1)
                if 0 <= current < len(self.history):
                    self.setText(self.history[current])
                else:
                    self.clear()
                self.current = current
                
                event.accept()

    def execute2(self):

        self.expression = self.text()
        # cmd2=CommandSet()

        result = str(eval('cmd.'+str(self.expression+'()')))
        self.pythonOutput.emit(result)
        self.w.append(result)
        # ProcessPool.gen_task(self.expression)

    def execute(self):
    
        # Define this here to give users something to look at.
        qApp = QtGui.qApp
        cmdset=CommandSet()
        self.expression = self.text()

        # print self.expression
        try:

            result = str(eval('cmdset.'+str(self.expression)+'()'))
            
            # Emit the result of the evaluated expression.

            self.pythonOutput.emit(result)
            self.w.append(result)

            # Clear the line edit, append the successful expression to the
            # history, and update the current command index.
            self.clear()
            self.history.append(self.expression)
            self.current = len(self.history)
        except:
            pass


if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)
    widget = PythonConsoleWidget()
    widget.show()


    # >>> # create the edit
    # edit = projexui.testWidget(XFilepathEdit)
    #
    # # >>> # set the filepath
    # edit.setFilepath('/path/to/file')
    #
    # # >>> # prompt the user to select the filepath
    # edit.pickFilepath()
    # print edit.filepath()
    #
    # edit.hide()
    # del edit

    # print eval('cmd.'+str('today'))


    sys.exit(app.exec_())

