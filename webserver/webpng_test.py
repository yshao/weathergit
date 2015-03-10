#!/usr/bin/env python
import sys
import signal

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import QWebPage, QWebView
import time


def onLoadFinished(result):
    if not result:
        print "Request failed"
        sys.exit(1)

    # # Set the size of the (virtual) browser window
    # webpage.setViewportSize(webpage.mainFrame().contentsSize())
    #
    # # Paint this frame into an image
    # image = QImage(webpage.viewportSize(), QImage.Format_ARGB32)
    # painter = QPainter(image)
    # webpage.mainFrame().render(painter)
    # painter.end()
    # image.save("output4.png")
    # sys.exit(0)
    webpage.page().mainFrame().evaluateJavaScript('getStreamData("0f6dc6f8-ac03-5fcb-9ae5-b9d9bb4dc2ed")')


def f():
    # Set the size of the (virtual) browser window
    webpage.page().setViewportSize(webpage.page().mainFrame().contentsSize())
    # webpage.page().setViewportSize(QSize(450,50))
    #
    # # # Paint this frame into an image
    rect=QRect(10, 20, 30, 40)
    image = QImage(webpage.page().viewportSize(), QImage.Format_ARGB32)
    # copy_image = image()

    painter = QPainter(image)
    webpage.page().mainFrame().render(painter)
    painter.end()
    image.save("output4.png")


app = QApplication(sys.argv)
signal.signal(signal.SIGINT, signal.SIG_DFL)

webpage = QWebView()

webpage.load(QUrl("http://192.168.1.120/status"))
webpage.connect(webpage, SIGNAL("loadFinished(bool)"), onLoadFinished)
# webpage.mainFrame().load(QUrl("http://192.168.1.120/status"))


webpage.show()

# Create a QTimer
timer = QTimer()
# Connect it to f
timer.timeout.connect(f)
# Call f() every 5 seconds
timer.start(3000)



# # sys.exit(0)

sys.exit(app.exec_())