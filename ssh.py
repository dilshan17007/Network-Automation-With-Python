from ssl import SSLSession
import paramiko
from getpass import getpass
import time


host= "ip address"
port=22
username = "user"
password = "password"


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname = host,
            port=port,
            username= username,
            password=password)

print("Successfull Loging to",host)



stdin, stdout, stderr = ssh.exec_command("show version")
time.sleep(.5)

print(stdout.read().decode())
    
ssh.close()



