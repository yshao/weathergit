from PyQt4 import QtGui
from copy import deepcopy
from PyQt4.QtGui import QTreeView
from PyQt4 import QtGui, QtCore
import sys
from utils.utils import csv_to_d

__author__ = 'yuping'


class TreeView(QTreeView):
    def __init__(self,data):
        ""
        super(TreeView, self).__init__()
        self.data = deepcopy(data)
        # Tree view
        self.setModel(QtGui.QStandardItemModel())
        self.setAlternatingRowColors(True)
        self.setSortingEnabled(True)
        self.setHeaderHidden(False)
        self.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.model().itemChanged.connect(self.handleItemChanged)
        self.model().setHorizontalHeaderLabels(['Parameter', 'Value'])

        for x in self.data:
            if not self.data[x]:
                continue
            parent = QtGui.QStandardItem(x)
            parent.setFlags(QtCore.Qt.NoItemFlags)
            for y in self.data[x]:
                value = self.data[x][y]
                child0 = QtGui.QStandardItem(y)
                child0.setFlags(QtCore.Qt.NoItemFlags |
                                QtCore.Qt.ItemIsEnabled)
                child1 = QtGui.QStandardItem(str(value))
                child1.setFlags(QtCore.Qt.ItemIsEnabled |
                                QtCore.Qt.ItemIsEditable |
                                ~ QtCore.Qt.ItemIsSelectable)

                # child0,child1=self.make_link(x,y)

                parent.appendRow([child0, child1])
            self.model().appendRow(parent)

        self.expandAll()

    def handleItemChanged(self, item):
            parent = self.data[item.parent().text()]
            key = item.parent().child(item.row(), 0).text()
            parent[key] = type(parent[key])(item.text())

    def get_data(self):
        ""
        return self.data

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    d=csv_to_d('todo.csv')
    tv=TreeView(d)
    tv.show()

    sys.exit(app.exec_())

