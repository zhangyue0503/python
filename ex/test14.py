
import re

f = open('data.txt','r',encoding='utf-8')
data = f.read()
f.close()


v = re.compile("href='([^']+)'")
print(v.findall(data))
for x in v.findall(data): print(x)

from t import app
app.printsm("aaa")
