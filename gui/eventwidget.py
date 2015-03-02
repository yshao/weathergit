from pyface.viewer.tree_viewer import TreeViewer
from common.driverconfig import EventConfig

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '2/25/2015' '2:06 PM'

from PyQt4 import QtGui
from weathergit.gui.ui.ui_schedulerwidget import Ui_schedulerwidget
import sys

class SchedulerWidget(QtGui.QWidget):
    ### connects widgets and signals ###
    def __init__(self, parent = None):
        super(SchedulerWidget, self).__init__()
        self.ui = Ui_schedulerwidget()
        self.ui.setupUi(self)

        self.update()

    def _guitInit(self):
        self.ui.eventView.setModel(TreeViewer(EventConfig('event.json').load()).gen_model())


    def update(self):
        self.ui.eventView.refresh()

        # curl.time.get()

        # self
        # self.ui.outLat.setText("1000")
        # self.ui.outLong.setText("1000")
        # self.ui.outCamView('http://')


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = SchedulerWidget()
    main.show()

    sys.exit(app.exec_())
