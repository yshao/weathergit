from weathergit.common.driverconfig import JsonConfig

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '2/25/2015' '1:22 PM'

class Scheduler(object):
    def __init__(self):
        ""
        self.config=JsonConfig('sched.json').load()

    def run_all(self):
        ""



    def status(self):
        ""



sched=Scheduler()
Daemon.daemonize(sched)



