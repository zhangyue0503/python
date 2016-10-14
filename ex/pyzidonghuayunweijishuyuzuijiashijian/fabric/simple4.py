#!/usr/bin/python
# coding=utf-8
# 文件打包、上传与校验
from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.user='root'
env.hosts=['192.168.74.129']
env.password='198653'

@task
@runs_once
def tar_task():
    with lcd("/root"):
        local("tar -czf index.tar.gz index.html")

@task
def put_task():
    run("mkdir -p /root/logs")
    with cd ('/root/logs'):
        with settings(warn_only=True):
            result = put("/root/index.tar.gz","/root/logs/index.tar.gz")
            if result.failed and not confirm("put file failed,Continue[Y/N]?"):
                abort("Aborting file put task!")

@task
def check_task():
    with settings(warn_only=True):
        lmd5 = local("md5sum /root/logs/index.tar.gz",capture=True).split(' ')[0]
        rmd5 = run("md5sum /root/logs/index.tar.gz").split(' ')[0]
    if lmd5==rmd5:
        print "OK"
    else:
        print "ERROR"

@task
def go():
    tar_task()
    put_task()
    check_task()