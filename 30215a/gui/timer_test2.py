from PyQt4.QtCore import QTimer, QCoreApplication

app = QCoreApplication([])

timerCallback = lambda: onTimer()
myTimer = QTimer()
myTimer.timeout.connect(timerCallback)
myTimer.start(1000) #once a sec


def onTimer():
    print 1



app.exec_()