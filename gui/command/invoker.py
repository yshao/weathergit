from weathergit.gui.command.commandhandler import CommandHandler


class Invoker(object):
    history=[]
    handler=CommandHandler()

    # def __init__(self, create_file_commands, delete_file_commands):
    #     self.create_file_commands = create_file_commands
    #     self.delete_file_commands = delete_file_commands
    #     self.history = []

    def __init__(self):
        ""


    def invoke(self,cmd):
        ""
        res=self.handler.proc(cmd)

        if res[1] != None:
            return True,res[0]

        return False,res[1]




    ### pyqt sig handler ###
    # def evt_openWebCmd(self):
    #     ""
    #     invoke()
    #
    # def evt_openToolCmd(self):
    #     ""
    #
    # def evt_testConnectionCmd(self):
    #     ""
    #
    # def evt_updateSMAPStatusCmd(self):
    #     ""
    #
    # def evt_sendSMAPServerCmd(self):
    #     ""

    # def create_file(self):
    #     print 'Creating file...'
    #     for command in self.create_file_commands:
    #         command.execute()
    #         self.history.append(command)
    #     print 'File created.\n'
    # def delete_file(self):
    #     print 'Deleting file...'
    #     for command in self.delete_file_commands:
    #         command.execute()
    #         self.history.append(command)
    #     print 'File deleted.\n'
    # def undo_all(self):
    #     print 'Undo all...'
    #     for command in reversed(self.history):
    #         command.undo()
    #
    #     print 'Undo all finished.'

