#! /usr/bin/python

import subprocess
import pipes

import sys


def create_dir(path, host):
    response = subprocess.call(['ssh', host, 'mkdir -p ' + pipes.quote(path)])
    if not response:
        sys.exit()
    else:
        sys.exit(1)


def is_dir_present(path, host):
    response = subprocess.call(['ssh', host, 'test -d ' + pipes.quote(path)])
    return response


def remote_dir(path, host):
    if is_dir_present(path, host) == 0:
        sys.exit()
    elif is_dir_present(path, host) == 1:
        create_dir(path, host)
    else:
        sys.exit(1)

remote_dir("/mahaon/test/", "root@192.168.143.2")
