#!-*- coding:utf-8 -*-
# python3.7
# CreateTime: 2023/7/11 17:04
# FileName:

import time
import getopt
import sys


def main(n):
    print(n)
    print(f'type: {type(n)}, len: {len(n)}')
    time.sleep(len(n) * 3)
    print('end')


if __name__ == '__main__':
    name = 'abc'

    opts, _ = getopt.getopt(sys.argv[1:], "n:", ["name=", ])
    opts = dict(opts)
    if opts.get("-n"):
        name = str(opts.get("-n"))
    elif opts.get("--name"):
        name = str(opts.get("--name"))

    main(name)
