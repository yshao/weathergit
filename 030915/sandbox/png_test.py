import unittest

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '2/3/2015' '9:43 AM'


fformat=dict(
    timestamp='',
    ext='png',
)

fileformat='%(timestamp)s.%(ext)s' % fformat
imgParam=dict(compression=80,
    fileformat=fileformat,
    path='test',
    zip=True,
)





import zlib

def save_file(filep):
    ""
    with open(filep, "rb") as in_file:
        zipped = zlib.compress(in_file.read(), 9)

    return zipped

def decompress_file(filep):
    ""
    def decompress():
        ""
    with open(filep, "rb") as in_file:
        cfilep=decompress(in_file)

    save_file(cfilep)

def compress_file(filep):
    ""
    def compress(filep):
        ""

    with open(filep, "rb") as in_file:
        cfilep=compress(in_file)


    zip=save_file(cfilep)
    return zip

def open_file(filep):
    ""
    with open(filep, "wb") as out_file:
        out_file.write(filep)


class Png_Test(unittest.TestCase):
    def setUp(self):
        self.filep='testp.png'

    def test_save(self):
        # filep='testp.png'
        compressedp='compressed_testp.png'
        assert compress_file(self.filep) == open_file(compressedp)

    def test_open(self):
        compressedp='compressed_testp.png'
        assert open_file(compressedp) == decompress_file(self.filep)



