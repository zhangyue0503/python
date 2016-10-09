#!/usr/bin/env python

import cgi
from urllib import quote_plus

header = 'Content-type:text/html\n\n'
url = '/cgi-bin/friendsC.py'

errhtml = '''<html><head><title>
Friends CGI Demo</title></head>
<body><h3>ERROR</h3>
<b>%s</b><p>
<form><input type="button" value="Back" onclick="window.history.back()"></form></body></html>
'''

def showError(error_str):
    print header + errhtml % error_str


formhtml = '''<html><head><title>
Friends CGI Demo
</title></head>
<body><h3>Friends list for: <i>NEW USER</i></h3>
<form action="/cgi-bin/friendsC.py">
<b>Enter your Name:</b>
<input type="hidden" name="action" value="edit"/>
<input type="text" name="person" value="NEW USER" size="15"/>
<p><b>How many friends do you have?</b>
%s
</p>
<p>
<input type="submit" />
</p>
</form>
</body></html>'''

fradio = '<input type="radio" name="howmany" value="%s" %s />%s\n'
def showForm():
    friends = []
    for i in (0,10,25,50,100):
        checked = ''
        # if i==0:
            # checked = 'CHECKED'
        friends.append(fradio % (str(i),checked,str(i)))
    print '%s%s'% (header,formhtml % ''.join(friends))

reshtml = '''<html><head><title>
Friends CGI Demo</title></head>
<body><h3>Friends list for: <i>%s</i></h3>
Your name is:<b>%s</b>
<p><b>You have <b>%s</b> friends.
</body></html>
'''
def doResults(who,howmany):
    newurl = url+'?action=reedit&person=%s&howmany=%s'%\
                 (quote_plus(who),howmany)
    print header + reshtml % (who,who,howmany)

def process():
    error = ''
    form = cgi.FieldStorage()
    if 'person' in form:
        who = form['person'].value
    else:
        who = 'NEW USER'
    if 'howmany' in form:
        howmany = form['howmany'].value
    else:
        if 'action' in form and \
            form['action'].value == 'edit':
            error = 'Please select number of friends.'
        else:
            howmany = 0

    if not error:
        if 'action' in form:
            doResults(who,howmany)
        else:
            showForm()
    else:
        showError(error)

if __name__ == '__main__':
    process()


