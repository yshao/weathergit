import re
from common.env import Env
from common.remote.remote import Remote

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/11/2015' '9:53 AM'


class Supervisory():
    def __init__(self):
        # self.remote=Remote(Remote.gen_login(target))
        self.cfg=Env().getConfig()
        self.pids=self.get_all_pids()
        self.source=Remote.gen_login('smapsource')
        self.server=Remote.gen_login('smapserver')

    def get_all_pids(self):
        d1=self.get_pids('smapserver')
        d2=self.get_pids('smapsource')
        d1.update(d2)
        return d1

    def get_pids(self,target):
        d=Remote.gen_login(target)
        # print d
        remote=Remote(d)

        res=remote.execute("ps aux | grep python | grep -v grep",d['base_dir'])
        res=res.splitlines()
        d={}

        for l in res:
            sl=re.split(r' *', l)
            k=sl[-1]
            v=sl[1]

            d[k]=v
            # print[1]
        return d

    def kill_all(self):
        self.pids=self.get_all_pids()
        l=['trendnet.ini','weather.ini','scheduler.py']
        for e in l:
            if e in self.pids:
                self.kill_pid(e)


    def restart_all(self):
        l=['trendnet.ini','weather.ini','scheduler.py']
        for e in l:
                self.restart(e)

    def kill_pid(self,p):
        ""
        if p == 'trendnet.ini':
            remote=Remote(self.server)
            # remote.execute('')
            remote.execute('kill -9 %s' % self.pids['trendnet.ini'])
        elif p == 'weather.ini':
            remote=Remote(self.source)
            remote.execute('kill %s' % self.pids['weather.ini'])
        elif p == 'scheduler.py':
            remote=Remote(self.server)
            remote.execute('kill %s' % self.pids['scheduler.py'])

    def check_pid(self,p):
        pids=self.get_all_pids()
        if p in pids.keys():
            return True
        else:
            return False


    def restart(self,p):
        # pids=self.get_all_pids()
        if p == 'trendnet.ini':
            remote=Remote(self.server)
            if p in self.pids.keys():
                self.kill_pid('trendnet.ini')

            remote.daemon('twistd smap trendnet.ini',self.server['base_dir'])
        elif p == 'weather.ini':
            remote=Remote(self.source)
            if p in self.pids.keys():
                self.kill_pid('weather.ini')

            print
            remote.daemon('twistd smap weather.ini',self.source['base_dir'])
        elif p == 'scheduler.py':
            remote=Remote(self.server)
            if p in self.pids.keys():
                self.kill_pid('scheduler.py')

            remote.daemon('python scheduler.py &',self.server['base_dir'])


if __name__ == '__main__':
    super=Supervisory()
    super.kill_all()
    super.restart_all()
    # d=super.get_all_pids()
    # print "SUPER"
    # print d
    # print super.check_pid('trendnet.ini')
    # print super.check_pid('weather.ini')

    # super.restart('scheduler.py')
    # super.restart('weather.ini')