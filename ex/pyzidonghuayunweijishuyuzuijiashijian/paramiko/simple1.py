#!/usr/bin/python
#coding:utf-8
#需要的第三方依赖
#yum install gcc libffi-devel python-devel openssl-devel
#pip install pycrypto
#pip install ecdsa
#pip install paramiko

import paramiko

hostname='192.168.74.129'
username='root'
password='198653'
paramiko.util.log_to_file('syslogin.log')

ssh=paramiko.SSHClient()
ssh.load_system_host_keys()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #本地测试需要这一句
#设置连接的远程主机没有本地主机密钥或HostKeys对象时的策略
#AutoAddPolicy自动添加主机名及主机密钥到本地的HostKeys对象
#RejectPolicy，默认，自动拒绝未知的主机名和密钥
#WarningPolicy，用于记录一个未知的主机密钥的Python警告

ssh.connect(hostname=hostname,username=username,password=password)
stdin,stdout,stderr=ssh.exec_command('free -m')
print stdout.read()
ssh.close()