import time
import sys
import live555
import threading

# Shows how to use live555 module to pull frames from an RTSP/RTP
# source.  Run this (likely first customizing the URL below:

# Example: python3 example.py 10.17.4.118 1 10 out.264 
# if len(sys.argv) != 5:
#   print()
#   print('Usage: python3 example.py cameraIP channel seconds fileOut')
#   print()
#   sys.exit(1)
  
# cameraIP = sys.argv[1]
cameraIP = '192.168.1.121'
# channel = sys.argv[2]
channel = 1
# seconds = float(sys.argv[3])
seconds = 10
# fileOut = sys.argv[4]
fileOut = 'out.264'


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