'''
Author : Febi Mudiyanto
Date   : 1 Februari 2022

This program for execute a command to many servers
'''

import subprocess

def sshClient(host, port, user, password, command):
    '''
    Function to connect to ssh server
    with given host, port, user, password and command
    and execute the command
    '''
    ssh = subprocess.Popen(["sshpass", "-p", password, 
                            "ssh", "-p", port, user + "@" + host, command],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = ssh.communicate()
    if stderr:
        print("Error: {}".format(stderr))
    else:
        print("Command success to IP : {}".format(host))

    

# Open file and read line by line then execute command
# My serverlist file like this -> nameOfContainer:root:password:ipAddress 
serverList = []
with open("serverlist") as fp:
    Lines = fp.readlines()
    for line in Lines:
        # change \n to ''
        line = line.strip()    
        server=line.split(":")
        serverList.append([server[1],server[2],server[3]])
    fp.close()

# Execute command on each server
cmd = "echo 'hello world' > testing.txt"
for server in serverList:
    user = server[0]
    password = server[1]
    host = server[2]
    port = '22'
    sshClient(host, port, user, password, cmd)

