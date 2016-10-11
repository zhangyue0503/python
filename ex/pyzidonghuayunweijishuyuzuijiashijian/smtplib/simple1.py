#!/usr/bin/python
import smtplib
import string

HOST='smtp.qq.com'
SUBJECT='Test email from Python'
TO="423257356@qq.com"
FROM="zhangyuecoder@qq.com"
text="Python rules them all!"
BODY=string.join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text
),"\r\n")

server=smtplib.SMTP()
server.connect(HOST,"25")
server.starttls()
server.login("149844827",'qblxghdwpeykbicc')
server.sendmail(FROM,[TO],BODY)
server.quit()