#!/usr/bin/env python

CODEC = 'UTF-8'
UNICODE_HELLO = u'''
Hello!
\u00A1Hola!
\u4F60\u597D!
\u3053\u3093\u306B\u3061\u306F!
'''

print 'Content-type:text/html;charset=%s\r' % CODEC
print '\r'
print '<html><head><title>Unicode CGI Demo</title></head><body>'
print UNICODE_HELLO.encode(CODEC)
print '</body></html>'