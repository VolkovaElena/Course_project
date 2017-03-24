#!C:\Python27\python.exe

import argparse
def super_funk():
    parser = argparse.ArgumentParser(description = "List of commands:")
    parser.add_argument("-p", action = "store_const", help = "--partial--progress", const = "P")
    parser.add_argument("-v", "--verbose", action = "store_const", help = "increase output verbosity", const = "v")
    # parser.add_argument("-e", action = "store_const", help = "--partial--progress", const = "e")
    parser.add_argument("local_dir", nargs = "*")
    parser.add_argument("remote_dir", nargs = "?")
    # parser.add_argument("a", nargs='1')
    arguments = parser.parse_args()
    # print (arguments.p)
    # print (arguments.verbose)
    # return arguments.__dict__
    print(arguments)


# def our_rsync():
#     our_list = super_funk()
#     print (our_list)
    # rsync /usr root@169.254.182.3


# our_rsync()
super_funk()
