from PyQt4.QtCore import pyqtSlot
from requests.packages.urllib3 import request

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '1/30/2015' '11:09 AM'


server="/home/stor"


fabclient=

def copy_files_list(src,dest):
    ""

def query_retrieve_image(params):
  ""

  params['uuid']='19210'
  sql= "select data %(start_time)s %(end_time)s streamlimit %(streamlimit)s where uuid = %(uuid)s" % params
  res=request.fetch(sql)



  files=[server+"/"+e+'.png' for e in res]


  fabclient.copy_list(res,local_path)


  return l_fileIdx



