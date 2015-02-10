

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '2/9/2015' '4:38 PM'


from PyQt4.QtGui import QFileDialog

def selectFile(msg='select folder:',ext='*.*'):   #Open a dialog to locate the sqlite file and some more...
    path = str(QFileDialog.getExistingDirectory(None,"Select Directory"))
    # path = QtGui.QFileDialog.getOpenFileName(None, QString.fromLocal8Bit(msg),ext)
    # if path:
    #     for i in items.iteritems():
    #         i = path # To make possible cancel the FileDialog and continue loading a predefined db

    return path