#!-*- coding:utf-8 -*-
# python3.7
# CreateTime: 2023/6/9 12:14
# FileName:

class Card:

    def __init__(self, attr):
        self._attr = str(attr)

    def __repr__(self):
        return self._attr

    def is_consistent(self, card):
        """校验两个卡牌是否一致"""
        consistent = False
        if self._attr == card.attr:
            consistent = True
        return consistent

    @property
    def attr(self):
        return self._attr
