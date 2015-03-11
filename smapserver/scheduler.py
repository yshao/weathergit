import schedule
import time
# from jsonconfig import JsonConfig
from common.jsonconfig import JsonConfig



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



# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

# from event.archiver import archive_files
from event.eventhandlers import update_status
from event.webgen import update_webpage

if __name__ == '__main__':
    update_status()


    # schedule.every().day.at("12:00").do(archive_files)
    schedule.every(5).minutes.do(update_webpage)
    schedule.every(30).minutes.do(update_status)
    # schedule.every(5).seconds.do(lambda: update_notify(i))
    while True:
        schedule.run_pending()
        time.sleep(1)