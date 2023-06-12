#!-*- coding:utf-8 -*-
# python3.7
# CreateTime: 2023/6/12 15:56
# FileName:

class Card:

    def __init__(self, attr):
        self._attr = str(attr)

    def __repr__(self):
        return self._attr

    @property
    def attr(self):
        return self._attr
