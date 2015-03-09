import os
import time
import logging

from smap.util import periodicSequentialCall
from smap.driver import SmapDriver

# from hd264utils import get_snapshot
def get_timestamp():
    timestr = time.strftime("%Y%m%d%H%M%S")
    return timestr


class TrendnetDriver(SmapDriver):
    path = '/time'

    def setup(self, opts):
        self.host = opts.get('IPHost')
        self.port = int(opts.get('IPPort', 8020))
        self.save_dir=opts.get('SaveDir')
        self.rate = float(opts.get('rate', 1))

        self.log = logging.getLogger('Trendnet')

        self.set_metadata('/', {
            'Instrument/Manufacturer' : 'Trendnet',
            'Instrument/Model' : 'TV-IP310PI' })


        # self.conn = DbConn()

        ### create timeseries
        # if not self.inst.lookup(self.path):
        #     self.add_timeseries(self.path, '', data_type="double",timezone=self.tz)
        if not self.lookup(self.path):
            # self.add_timeseries(self.path, '', data_type="double",timezone=self.tz)
            self.add_timeseries(self.path, '', data_type="long")

        self.poll_snapshot()

    def poll_snapshot(self):
        ""
        timeidx=int(get_timestamp())
        print timeidx
        print self.rate

        from hd264utils import get_snapshot
        # print 'h'
        self.add(self.path,timeidx)
        imgpath=str(timeidx)+'.png'
        print imgpath
        imagepath=get_snapshot(imgpath)
        print imagepath
        print self.rate
        # imageidx=os.path.basename(imagepath)
        # self.conn.insert(imageidx)

        # self.inst.add(self.path, imageidx)

    def poll_timestamp(self):
        timeidx=int(get_timestamp())
        print timeidx
        self.add(self.path,timeidx)


    def start(self):

        periodicSequentialCall(self.poll_snapshot).start(300)