from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSVR = 'smtp.163.com'
POP3SVR = 'pop.163.com'

who = 'zhangyue0503@163.com'
body = '''
From: %(who)s
To: %(who)s
Subject:test msg
Hello World!
''' % {'who':who}

sendSvr = SMTP(SMTPSVR)
sendSvr.login('zhangyue0503','1986yuehuan53')
errs = sendSvr.sendmail(who,[who],body)
sendSvr.quit()
assert len(errs)==0,errs
sleep(10)

recvSvr = POP3(POP3SVR)
recvSvr.user('zhangyue0503')
recvSvr.pass_('198653')
rsp,msg,siz = recvSvr.retr(recvSvr.stat()[0])
sep = msg.index('')
recvBody = msg[sep+1:]
assert body == recvBody