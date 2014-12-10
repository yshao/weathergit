from abc import abstractmethod


class Invoker(object):
    ""

class Command():
    ""
    @abstractmethod
    def execute(self):
        ""


class CmdReceiver():
    ""
    @abstractmethod
    def build(self):
        ""

    def send(self):
        ""

class FetchCmdReceiver(CmdReceiver):
    ""

class OperateCmdReceiver(CmdReceiver):
    ""

class FetchCmd(Command):
    ""

class OperateCmd(Command):
    ""

class PostCmd(Command):
    ""
    def execute(self):
        """"""


