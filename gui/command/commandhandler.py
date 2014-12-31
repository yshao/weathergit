from PyQt4.QtCore import QThread


class CommandHandler(object):
    def __init__(self):
        """"""

    def proc(self,cmd):
        """"""
        out="OUT"
        err="ERR"
        print cmd
        t=QThread(cmd.execute)
        t.run()
        return out,err
