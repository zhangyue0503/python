#!/usr/bin/python
#查看本地及远程主机信息
from fabric.api import *

env.user='root'
env.hosts=['192.168.74.129']
env.password='198653'

@runs_once
def local_task():
    local('uname -a')

def remote_task():
    with cd('/root/pyproject'):
        run("ls -l")

