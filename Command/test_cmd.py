#!-*- coding:utf-8 -*-
# python3.7
# CreateTime: 2023/7/11 17:01
# FileName: 测试subprocess.Popen

import subprocess

# # 可执行多条，但存在 引号与空格的问题
# commands = [
#     'python script_demo.py -n "a" && python script_demo.py -n "b" && python --version',
#     'python script_demo.py -n "a a"',
# ]
#
# for cmd in commands:
#     subprocess.Popen(['start', 'cmd', '/k', cmd], shell=True)


# # 解决了 空格与引号，但无法执行多条
# commands = [
#     ['python', 'script_demo.py', '-n', 'a', '&&', 'python', 'script_demo.py', '-n', 'b'],
#     ['python', 'script_demo.py', '-n', 'a a']
# ]
#
# for cmd in commands:
#     subprocess.Popen(['start', 'cmd', '/k', *cmd], shell=True)


# # 可执行多条，但存在空格问题
# commands = [
#     ['python', 'script_demo.py', '-n', 'a', '&&', 'python', 'script_demo.py', '-n', 'b', '&&', 'python', '--version'],
#     ['python', 'script_demo.py', '-n', 'a a'],
# ]
#
# for cmd in commands:
#     cmd = subprocess.list2cmdline(cmd)
#     subprocess.Popen(['start', 'cmd', '/k', cmd], shell=True)


commands = [
    ['python', 'script_demo.py', '-n', 'a', '&&', 'python', 'script_demo.py', '-n', 'b', '&&', 'python', '--version'],
    ['python', 'script_demo.py', '-n', 'a a'],
    ['python', 'script_demo.py', '--name', 'b b b'],
]

for cmd in commands:
    cmd = subprocess.list2cmdline(cmd)
    cmd = subprocess.list2cmdline(["echo", cmd.replace('&&', '[and]')]) + f' && {cmd}'
    cmd = "start cmd /k " + f'"{cmd}"'
    subprocess.Popen(cmd, shell=True)
