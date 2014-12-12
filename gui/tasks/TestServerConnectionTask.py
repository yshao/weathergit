from PyQt4.QtCore import pyqtSignal, SIGNAL, QThread

class TestServerConnectionTask(QThread):
    def __init__(self,win,logger,outWidgets):
        """"""
        QThread.__init__(self)
        self.logger=logger
        self.win=win
        self.outWidgets=outWidgets

        self.logger.info("TEST SERVER CONNECTION")

        ###TODO include tid in log file

    def run(self):
        """"""
        print self.__class__
        print self.currentThreadId()
        print self.currentThread()

        self.logger.info("TEST SERVER CONNECTION STARTED")
        self.win.ui.outSMAPStatus.setText("Connecting")




    def stop(self):
        self.logger.info("TEST SERVER CONNECTION STOPPED")

