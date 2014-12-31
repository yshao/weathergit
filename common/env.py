

class Env(object):
    param={'HOME':'c:/Users/Ping/Workspace/weathergit'}
    def __init__(self):
        ""

    @classmethod
    def getpath(self,param):
        return self.param[param]
