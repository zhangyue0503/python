#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
import string
from email.mime.text import MIMEText

HOST='smtp.qq.com'
SUBJECT='Test email from Python'
TO="423257356@qq.com"
FROM="zhangyuecoder@qq.com"
text="Python rules them all!"

msg=MIMEText("""<table>
<tr><td bgcolor="#eee">试试1</td>
<td>试试2</td></tr>
<tr><td bgcolor="#eee">试试3</td>
<td>试试4</td></tr>
</table>
""","html","utf-8")

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
server.sendmail(FROM,[TO],msg.as_string())
server.quit()