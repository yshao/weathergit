import sys
from PyQt4 import QtGui, QtCore, QtWebKit 

class MainForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)

        self.tabWidget = QtGui.QTabWidget(self)        
        self.setCentralWidget(self.tabWidget)        
        self.loadUrl(QtCore.QUrl('http://qt.nokia.com/'))

    def loadUrl(self, url):    
        view = QtWebKit.QWebView()  
        view.connect(view, QtCore.SIGNAL('loadFinished(bool)'), self.loadFinished)
        view.connect(view, QtCore.SIGNAL('linkClicked(const QUrl&)'), self.linkClicked)
        view.page().setLinkDelegationPolicy(QtWebKit.QWebPage.DelegateAllLinks)
        self.tabWidget.setCurrentIndex(self.tabWidget.addTab(view, 'loading...'))
        view.load(url)

    def loadFinished(self, ok):
        index = self.tabWidget.indexOf(self.sender())
        self.tabWidget.setTabText(index, self.sender().url().host())

    def linkClicked(self, url):        
        self.loadUrl(url)

def main():
    app = QtGui.QApplication(sys.argv)
    form = MainForm()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()