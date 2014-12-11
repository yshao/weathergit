#from utils import sigint

import functools
from PyQt4.QtCore import QTimer, QCoreApplication
app = QCoreApplication([])

def onTimer(initParams):
    print initParams
    print "HERE"
    # your code here...
def update():
    print "Upd"
myInitParams = "Init!"
timerCallback = lambda: onTimer(myInitParams)
myTimer = QTimer()
myTimer.timeout.connect(timerCallback)
myTimer.start(1000) #once a sec

t = QTimer()

t.start(500)
t.timeout.connect(update)

# use a timer to stop the event loop after some time
stopTimer = QTimer(timeout=app.quit, singleShot=True)
stopTimer.start(4000)

app.exec_()