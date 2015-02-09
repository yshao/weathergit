__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '2/4/2015' '10:47 AM'

from PyQt4 import QtGui
import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QWidget
from gui.ui.ui_statuscontrolwidget import Ui_statuscontrolwidget


# logpipe=XLogger()

# testtask=Task()

class StatusControlWidget(QWidget,Ui_statuscontrolwidget):
    def __init__(self):
        super(StatusControlWidget, self).__init__()
        self.ui = Ui_statuscontrolwidget()
        self.ui.setupUi(self)
        self._guiInit()
        # self.widgets=
        print self.ui
        # print self.ui.gridLayout.children()
        # print self.ui.children()
        # def layout_widgets(layout):
        #     return layout.children()
        # print layout
        # items = (layout.itemAt(i) for i in range(layout.count()))
        # print self.ui
        # for w in self.ui.gridLayout:
        #     print w



    def _guiInit(self):
        ""
        # self.ui.logger.connect(actionPerformed)
        self.ui.actionUpdate.clicked.connect(lambda: self._guiUpdate(self.ui.gridLayout,self.getData()))

    @pyqtSlot()
    def _guiUpdate(self,layout,data):
        ""
        print data
        # def layout_widgets(layout):
        #     return layout.children()
        # print layout
        # items = (layout.itemAt(i) for i in range(layout.count()))
        # print self.ui
        # for w in layout_widgets(layout):
        #     print w
            # print w.objectName()
            # print w
            # w.text=data[w]


    def getData(self):
        ""
        return dict(field='something',value='100')



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Test1Widget()
    main.show()

    sys.exit(app.exec_())

