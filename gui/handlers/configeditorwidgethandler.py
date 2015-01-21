__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '1/21/2015' '12:03 PM'

from PyQt4.QtCore import pyqtSlot, pyqtSignal
from weathergit.gui.handlers.handler import Handler

class configeditorwidgetHandler(Handler):

    sigSql=pyqtSignal(str)
    def __init__(self):
        ""
        super(configeditorwidgetHandler, self).__init__()


    @pyqtSlot(list)
    def on_action_file_path_selct(self):
        ""
        path=openFileBrowse()


    # def on_populate


