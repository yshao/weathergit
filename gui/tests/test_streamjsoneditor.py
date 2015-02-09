from common.weather.common.dbconn import DbConn

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '2/4/2015' '12:04 PM'


def build_widget(uuid):

    conn=DbConn()
    meta=conn.get_meta(uuid)

    widget=StreamJsonEditor(meta)
    widget.show()


def d2meta(d):
    ""
    s=''
    for k in d:
       s=s+k

    s.replace(':','=>')
    return s

class StreamJsonEditor():
    def __init__(self,meta):
        self.meta=meta
        self.uuid=meta['uuid']

        # self.connect(exit,SIGNAL('triggered()'),self.menuExit)


    # def close(self):
    #     widget.close()

    def commit(self):
        conn=DbConn()
        metastring=d2meta(self._guiGetData())

        conn.commit(self.uuid,metastring)

        conn.commit()
        #TODO: connect logger
        # logger.log('INFO')

    def _guiInit(self):
        for item in self.meta:

            self.ui.jsoneditor.addItem()


    def _guiGetData(self):
        d={}
        for item in self.meta:


            d[item[0]]=item[1]

        return d

uuid=


### main ###
task="open menu"

logger=XLogger()
self.ui.addWidget(logger)



action
actionAdd.triggered.connect(lambda: ConfigEditor.show())


### streamwidget ###

actionEdit.clicked.connect(lambda: build_widget(uuid))
actionUUIDReload.clicked.connect(lambda: self.update_uuid())
actionUUIDClearSelection.clicked.connect(lambda: self.ui.metaeditor.clear_selection())

### statuswidget ###

actionSendCmd.clicked.connect(lambda: self.ui.send_cmd(self.ui.inCmdSelct))

def _guiInit():
    # TODO: add self.ui.inCmdSelct.ad commands from cmdClient
    cmdClient=CommandClient

    cmdClient

    self.ui.addWidget(cmdClient)




actionUpdate.clicked.connect(lambda: self._guiUpdate())

### stream signals ###
selectSel(self.ui.rightTab.rtwidget.update_rtdisp())

def


### datawidget signals ###
actionSQLGen.clicked.connect(lambda: self._guiUpdate_Sql(self._guiGetData()))

def _guiGetData():
    ""

actionDownloadData.clicked.connect(lambda: self.download(self.ui.inFormatSelect))


