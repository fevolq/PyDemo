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

    @staticmethod
    def adapter(scripts) -> list:

        def is_posix(value: str) -> bool:
            return not (value.find('/') > -1 or value.find('\\') > -1)

        result = []
        if isinstance(scripts, str):
            # 单条命令
            result = shlex.split(scripts, posix=is_posix(scripts))  # 用于将字符串按照 shell 命令语法进行分割的函数。posix=False不分隔路径
        else:
            # 多条命令
            for script in scripts:
                if isinstance(script, str):
                    tmp_result = shlex.split(script, posix=is_posix(script))
                else:
                    tmp_result = script
                result.extend(tmp_result)
                result.append('&&')
            result.pop()

        return result

    def _load(self):
        self.option = self.data['option']

        lines = self.data['lines']
        for line in lines:
            scripts = self.adapter(line['scripts'])

            for _ in range(0, line.get('process', 1)):
                self.lines.append(scripts)
