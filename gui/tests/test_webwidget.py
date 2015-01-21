import json

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '1/21/2015' '3:13 PM'


uuid=self.ui.uuidlist.currentText()




sql="select * where uuid = '%s'" % uuid

su = SmapUtils()
res=su.run_query(sql)

updateTree(res)

ww = WebWidget()

def updateTree(js):
    d=json.loads(js)


# camera

c = pycurl.Curl()
c.setopt(c.URL,"")
c.setopt(c.POST,1)
