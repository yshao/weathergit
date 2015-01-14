from PyQt4 import QtGui


class LoggerWidget(QtGui.QTextBrowser):
    def __init__(self,parent=None):
        super(LoggerWidget, self).__init__(parent)

        # self.logger=logger()
        #
        # self.connect(SIGNAL=,self.print)

