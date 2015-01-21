from PyQt4.QtCore import pyqtSignal, pyqtSlot
from weathergit.gui.handlers.handler import Handler

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '1/21/2015' '12:06 PM'

class commandconsolewidgetHandler(Handler):

    sigSql=pyqtSignal(str)
    def __init__(self):
        ""
        super(commandconsolewidgetHandler, self).__init__()

    @pyqtSlot(list)
    def on_download_data(self,params):
        for p in params['paths']:
            param={}
            param['uuid']=p
            param=dict(params.items()+param.items())

            sql = "select data %(start_time)s %(end_time)s streamlimit %(stream_limit)s where uuid like '%(uuid)s'" % param
            print sql

        self.sigSql.emit(sql)
        # self.parent().ui.outSql.setText(sql)
        return sql

    @pyqtSlot(list)
    def on_download_data(self,params):
        for p in params['paths']:
            param={}
            param['uuid']=p
            param=dict(params.items()+param.items())

            sql = "select data %(start_time)s %(end_time)s streamlimit %(stream_limit)s where uuid like '%(uuid)s'" % param
            print sql

        self.sigSql.emit(sql)
        # self.parent().ui.outSql.setText(sql)
        return sql

    # def on_populate