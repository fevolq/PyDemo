#!-*- coding:utf-8 -*-
# python3.7
# CreateTime: 2023/6/9 12:09
# FileName:

from user import User
from process import Process


def main():
    users = [User(name) for name in ['Martin', 'Jack', 'Bruce']]
    Process(users).run()


if __name__ == '__main__':
    main()
