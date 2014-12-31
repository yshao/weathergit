from weathergit.common.sourceclient import SourceClient
from weathergit.gui.command.command import Command


class OpenVNCCmd(Command):
    def __init__(self):
        ""
        # self.args=args

    def execute(self):
        ""
        sc=SourceClient()
