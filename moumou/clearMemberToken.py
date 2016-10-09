# -*- coding=UTF-8 -*-

import mm
import time

# sql = "DELETE FROM `mm_member_token` WHERE `expireTime` <= '%s'" % time.strftime("%Y-%m-%d %H:%I:%S", time.localtime( time.time() - 3600 * 24 * 60))
# print mm.executeMmDb(sql)


import os

print [d for d in os.listdir('.')]


L = ['Hello', 'World', 18, 'Apple', None]

E = [s.lower() for s in L if isinstance(s,str)]

print E