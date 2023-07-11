#!-*- coding:utf-8 -*-
# python3.7
# CreateTime: 2023/7/11 17:01
# FileName:

import getopt
import sys

from process import Process
from command import Command
from reader import read


def main(file):
    commands = Command(read(file))
    Process(**commands.option).run(commands.lines)


if __name__ == '__main__':
    file_path = ''

    opts, _ = getopt.getopt(sys.argv[1:], "f:", ["file=", ])
    opts = dict(opts)
    if opts.get("-f"):
        file_path = str(opts.get("-f"))
    elif opts.get("--file"):
        file_path = str(opts.get("--file"))

    main(file_path)
