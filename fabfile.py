import os

from fabric.api import run, sudo, env, cd, local, prefix, put, lcd, settings
from fabric.contrib.files import exists, sed
from fabric.contrib.project import rsync_project

env.use_ssh_config = True

user = 'deploy'
kb_dir = '/var/www/knowledgebase'
project_dir = '.'
dist = 'debian'
host_count = len(env.hosts)
tmp_dir = '/tmp/uluru-platform' + str(os.getpid())

def _set_user_dir():
    global dist,user,kb_dir
    with settings(warn_only=True):
        issue = run('id ubuntu').lower()
        if 'id: ubuntu' in issue:
            dist = 'debian'
        elif 'uid=' in issue:
            dist = 'ubuntu'
            user = 'ubuntu'
            kb_dir = '/mnt/avos/knowledgebase'

def _clean_local():
    local("rm -rf %s" % (tmp_dir))

def _prepare_remote_dirs():
    _set_user_dir()
    if not exists(kb_dir):
        sudo('mkdir -p %s' % kb_dir)
        sudo('chown -R 755 %s' % kb_dir)
    sudo('chown %s %s' % (user, kb_dir))

def _prepare_local_knowledgebase(target, install="true"):
    local("mkdir -p %s" % tmp_dir)
    if install == "true":
        local("./gitbook.sh install && ./gitbook init" )
    local("./gitbook.sh build" )
    local("cp -rv _book/* %s" % tmp_dir )

def deploy_knowledgebase(target="stage", install="false", prod='cn'):
    global host_count
    _set_user_dir()
    if (host_count == len(env.hosts)):
        _prepare_local_knowledgebase(target, install)

    _prepare_remote_dirs()
    rsync_project(local_dir=tmp_dir + '/',
                  remote_dir=kb_dir,
                  delete=True)
    host_count -= 1
    if (host_count == 0):
       _clean_local()
