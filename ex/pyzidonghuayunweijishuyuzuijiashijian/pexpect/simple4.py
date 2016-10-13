#coding:utf-8
import pexpect
import sys

ip = "192.168.74.129"
user="root"
passwd="198653"
target_file="/root/pyproject/pyzidonghuayunweijishuyuzuijiashijian/pexpect/mylog.txt"

# 远程文件打包功能
child = pexpect.spawn('/usr/bin/ssh',[user+'@'+ip])
fout = file('mylog2.txt','w')
child.logfie = fout

try:
    child.expect('(?i)password')
    child.sendline(passwd)
    child.expect('#')
    child.sendline('tar -czf /root/pyproject/pyzidonghuayunweijishuyuzuijiashijian/pexpect/mylog.tar.gz '+target_file)

    child.expect('#')
    print child.before
    child.sendline('exit')
    fout.close()
except EOF:
    print "expect EOF"
except TIMEOUT:
    print "expect TIMEOUT"

# 将上面打包的文件拷贝的当前服务器的home目录里一份
child = pexpect.spawn('usr/bin/scp',[user+'@'+ip+':/root/pyproject/pyzidonghuayunweijishuyuzuijiashijian/pexpect/mylog.tar.gz','/home'])
fout = file('mylog2.txt','a')
child.logfile = fout
try:
    child.expect('(?i)password')
    child.sendline(passwd)
    child.expect(pexpect.EOF)
except EOF:
    print "expect EOF"
except TIMEOUT:
    print "expect TIMEOUT"