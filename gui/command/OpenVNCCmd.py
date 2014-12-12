from common.sourceclient import SourceClient
from gui.command.command import Command


class OpenVNCCmd(Command):
    def __init__(self):
        ""
        # self.args=args

    def execute(self):
        ""
        sc=SourceClient()
