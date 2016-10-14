#!/usr/bin/python
#coding=utf-8
#部署LNMP业务服务环境
from fabric.colors import *
from fabric.api import *
env.usr='root'
env.roledefs = {
    'webservers':['192.168.74.129'],
    'dbservers':['192.168.74.129']
}
env.passwords={
    'root@192.168.74.129:22':'198653'
}

@roles('webservers')
def webtask():
    print yellow("Install nginx php php-fpm...")
    with settings(warn_only=True):
        run("yum -y install nginx")
        run("yum -y install php-fpm php-mysql php-mbstring php-xml php-mcrypt php-gd")
        run("chkconfig --levels 235 php-fpm on")
        run("chkconfig --levels 235 nginx on")

@roles("dbservers")
def dbtask():
    print yellow("Install Mysql...")
    with settings(warn_only=True):
        run("yum -y install mysql mysql-server")
        run("chkconfig --levels 235 mysqld on")

@roles('webservers','dbservers')
def publictask():
    print yellow("Install epel ntp...")
    with settings(warn_only=True):
        run("rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm")
        run("yum -y install ntp")

def deploy():
    execute(publictask)
    execute(webtask)
    execute(dbtask)
