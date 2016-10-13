#coding:utf-8
import pexpect
import sys

child = pexpect.spawn('ssh root@192.168.74.129')
fout = file('mylog.txt',w)
child.logfile = fout
#child.logfile = sys.stdout

child.expect("password:")
child.sendline('198653')
child.expect('#')
child.sendline('ls /home')
child.expect('#')

