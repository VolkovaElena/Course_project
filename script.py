import os


def create_dir(path):
    path = path
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

create_dir('mahaon/test/')
