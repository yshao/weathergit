__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '1/21/2015' '9:51 AM'

class TaskThread(QThread):
    ""
    def __init__(self,parser):
        ""
        super(TaskThread, self).__init__()
        tid=self.currentThreadId()


    # @log
    def run(self):
        ""