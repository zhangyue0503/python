#!/usr/bin/python
import paramiko

username="ftpuser"
password="123456"
hostname="192.168.74.129"
port=22

try:
    t = paramiko.Transport((hostname,port))
    t.connect(username=username,password=password)
    sftp=paramiko.SFTPClient.from_transport(t)

    sftp.put("/home/ftpuser/info.db","/root/info.db")
    sftp.get("/root/info_1.db","/home/ftpuser/info_1.db")
    sftp.mkdir("/home/ftpuser/userdir",0755)
    sftp.rmdir("/home/ftpuser/userdir1")
    sftp.rename("/home/ftpuser/test.sh","/home/ftpuser/test.sh")

    print sftp.stat("/home/ftpuser/testfile.sh")
    print sftp.listdir("/home/ftpuser")
    t.close()

except Exception,e:
    print str(e)