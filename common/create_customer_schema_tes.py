'time'
import paramiko

'data'
''

'soil_temp'
'soil_humidity'

'location'

'wind_direction'

'precipitation'

'pressure'


class ServerClient(object):
    def __init__(self):
        """"""

    def connect(self):
        """"""
        self.ssh=paramiko


    def query(self,msg):

        ssh=self.ssh

        ssh.


    def close(self):
        self.ssh.close()

    def __del__(self):
        self.close()


sc=ServerClient()


### get from reading ###


rdb=Reading()




'query from '

### processing ###



### put into customer
config=Config('dbconn.conf')

login={'':'5432','host':}
db=DbConn(login)