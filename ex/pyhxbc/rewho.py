import os
import re

f = os.popen('tasklist','r')
for eachLine in f:
    print re.split(r'\s\s+|\r',eachLine.rstrip())
f.close()