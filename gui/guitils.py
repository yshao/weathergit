from PyQt4.QtGui import QDialog

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/2/2015' '6:12 PM'

class LogoView(QDialog):
    def __init__(self):
        super(LogoView, self).__init__()


def open_dialog(dlg):
    dlg.show()