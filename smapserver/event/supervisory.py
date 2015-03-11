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


    def get_all_pids(self):
        d1=self.get_pids('smapserver')
        d2=self.get_pids('smapsource')
        d1.update(d2)
        return d1

    def get_pids(self,target):
        d=Remote.gen_login(target)
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

    def kill_pid(self,pid):
        ""
        remote=self.remote



    def restart(self,p):
        source=Remote.gen_login('smapsource')
        server=Remote.gen_login('smapserver')

        pids=self.get_all_pids()
        if p == 'trendnet.ini':
            remote=Remote(server)
            if p in pids.keys():
                self.kill_pid(pids['trendnet.ini'])

            remote.execute('')
        elif p == 'weather.ini':
            remote=Remote(source)
            if p in pids.keys():
                self.kill_pid(pids['weather.ini'])

            remote.execute('')
        elif p == 'scheduler.py':
            remote=Remote(server)
            if p in pids.keys():
                self.kill_pid(pids['scheduler.py'])

            remote.execute('')

