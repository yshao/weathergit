from PyQt4.QtCore import QUrl
from PyQt4.QtGui import QWidget

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/2/2015' '5:43 PM'

class WebView(QWidget):
    def __init__(self,name,url):
        ""
        super(WebView, self).__init__()
        self.setObjectName(name)
        self.url=url

    def load_page(self):
        self.load_page(QUrl(self.url))