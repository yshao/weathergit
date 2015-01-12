import logging
from logging.config import fileConfig
from os import getcwd
import sys

from PyQt4.QtCore import QObject,\
                         pyqtSignal

from PyQt4.QtGui import QDialog, \
                        QVBoxLayout, \
                        QPushButton, \
                        QTextBrowser,\
                        QApplication

class XStream(QObject):
    _stdout = None
    _stderr = None

    messageWritten = pyqtSignal(str)

    def flush( self ):
        pass

    def fileno( self ):
        return -1

    def write( self, msg ):
        if ( not self.signalsBlocked() ):
            self.messageWritten.emit(unicode(msg))

    @staticmethod
    def stdout():
        if ( not XStream._stdout ):
            XStream._stdout = XStream()
            sys.stdout = XStream._stdout
        return XStream._stdout

    @staticmethod
    def stderr():
        if ( not XStream._stderr ):
            XStream._stderr = XStream()
            sys.stderr = XStream._stderr
        return XStream._stderr

class XLogger():
    def __init__(self, name):
        self.logger = logging.getLogger(name)
    def debug(self,text):
        print text
        self.logger.debug(text)
    def info(self,text):
        print text
        self.logger.info(text)
    def warning(self,text):
        print text
        self.logger.warning(text)
    def error(self,text):
        print text
        self.logger.error(text)

class MyDialog(QDialog):
    def __init__( self, parent = None ):
        super(MyDialog, self).__init__(parent)

        # setup the ui
        self._console = QTextBrowser(self)
        self._button  = QPushButton(self)
        self._button.setText('Test Me')

        # create the layout
        layout = QVBoxLayout()
        layout.addWidget(self._console)
        layout.addWidget(self._button)
        self.setLayout(layout)

        # create connections
        XStream.stdout().messageWritten.connect( self._console.insertPlainText )
        XStream.stderr().messageWritten.connect( self._console.insertPlainText )

        self.xlogger = XLogger('analyzer')

        self._button.clicked.connect(self.test)

    def test( self ):

        # log some stuff
        self.xlogger.debug("Testing debug")
        self.xlogger.info('Testing info')
        self.xlogger.warning('Testing warning')
        self.xlogger.error('Testing error')

if ( __name__ == '__main__' ):
    fileConfig(''.join([getcwd(),'/logging.conf']))

    app = None
    if ( not QApplication.instance() ):
        app = QApplication([])

    dlg = MyDialog()
    dlg.show()