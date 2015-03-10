import schedule
import time
from jsonconfig import JsonConfig


class Scheduler(object):
    def __init__(self):
        ""
        self.sch=schedule

    def load_events(self):
        ""
        cfg=JsonConfig('event.json')
        for evt in cfg:
            self.register_event(evt)
        self.cfg=cfg

    def run(self):
        ""
        while True:
            self.sch.run_pending()
            time.sleep(1)

    def register_event(self,evt):
        min=evt['interval']
        action=evt['action']
        self.sch.every(min).minute.do(action)


def update():
        print "10 seconds working"


def update_notify(i):
    time.sleep(2)
    if i % 2 == 0:
        print i
        print "emailing"

    i += 1


# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
if __name__ == '__main__':
    i=10
    schedule.every(10).seconds.do(update)
    schedule.every(5).seconds.do(lambda: update_notify(i))
    while True:
        schedule.run_pending()
        time.sleep(1)