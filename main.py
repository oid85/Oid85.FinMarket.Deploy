import time
import os


def do():
    cmd = "git --version"
    returned_value = os.system(cmd)  # returns the exit code in unix
    print('returned value:', returned_value)


if __name__ == '__main__':
    do()
