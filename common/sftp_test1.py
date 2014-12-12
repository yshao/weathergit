import paramiko
paramiko.util.log_to_file('/tmp/paramiko.log')

# Open a transport

host = "192.168.1.146"
port = 22
transport = paramiko.Transport((host, port))

# Auth

password = "temppwd"
username = "debian"
keyfile='source_id_rsa'
pkey=paramiko.RSAKey.from_private_key_file(keyfile)

# transport.connect(username = username, pkey = pkey)
transport.connect(username = username, password=password)

# Go!

sftp = paramiko.SFTPClient.from_transport(transport)

# Download
filepath = '/home/debian/Desktop/weather/common/opc.ini'
localpath = 'c:/Demo/opc.ini'
try:

    print sftp.get(filepath, localpath)
except Exception,e:
    print e
    pass

# Upload

filepath = '/home/debian/Desktop/install.ini'
localpath = 'c:/install.ini'
sftp.put(localpath, filepath)

# Close

sftp.close()
transport.close()