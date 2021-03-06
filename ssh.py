import paramiko
import time
import os

class SSH():
    def __init__(self,hostname,user_name,private_key):
        self.hostname = hostname
        self.user_name = user_name
        self.private_key = private_key 
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        self.client.connect(self.hostname, username=self.user_name, key_filename=self.private_key)
        return True

    def excute_command(self,command):
        self.connect()
        stdin, stdout, stderr = self.client.exec_command(command)
        for line in stdout:
            print(line.strip('\n'))
    
    def close(self):
        self.client.close()