import os
import time
import sys
import live555
import threading
from common.env import Env
from sysutils import run_command


def rtsp_pull_frames():
    cameraIP = '192.168.1.212'
    channel = 1
    seconds = 5
    fileOut = 'out.264'

    d=Env().getConfig()
    username=d['smap_ipcam_username']
    password=d['smap_ipcam_password']
    cameraIP=d['smap_ipcam_host']

    # TrendNet
    url = 'rtsp://admin:bestcamera@%s:554/Streaming/channels/%s' % (username,password,cameraIP, channel)
    fOut = open(fileOut, 'wb')

    #callback
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

    if os.path.exists(fileOut):
        return True
    else:
        return False


def convert_to_png(filep,outfilep):
    # os.remove(outfilep)
    cmd='ffmpeg -i %s -vcodec png -ss 1 -vframes 1 -an -f rawvideo %s' % (filep,outfilep)
    run_command(cmd)


def get_snapshot(outfilep):
    # outfilep=sys.argv[1]
    print 'snapshot'
    # print outfilep
    b=False
    while b == False:

        if rtsp_pull_frames():
            convert_to_png('out.264',outfilep)

        statinfo = os.stat(outfilep)
        print statinfo
        if statinfo.st_size > 100:
            b = True
        else:
            time.sleep(5)


    from fabric.context_managers import settings
    from fabfile import move_file

    with settings(host_string='data@192.168.1.223'):
        print 'moving: ' + outfilep
        move_file(outfilep)

    os.remove(outfilep)





# from fabric.main import main
#
# if __name__ == '__main__':
#     import sys
#     sys.argv = ['fab', '-f', __file__, 'move_file','outfilep']
#     main()
