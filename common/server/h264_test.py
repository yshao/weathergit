import time
import sys
import live555
import threading

# Shows how to use live555 module to pull frames from an RTSP/RTP
# source.  Run this (likely first customizing the URL below:
cameraIP = '192.168.1.121'
channel = 1
seconds = 1
fileOut = 'buf.264'
SERVER_STORE_PATH

# TrendNet
url = 'rtsp://admin:bestcamera@%s:554/Streaming/channels/%s' % (cameraIP, channel)
fOut = open(fileOut, 'wb')

def oneFrame(codecName, bytes, sec, usec, durUSec):
  print('frame for %s: %d bytes' % (codecName, len(bytes)))
  fOut.write(b'\0\0\0\1' + bytes)

# Starts pulling frames from the URL, with the provided callback:
useTCP = False
live555.startRTSP(url, oneFrame, useTCP)

# Run Live555's event loop in a background thread:
t = threading.Thread(target=live555.runEventLoop, args=())
t.setDaemon(True)
t.start()

endTime = time.time() + seconds
while time.time() < endTime:
  time.sleep(0.1)

# Tell Live555's event loop to stop:
live555.stopEventLoop()

# Wait for the background thread to finish:
t.join()



### send to server ###
from fabfile import *
put(os.path.basename(fileOut),os.path.join(SERVER_STORE_PATH,fileout))