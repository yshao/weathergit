import re
import socket
import paramiko
import select

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect("9.9.9.9", 22, "username", "password")
channel = client.invoke_shell()
channel.settimeout(0.0)

while True:
    r, w, e = select.select([channel], [], [])
    try:
        console_data = ""
        while channel.recv_ready():
            console_data += channel.recv(1024)
        if len(console_data) == 0:
           print "\n*** EOF\n"
           break

        # Search console_data for console prompt
        # If found, start a serial console
        if re.search("->", console_data):
            channel.send("start -script SP/Console")
        elif re.search("y/n", console_data):
            channel.send("y\n")
        elif re.search("SOME STRING ON CONSOLE", console_data):
            print "Action completed"
            break
    except socket.timeout:
        pass
channel.close()
client.close()