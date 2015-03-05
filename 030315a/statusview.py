from PyQt4.QtGui import QTabWidget, QWidget
from weathergit.gui.treeview_test import TreeView

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/3/2015' '2:21 PM'

class StatusView(QWidget):
    def __init__(self):
        ""
        self.treeview=TreeView()
        tab=QTabWidget()
        self.addWidget(tab)
        self.addTab('Process')
        # self.

        self.addTab('Disk')

        self.addTab('System')


    def _guiBuild(self):
        ""

    def _init(self):
        # signal, slot
        self.connect(actionUpdateMonitor,lambda: guiUpdate(self.layout1,is_device_on()))
