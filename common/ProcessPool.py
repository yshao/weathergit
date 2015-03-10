from weathergit.gui.commandset import CommandSet


__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '2/9/2015' '3:58 PM'

class ProcessPool(object):
    def __init__(self):
        ""
    @classmethod
    def gen_task(self,func):
        ""
        # task=Task(start=func)
        # task.sigLogger.connect(logger.s)
        # task.sigGuiUpdate.connect()

        # self.pool.append(task)

    @classmethod
    def gen_task_cmd(self,cmd):
        ""
        getattr(CommandSet, cmd)()
        # self.gen_task(func)



class Task(object):
    ""


# ProcessPool.gen_task_cmd("take_snapshot")