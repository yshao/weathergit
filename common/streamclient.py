__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '2/23/2015' '4:20 PM'

class StreamClient(object):
  def __init__(self):
    self.rc=RDBClient()
    self.pc=DbConn()

  def del_stream(self,uuid):
    rc.delete(uuid)
    pc.delete(uuid)

  def update_attributes():
    fc.upload('')


class RDBClient(object):
    "Remote controlling real-time DB"
    def __init__(self):
        ""
        # self.fc=FabUtils()

    def exec_sql(self):
        ""
        # self.fc.rdbc_exec('')


    def status(self):
        ""

