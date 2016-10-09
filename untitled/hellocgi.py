#!C:/Python27/python.exe
# -*- coding: UTF-8 -*-

#windows下要写python.exe
#/var/local/python

# print "Content-type:text/html"
# print                               # 空行，告诉服务器结束头部

#apache cgi 一定要有上面这两个print

# print '<html>'
# print '<head>'
# print '<meta charset="utf-8">'
# print '<title>Hello Word - 我的第一个 CGI 程序！</title>'
# print '</head>'
# print '<body>'
# print '<h2>Hello Word! 我是来自菜鸟教程的第一CGI程序</h2>'
# print '</body>'
# print '</html>'

# import os
#
# print "Content-type: text/html"
# print
# print "<meta charset=\"utf-8\">"
# print "<b>环境变量</b><br>";
# print "<ul>"
# for key in os.environ.keys():
#     print "<li><span style='color:green'>%30s </span> : %s </li>" % (key,os.environ[key])
# print "</ul>"

# CGI处理模块
import cgi, cgitb

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()

# 获取数据
site_name = form.getvalue('name')
site_url  = form.getvalue('url')

print "Content-type:text/html"
print
print "<html>"
print "<head>"
print "<meta charset=\"utf-8\">"
print "<title>菜鸟教程 CGI 测试实例</title>"
print "</head>"
print "<body>"
print "<h2>%s官网：%s</h2>" % (site_name, site_url)
print "</body>"
print "</html>"