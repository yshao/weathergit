import paramiko
import os

# def connection():
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     privatekey = os.path.expanduser('/home/rabia/private')
#     mkey = paramiko.RSAKey.from_private_key_file(privatekey)
#     ssh.connect('78.46.172.47', port=22, username='debian', password=temppwd, pkey=mkey)
#     stdin, stdout, stderr = ssh.exec_command('ls')
#     print stdout.readlines()

# connection()


# import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.146', username='debian', password='temppwd')

stdin, stdout, stderr = ssh.exec_command('ls')
print stdout.readlines()
ssh.close()

print "login using ids"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.146', key_filename='id_dsa', username="root",password='')

stdin, stdout, stderr = ssh.exec_command('cat /proc/version')
print stdout.readlines()
ssh.close()

