#!-*- coding:utf-8 -*-
# python3.7
# CreateTime: 2023/7/11 19:03
# FileName: 执行命令

import subprocess


class Process:

    def __init__(self, exe='cmd', shell=True, cwd=None, echo=True, **options):
        """

        :param exe:
        :param shell:
        :param cwd: 执行路径
        :param echo: 是否打印命令
        :return:
        """
        self.exe = exe
        self.shell = shell
        self.cwd = cwd

        self.echo = echo

    def run(self, commands):
        for cmd in commands:
            if isinstance(cmd, (list, tuple)):
                cmd = subprocess.list2cmdline(cmd)
            if self.echo:
                cmd = subprocess.list2cmdline(["echo", 'Execute: ' + cmd.replace('&&', '[and]')]) + f' && {cmd}'

            cmd = f"start {self.exe} /k " + f'"{cmd}"'
            subprocess.Popen(cmd, shell=self.shell, cwd=self.cwd)
