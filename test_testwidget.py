from PyQt4 import QtGui
import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QWidget
from gui.ui.ui_testwidget import Ui_testwidget


__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '2/3/2015' '12:18 PM'


# logpipe=XLogger()

# testtask=Task()

class TestWidget(QWidget):
    def __init__(self):
        super(TestWidget, self).__init__()
        self.ui = Ui_testwidget()
        self.ui.setupUi(self)
        self.guiInit()





    def _guiInit(self):
        ""
        # self.ui.logger.connect(actionPerformed)
        self.ui.actionSomething.clicked.connect(lambda: self._guiUpdate(self.layout(),self.getData()))

    @pyqtSlot()
    def _guiUpdate(self,data):
        ""


    def getData(self):
        ""
        return dict(field='something',value='100')


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = TestWidget()
    main.show()

    sys.exit(app.exec_())

