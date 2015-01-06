import sys
import unittest
from PyQt4 import QtCore, QtGui
import logging
from PyQt4.QtGui import QTextBrowser


class QtHandler(logging.Handler):
    def __init__(self):
        logging.Handler.__init__(self)
    def emit(self, record):
        record = self.format(record)
        if record: XStream.stdout().write('%s\n'%record)
        # originally: XStream.stdout().write("{}\n".format(record))


class XStream(QtCore.QObject):
    _stdout = None
    _stderr = None
    messageWritten = QtCore.pyqtSignal(str)
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


class test_XStream(unittest.TestCase):

    def setUp(self):
        ""
        self.logger = logging.getLogger(__name__)
        handler = QtHandler()
        handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)

        self.outHandlerGui=QTextBrowser()


    def test_stdout(self):

        self.logger.debug('debug message')
        self.logger.info('info message')
        self.logger.warning('warning message')
        self.logger.error('error message')
        print 'Old school hand made print message'

        out=self.outHandlerGui.toPlainText()
        XStream.stderr().messageWritten.connect( self.outHandlerGui.insertPlainText )
        self.assertRegexpMatches(out,'DEBUG: debug message')
        self.assertRegexpMatches(out,'INFO: info message')
        self.assertRegexpMatches(out,'WARNING: warning message')
        self.assertRegexpMatches(out,'ERROR: error message')


    if ( not QtGui.QApplication.instance() ):
        app = QtGui.QApplication([])


# class MyDialog(QtGui.QDialog):
#     def __init__( self, parent = None ):
#         super(MyDialog, self).__init__(parent)
#
#         self._console = QtGui.QTextBrowser(self)
#         self._button  = QtGui.QPushButton(self)
#         self._button.setText('Test Me')
#
#         layout = QtGui.QVBoxLayout()
#         layout.addWidget(self._console)
#         layout.addWidget(self._button)
#         self.setLayout(layout)
#
#         XStream.stdout().messageWritten.connect( self._console.insertPlainText )
#         XStream.stderr().messageWritten.connect( self._console.insertPlainText )
#
#         self._button.clicked.connect(self.test)
#
#     # def test( self ):
#     #     logger.debug('debug message')
#     #     logger.info('info message')
#     #     logger.warning('warning message')
#     #     logger.error('error message')
#     #     print 'Old school hand made print message'
#
#
# if ( __name__ == '__main__' ):
#     app = None
#     if ( not QtGui.QApplication.instance() ):
#         app = QtGui.QApplication([])
#     dlg = MyDialog()
#     dlg.show()
#     if ( app ):
#         app.exec_()