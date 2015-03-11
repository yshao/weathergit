import schedule
from smap.driver import SmapDriver
import time
from smap.util import periodicSequentialCall
from eventhandlers import Watchdog
from archiver import archive_files
from webgen import update_webpage

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/11/2015' '1:27 PM'

class Scheduler(SmapDriver):
    def setup(self, opts):
        self.dog=Watchdog()
        self.dog.watchdog()

        schedule.every(20).minutes.do(self.dog.update_status)
        schedule.every(5).minutes.do(update_webpage)
        schedule.every().day.at("1:00").do(archive_files)

    def poll_tasks(self):
        schedule.run_pending()

    def start(self):
        periodicSequentialCall(self.poll_tasks).start(1)    # time.sleep(1)