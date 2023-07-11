#!-*- coding:utf-8 -*-
# python3.7
# CreateTime: 2023/7/11 19:20
# FileName: 读取配置，生成命令

import shlex


class Command:

    def __init__(self, data):
        self.data = data

        self.option = {}
        self.lines = []

        self._load()

    def _load(self):
        self.option = self.data['option']

        lines = self.data['lines']
        for line in lines:
            scripts = adapter(line['scripts'])

            for _ in range(0, line.get('process', 1)):
                self.lines.append(scripts)


def adapter(scripts) -> list:
    result = []
    if isinstance(scripts, str):
        # 单条命令
        result = shlex.split(scripts)
    else:
        # 多条命令
        for script in scripts:
            if isinstance(script, str):
                tmp_result = shlex.split(script)
            else:
                tmp_result = script
            result.extend(tmp_result)
            result.append('&&')
        result.pop()

    return result
