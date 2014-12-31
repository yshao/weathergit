
from weathergit.gui.command.command import Command
from weathergit.configeditor import ConfigEditor


class OpenDialogCmd(Command):
    DIALOG={"ConfigEditor":ConfigEditor,}
    def __init__(self,args):
        self.args=args

    def execute(self):
        ""
        widget=self.DIALOG[self.args]
        widget.show()