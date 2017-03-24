#!/usr/bin/env python
import subprocess

def check_ping(hostname):

    response = subprocess.call(['ping', '-c', '3', hostname])

    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"

    return pingstatus

pingstatus = check_ping('127.0.0.1')
print (pingstatus)
