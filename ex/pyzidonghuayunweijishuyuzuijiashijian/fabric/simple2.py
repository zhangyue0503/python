#!/usr/bin/python
# 动态获取远程目录列表
from fabric.api import *

env.user='root'
env.hosts=['192.168.74.129']
env.password='198653'


@runs_once
def input_raw():
    return prompt("please input directory name:",default="/home")

def worktask(dirname):
    run("ls -l "+dirname)

@task
def go():
    getdirname = input_raw()
    worktask(getdirname)
