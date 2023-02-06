import re

lst = re.findall("\d+", "我的电话号是：10086，我女朋友的电话是：10010")
print(lst)

lst = re.finditer("\d+", "我的电话号是：10086，我女朋友的电话是：10010")
print(lst)
for i in lst:
    print(i.group())

lst = re.search("\d+", "我的电话号是：10086，我女朋友的电话是：10010")
print(lst.group())

lst = re.match(r"\d+", "10086，我女朋友的电话是：10010")
print(lst.group())

obj = re.compile(r"\d+")

ret = obj.finditer("我的电话号是：10086，我女朋友的电话是：10010")
for it in ret:
    print(it.group())

