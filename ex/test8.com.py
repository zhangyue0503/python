import urllib.request
web = urllib.request.urlopen('http://www.baidu.com')
content = web.read()
print(content)