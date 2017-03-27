#!C:\Python27\python.exe
# _*_ coding:utf-8 _*_
"""
Our course project.
"""

import argparse, subprocess, sys, os


# Парсит вводимые аргументы
def super_funk():
    parser = argparse.ArgumentParser(
        description="[keys] [password] [local directory or file name] [destination(root@host)]")
    parser.add_argument("-P", action="store_const", help="--partial--progress", const="P")
    parser.add_argument("-v", "--verbose", action="store_const", help="increase output verbosity", const="v")
    parser.add_argument("-e", nargs=1, help="specify the remote shell to use")
    parser.add_argument("--pass=", nargs=1, help="password")
    parser.add_argument("-a", "--archive", action="store_const", help="archive mode", const="a")
    parser.add_argument("-S", "--sparse", action="store_const", help="handle sparse files efficiently", const="S")
    parser.add_argument("-q", "--quiet", action="store_const", help="suppress non-error messages", const="q")
    parser.add_argument("-i", "--itemize-changes", action="store_const", help="output a change-summary for all updates",
                        const="i")
    parser.add_argument("-z", "--compress", action="store_const", help="compress file data during the transfer",
                        const="z")
    parser.add_argument("extra_args", nargs=argparse.REMAINDER)
    return parser.parse_args().__dict__


# Собирает все ключи вместе
def concat_keys():
    key_e = super_funk()["e"]
    keys = []
    for _ in super_funk().values():
        if _ in list("PSvaqiz"):
            keys.append(_)

    if keys:
        keys = "".join(["-"] + keys)
    else:
        keys = ""

    if key_e is not None:
        key_with_e = keys + (" -e {}".format(key_e[0]))
    else:
        key_with_e = keys
    return key_with_e


# Все что не содержит "@" относит к источнику данных, остальное к пункту назначения данных
def source_dst():
    extra_args = super_funk()["extra_args"]
    source_dir = []
    destination = []
    for _ in extra_args:
        if "@" not in _:
            source_dir.append(_)
        else:
            destination.append(_)

    source = " ".join(source_dir)
    dst = " ".join(destination)
    return source, dst


# Забирает только IP адрес удаленной машины
def parse_ip():
    ip_str = source_dst()[1]
    index_split = ip_str.index("@")
    middle_ip_str = ip_str[index_split + 1:]
    index_final_split = middle_ip_str.index(":")
    final_ip_str = middle_ip_str[:index_final_split]
    return final_ip_str


# Пингует удаленную машину
def check_ping(hostname):
    response = subprocess.call(['ping', '-c', '3', hostname], stdout=open(os.devnull, 'wb'))

    if response == 0:
        print ("Network Active")
    else:
        print ("Network Error")
        sys.exit(1)


# При запуске из консоли выполняет следующие функции
if __name__ == "__main__":
    super_funk()
    concat_keys()
    source_dst()
    parse_ip()
    check_ping(parse_ip())
