#!/usr/bin/python
# _*_ coding:utf-8 _*_
"""
Config 
"""
import platform
import sys


class Config(object):
    def __init__(self):
        self.check_os()
        self.check_python()

    # Main function
    @classmethod
    def main(cls):
        if Config.check_python():
            if Config.check_os():
                Config.check_apps()
            else:
                sys.exit(1)

    # Checking system version
    @staticmethod
    def check_os():
        if platform.system() == "Linux":
            dist = platform.dist()
            return True, dist[0]
        else:
            print("You use the {} operating system to run the script, you must use Linux.".format(platform.system()))
            return False

    # Checking python version
    @staticmethod
    def check_python():
        if sys.version_info.major == 2:
            print ("You are using the appropriate version of the Python.")
            return True
        else:
            print("Yoy are using Python version {}, please use Python version 2.".format(sys.version_info.major))
            return True



    # Checking installed apps
    @staticmethod
    def check_apps():
        os_type = Config.check_os()[1]
        print(os_type)


Config.main()