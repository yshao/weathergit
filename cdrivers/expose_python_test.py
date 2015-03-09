import sys
from PyQt4 import QtCore, QtGui, QtWebKit

"""Html snippet."""
html = """
<html><body>
  <center>
  <script language="JavaScript">
    document.write('<p>Python ' + pyObj.pyVersion + '</p>')
  </script>
  <button onClick="pyObj.showMessage('Hello from WebKit')">Press me</button>
  <button onClick="pyObj2.showMessage('Goodbye')">Press me</button>
  </center>
</body></html>
"""

class StupidClass2(QtCore.QObject):
    """Simple class with one slot and one read-only property."""

    @QtCore.pyqtSlot(str)
    def showMessage(self, msg):
        """Open a message box and display the specified message."""
        QtGui.QMessageBox.information(None, "Info", msg)

    # def _pyVersion(self):
    #     """Return the Python version."""
    #     return sys.version + ">>"
    #
    # """Python interpreter version property."""
    # pyVersion = QtCore.pyqtProperty(str, fget=_pyVersion)


class StupidClass(QtCore.QObject):
    """Simple class with one slot and one read-only property."""

    @QtCore.pyqtSlot(str)
    def showMessage(self, msg):
        """Open a message box and display the specified message."""
        QtGui.QMessageBox.information(None, "Info", msg)

    def _pyVersion(self):
        """Return the Python version."""
        return sys.version + ">>"

    """Python interpreter version property."""
    pyVersion = QtCore.pyqtProperty(str, fget=_pyVersion)

def main():
    app = QtGui.QApplication(sys.argv)

    myObj = StupidClass()
    myObj2 = StupidClass2()

    webView = QtWebKit.QWebView()
    # Make myObj exposed as JavaScript object named 'pyObj'
    webView.page().mainFrame().addToJavaScriptWindowObject("pyObj", myObj)
    webView.page().mainFrame().addToJavaScriptWindowObject("pyObj2", myObj2)
    webView.setHtml(html)
    webView.page().mainFrame().evaluateJavaScript("alert('HelloD');")

    window = QtGui.QMainWindow()
    window.setCentralWidget(webView)
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
