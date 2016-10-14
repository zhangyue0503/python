#!/usr/bin/python
#网关模式文件上传与执行--未验证
from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.user='root'
env.hosts=['192.168.74.129']
env.password='198653'
env.passwords={
    'root@192.168.74.129:22':'198653'
}

lpackpath=""
rpackpath="/tmp/install"

@task
def put_task():
    run("mkdir -p /tmp/install")
    with settings(warn_only=True):
        result = put(lpackpath,rpackpath)
    if result.failed and not confirm("put file failed,Continue(Y/N)?"):
        abort("Aborting file put task!")

@task
def run_task():
    with cd("/tmp/install"):
        run("tar -zxvf lnmp0.9.tar.gz")
        with cd（"lnmp0.9"）:
            run("./centos.sh")

@task
def go():
    put_task()
    run_task()