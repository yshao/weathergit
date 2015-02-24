__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '2/2/2015' '4:24 PM'


from xlwings import Range,Workbook

def upload_data(filep):
    ""


def guiGet(layout):
    for w in layout:
        field=w.field




def actionDownloadData():
    val=guiGet(self.layout)

    self.connect(lambda: handleDownload(guiGet(self.layout)))


def handleDownload():



def download_data(filep,ul):
    ""
    wb=Workbook.open(filep)
    wb.call()



    for uuid in ul:

        Range['A2']=uuid


if name == '__main__':
