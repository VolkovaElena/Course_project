#!/usr/bin/env python
import subprocess
import sys
import os


def check_ping(hostname):
    response = subprocess.call(['ping', '-c', '3', hostname], stdout=open(os.devnull, 'wb'))

    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"
        sys.exit(1)

    return pingstatus


pingstatus = check_ping('127.0.0.1')
print(pingstatus)