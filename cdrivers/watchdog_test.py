import time
import os

os.nice(20)
time.sleep(60)                  # Wait before starting
wd = open("/dev/watchdog", "w+")
while 1:
     wd.write("\n")
     wd.flush()
     time.sleep(5)
