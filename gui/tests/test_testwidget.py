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

class Test1Widget(QWidget,Ui_testwidget):
    def __init__(self):
        super(Test1Widget, self).__init__()
        self.ui = Ui_testwidget()
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
        self.ui.actionSomething.clicked.connect(lambda: self._guiUpdate(self.ui.gridLayout,self.getData()))

    @pyqtSlot()
    def _guiUpdate(self,layout,data):
        ""
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

