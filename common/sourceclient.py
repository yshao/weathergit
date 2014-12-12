import re
import paramiko


class SourceClient(object):
    COMMAND=dict(CMD_RESTART="shutdown -r now",CMD_DATE="date '+%D %T'",CMD_DISKSPACE="df -h | grep rootfs")

    connected=False

    def __init__(self,login):
        self.login=login
        self.conn=paramiko.SSHClient()
        self.connect()

    def __init__(self):
        config=Config()
        login=config['']


        self.login=login
        self.conn=paramiko.SSHClient()
        self.sftp=paramiko.sftp_client.SFTP()
        self.connect()

    def connectSFTP(self):
        """"""
        def parse(res):
            """"""

        sftp=self.sftp
        sftp

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

        ssh=self.conn
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(**self.login)

        res = ssh.exec_command('cat /proc/version')
        parse(res)


    def send_cmd(self,cmd):
        """"""
        ssh=self.conn
        res = ssh.exec_command(self.COMMAND[cmd])

        if res[2].readlines() != '':
            return res[1].readlines()

    def send(self,str):

        ssh=self.conn
        res = ssh.exec_command(str)

        if res[2].readlines() != '':
            return res[1].readlines()

    def close(self):
        self.conn.close()






# class Command(object):
#
