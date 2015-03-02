from PyQt4 import QtGui
from weathergit.gui.treeview_test import TreeView
from weathergit.gui.ui.ui_instrumentwidget import Ui_instrumentwidget
import sys
# from fabtools.require import curl

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '2/25/2015' '10:53 AM'

class InstrumentWidget(QtGui.QWidget):
    """Matplotlib wxFrame with animation effect"""
    ### connects widgets and signals ###
    def __init__(self, parent = None):
        super(InstrumentWidget, self).__init__()
        self.ui = Ui_instrumentwidget()
        self.ui.setupUi(self)

        self.update()

        # self.ui.treeView=TreeView()

    def _guitInit(self):
        self.ui.eventView.setModel(TreeView(EventConfig('event.json').load()).gen_model())
        self.ui.driverView.setModel(TreeView(DriverConfig('driver.json').load()).gen_model())

    def update(self):

        # curl.time.get()

        self
        # self.ui.outLat.setText("1000")
        # self.ui.outLong.setText("1000")
        # self.ui.outCamView('http://')


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = InstrumentWidget()
    main.show()

    sys.exit(app.exec_())
