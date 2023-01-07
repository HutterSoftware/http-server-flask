import os.path
import os
import sys


def read_file(file_path):
    file_path = file_path.replace("/", os.sep)
    file_path = os.getcwd() + file_path

    if not os.path.exists(file_path):
        sys.exit(-1)

    file = open(file_path, "r")
    content = file.read()
    file.close()

    return content


