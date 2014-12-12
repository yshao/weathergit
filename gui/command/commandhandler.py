class CommandHandler(object):
    def __init__(self):
        """"""

    def proc(self,cmd):
        """"""
        out="OUT"
        err="ERR"
        print cmd
        cmd.execute()
        return out,err
