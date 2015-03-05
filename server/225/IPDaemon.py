__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '2/25/2015' '9:26 AM'

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '2/19/2015' '4:08 PM'

import sys
import time
from daemon import Daemon

from server import Webpage


class MyDaemon(Daemon):
        def run(self):
               webpage = Webpage()
               webpage.run()

if __name__ == "__main__":
        daemon = MyDaemon('/tmp/server-daemon.pid')
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        daemon.restart()
                else:
                        print "Unknown command"
                        sys.exit(2)
                sys.exit(0)
        else:
                print "usage: %s start|stop|restart" % sys.argv[0]
                sys.exit(2)