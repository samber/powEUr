import os


def create_directory(directory):
    try:
        os.mkdir(directory)
    except:
        pass
