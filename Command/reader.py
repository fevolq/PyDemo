#!-*- coding:utf-8 -*-
# python3.7
# CreateTime: 2023/7/11 19:26
# FileName:

import json


class Reader:

    def __init__(self, file: str):
        self.file = file
        self.mod = ''
        self.data = {}

        self._read()
        assert isinstance(self.data, dict)

    def _read_json(self):
        with open(self.file.replace('\\', '/'), 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def _read(self):
        self.mod = self.file.split('.')[-1]
        if self.mod == 'json':
            self._read_json()
        else:
            raise Exception(f'The {self.mod} file format is not supported yet')


def read(file: str) -> dict:
    return Reader(file).data
