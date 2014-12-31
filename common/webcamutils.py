from datetime import datetime
import httplib
import io
import os
import time
import unittest

from PIL import Image
from PIL import ImageDraw

import pytz
import datetime
import requests


def InitCamera():
    """routine to check camera is running"""
    print 'httpbin'

    url = 'http://217.126.89.102:8020/axis-cgi/mjpg/video.cgi'
    # files = {'file': open('cam.ini', 'rb')}
    # h= httplib.HTTP(,8020)
    r = requests.post(url)
    print r.text
    print r.headers['content-type']
    print r.encoding
    print r.text
    assert r.status_code == 200


def _get_timestamp():
    date= datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    # print date
    naive_date = datetime.datetime.strptime(date, "%Y-%m-%d %H-%M-%S")
    localtz = pytz.timezone('America/Denver')
    date_aware = localtz.localize(naive_date)
    # print(date_aware)   # 2013-10-21 08:44:08-07:00

    utc_date = date_aware.astimezone(pytz.utc)
    # print(utc_date)
    return utc_date


def get_snapshot(port,save_dir):
    h= httplib.HTTP(*port)
    h.putrequest('GET','/axis-cgi/mjpg/video.cgi')
    # h.putheader('Authorization', 'Basic %s' % base64.encodestring('%s:%s' % (username, password))[:-1])
    h.endheaders()
    errcode, errmsg, headers = h.getreply()
    print headers
    stream_file = h.getfile()
    start = time.time()
    end = start + 2
    while time.time() <= end:
        now = datetime.datetime.now()
        dte = str(now.day) + "-" + str(now.month) + "-" + str(now.year)
        dte1 = str(now.hour) + "-" + str(now.minute) + "-" + str(now.second) + "." + str(now.microsecond)
        date=_get_timestamp()
        cname = "Cam1-"+date.strftime("%Y-%m-%d %H-%M-%S")
        dnow = """Date: %s """ % dte
        dnow1 = """Time: %s""" % dte1

        idx=date

        # your camera may have a different streaming format
        # but I think you can figure it out from the debug style below
        source_name = stream_file.readline()    # '--ipcamera'
        content_type = stream_file.readline()    # 'Content-Type: image/jpeg'
        content_length = stream_file.readline()   # 'Content-Length: 19565'
        print 'confirm/adjust content (source?): ' + source_name
        print 'confirm/adjust content (type?): ' + content_type
        print 'confirm/adjust content (length?): ' + content_length

        # find the beginning of the jpeg data BEFORE pulling the jpeg framesize
        # there must be a more efficient way, but hopefully this is not too bad
        b1 = b2 = b''
        while True:
            b1 = stream_file.read(1)
            while b1 != chr(0xff):
                b1 = stream_file.read(1)
            b2 = stream_file.read(1)
            if b2 == chr(0xd8):
                break

        # pull the jpeg data
        framesize = int(content_length[16:])
        jpeg_stripped = b''.join((b1, b2, stream_file.read(framesize - 2)))

        # throw away the remaining stream data. Sorry I have no idea what it is
        junk = stream_file.readline()

        image_as_file = io.BytesIO(jpeg_stripped)
        image_as_pil = Image.open(image_as_file)
        draw = ImageDraw.Draw(image_as_pil)
        draw.text((0, 0), cname, fill="white")
        draw.text((0, 10), dnow, fill="white")
        draw.text((0, 20), dnow1, fill="white")
        img_name = cname+ ".jpg"
        img_path = os.path.join(save_dir, img_name)
        image_as_pil.save(img_path)

    return idx,img_path


def main():
    wdir = "workdir"
    time_count = 2
    idx,file_path=get_snapshot(('217.126.89.102',8020),wdir)
    print idx,file_path

    InitCamera()

if __name__ == '__main__':
    main()

class webcamutilsTest(unittest.TestCase):
    def setUp(self):
        ""

    def test_InitCamera(self):
        self.assertTrue(InitCamera())

    def test_getSnapshop(self):
        get_snapshot(('217.126.89.102',8020),"workdir")