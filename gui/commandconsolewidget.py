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

from PyQt4 import QtCore, QtGui
import datetime
from gui.loggerhandler import logger

from projexui.widgets.xfilepathedit import XFilepathEdit
import projexui

class CommandSet(object):
    def __init__(self):
        ""
    def run(self,b):
        print b


def command(a,b):
    print a+b

def show_disk():
    print datetime.datetime.today()

def smap_connected():
    ""

def disk_size():
    ""

def sync_time():
    ""

def get_data():
    ""

def del_stream():
    ""

def show_stream():
    ""

def



import sys
current_module = sys.modules[__name__]

# class LoggerWidget(QtGui.QTextBrowser):
#     def __init__(self,parent=None):
#         super(LoggerWidget, self).__init__(parent)
#
#         self.logger=logger()
#
#         self.connect(SIGNAL=,self.print)
#
#     def print():
cmd=CommandSet()

import inspect
from pprint import pprint

# pprint(inspect.getmembers(current_module, inspect.isfunction))
a=[]
lis=inspect.getmembers(current_module, inspect.isfunction)
for item in lis:
    a.append(item[0])

print a

class PythonConsoleWidget(QtGui.QLineEdit):

    """PythonConsoleWidget(QtGui.QLineEdit)
    
    Provides a custom widget to accept Python expressions and emit output
    to other components via a custom signal.
    """
    
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
    
    def execute(self):
    
        # Define this here to give users something to look at.
        qApp = QtGui.qApp
        
        self.expression = self.text()
        try:
            result = str(eval(str(self.expression)))
            
            # Emit the result of the evaluated expression.

            self.pythonOutput.emit(result)

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
    edit = projexui.testWidget(XFilepathEdit)

    # >>> # set the filepath
    edit.setFilepath('/path/to/file')

    # >>> # prompt the user to select the filepath
    edit.pickFilepath()
    print edit.filepath()

    edit.hide()
    del edit


    sys.exit(app.exec_())