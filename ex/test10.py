# import re
# text = "Hi, I am Shirley Hilton. I am his wife."
# m = re.findall(r"hi",text)
# if m:
#     print(m)
# else:
#     print('not match')


import time

localtime =  time.asctime( time.localtime(time.time()))
print ("本地时间为 :", localtime)

print( time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )

import calendar

cal = calendar.calendar(2016)
print (cal);