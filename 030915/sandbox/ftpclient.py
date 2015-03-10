import os
import re
import ftputil
import paramiko
from common.config import Config


class FtpClient(object):
    COMMAND=dict(CMD_RESTART="shutdown -r now",CMD_DATE="date '+%D %T'",CMD_DISKSPACE="df -h | grep rootfs")

    connected=False

    def __init__(self,login):
        self.login=login
        self.connect()


    def connect(self):
        """"""
        def parse(res):
            """"""
            #
            # res = stdin, stdout, stderr
            #
            m=None

            for ln in res[1].readlines():
                m = re.search(r'Linux version',ln)
                if m != None:
                    self.connected=True
                    return True

            return False,''

        print self.login
        ftp=ftputil.FTPHost(self.login)
        # ftp=self.conn
        res = ftp.exec_command('cat /proc/version')
        parse(res)


    # def send_cmd(self,cmd):
    #     """"""
    #     ssh=self.conn
    #     res = ssh.exec_command(self.COMMAND[cmd])
    #
    #     if res[2].readlines() != '':
    #         return res[1].readlines()
    #
    # def send(self,str):
    #
    #     ssh=self.conn
    #     res = ssh.exec_command(str)
    #
    #     if res[2].readlines() != '':
    #         return res[1].readlines()

    # def close(self):
    #     self.conn.close()
    #
    # def __del__(self):
    #     self.close()


config=Config("../common/weatherplotter.conf")
login=dict(ip=config['smap_source_host'],user=config['smap_source_user'],
           password=config['smap_source_password']
)



login=list([
config['smap_source_host'],config['smap_source_user'],
           config['smap_source_password']])

remote_folder="/home/debian/Desktop/weather/common"

folder="test1"
# localdir=os.path.join(config["LOCAL_DATA_DIR"],folder)

host= ftputil.FTPHost(login[0],login[1],login[2])

paramiko.sftp_client.SFTP()


c=FtpClient(login)


