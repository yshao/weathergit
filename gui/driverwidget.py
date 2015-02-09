from PyQt4.QtGui import QTreeView

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '2/4/2015' '3:49 PM'

import os
from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSignal, pyqtSlot
import sys
import ConfigParser
from gui.handlers.configeditorwidgethandler import configeditorwidgetHandler
from gui.ui.ui_configeditorwidget import Ui_configeditorwidget


class DriverMonitorWidget(QtGui.QWidget):
    def __init__(self):
        ""
        self.curl=request

    def _guiUpdate(self,data):
        ""

        for k,v in data:
            self.ui.outDriverMonitor.addItem()

    def _guiInit(self):
        ""



from weathergit.common.smaputils import SmapUtils

def get_monitor():
    su=SmapUtils()
    SmapUtils=su.get_query()

    d={}
    d.

    return d

self.actionUpdate.clicked.connect(lambda: self._guiUpdate(self._guiGetData))




class uiTreeView(QTreeView):
    columns = []
    rows = {}
    def __init__(self, treestore = None):
        if treestore:
            self.treestore = treestore
        else:
            self.treestore = QTreeModel(str)

        super(uiTreeView, self).__init__(self.treestore)

    def add_columns(self,columns=[], expander_index = -1, edited_callback = None):
        if columns and isinstance(columns, list):
            self.cells = {}
            for i in range(len(columns)):
                def col0_edited_cb( cell, path, new_text, model, callback ):
                    callback(cell, path, new_text, model )
                    #if model[path][2] is not new_text:
                        #print "Change '%s' to '%s'" % (model[path][2], new_text)
                        #model[path][2] = new_text
                    #return

                self.cells[ columns[i] ] = gtk.CellRendererText()

                if i == 0:
                    self.cells[ columns[i] ].set_property('cell-background', 'black')
                    self.cells[ columns[i] ].set_property('foreground', 'white')
                else:
                    self.cells[ columns[i] ].set_property( 'editable', True )
                    if edited_callback:
                        self.cells[ columns[i] ].connect( 'edited', col0_edited_cb, self.treestore, edited_callback )
                setattr(self, 'tvcolumn' + str(i), getattr(gtk, 'TreeViewColumn')(columns[i], self.cells[ columns[i] ]))
                curr_column = getattr(self, 'tvcolumn' + str(i) )
                #curr_column.pack_start(self.cell, True)
                #curr_column.set_attribute(cell, 'text', i)
                curr_column.set_attributes(self.cells[ columns[i] ], text=i, cell_background_set=3)
                self.append_column(curr_column)
                if expander_index >= 0 and i == expander_index:
                    self.set_expander_column(curr_column)

    def add_row(self,fields = [], index = None):
        return self.append_row(fields, index)

    def add_rows(self, rows = []):
        return self.append_rows(rows)

    def append_row(self, fields = [], index = None):
        return self.treestore.append(index, fields)

    def append_rows(self, rows = []):
        iters = []
        for row in range(len(rows)):
            index, fields = rows[row]
            iters.append(self.append_row(fields, index))

        return iters