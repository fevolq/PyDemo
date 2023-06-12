#!-*- coding:utf-8 -*-
# python3.7
# CreateTime: 2023/6/9 16:59
# FileName:

from process import Process


def main():
    users = Process.gen_users()
    Process(users).run()


if __name__ == '__main__':
    main()
