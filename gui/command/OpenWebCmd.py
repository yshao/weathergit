import webbrowser
from gui.command.command import Command


class OpenWebCmd(Command):
    def __init__(self,args):
        self.args=args
        print args

    def execute(self):
        ""
        # webbrowser.open ('file://'+ self.ui.inDataFolder.text())
        webbrowser.open (self.args)
