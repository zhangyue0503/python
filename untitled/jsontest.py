# -*- coding: UTF-8 -*-

import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

json1 = json.dumps(data)
print json1

json2 = json.loads('{"a": 1, "b": 2, "c": 3}')
print json2