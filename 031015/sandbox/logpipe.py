__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '2/2/2015' '5:28 PM'
import logging
import threading
import os
import subprocess

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

class LogPipe(threading.Thread):

    def __init__(self, level):
        """Setup the object with a logger and a loglevel
        and start the thread
        """
        threading.Thread.__init__(self)
        self.daemon = False
        self.level = level
        self.fdRead, self.fdWrite = os.pipe()
        self.pipeReader = os.fdopen(self.fdRead)
        self.start()

    def fileno(self):
        """Return the write file descriptor of the pipe
        """
        return self.fdWrite

    def run(self):
        """Run the thread, logging everything.
        """
        for line in iter(self.pipeReader.readline, ''):
            logging.log(self.level, line.strip('\n'))

        self.pipeReader.close()

    def close(self):
        """Close the write end of the pipe.
        """
        os.close(self.fdWrite)

# For testing
if __name__ == "__main__":
    import sys

    logpipe = LogPipe(logging.INFO)
    with subprocess.Popen(['/bin/ls'], stdout=logpipe, stderr=logpipe) as s:
        logpipe.close()

    sys.exit
