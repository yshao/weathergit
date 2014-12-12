
from gui.command.command import Command
from gui.configeditor import ConfigEditor


class OpenDialogCmd(Command):
    DIALOG={"ConfigEditor":ConfigEditor,}
    def __init__(self,args):
        self.args=args

    def execute(self):
        ""
        widget=self.DIALOG[self.args]
        widget.show()