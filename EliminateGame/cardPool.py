#!-*- coding:utf-8 -*-
# python3.7
# CreateTime: 2023/6/9 17:01
# FileName:

import random
from typing import List

from card import Card
import constant


class CardPool:

    def __init__(self, is_all=True):
        self._cards: List[Card] = []
        self.__is_all = is_all  # 是否为初始牌堆
        self.__inflate()

    @property
    def cards(self):
        return self._cards

    def __inflate(self):
        if self.__is_all:
            """初始化牌池"""
            for _ in range(constant.EVERY_CARD_NUMBER):
                for attr in constant.CARD_ATTR_POOL:
                    card = Card(attr)
                    self.__add_card(card)
            self._cards = disarrange_array(self._cards)

    def __add_card(self, card: Card):
        self._cards.append(card)

    def add_card(self, card: Card):
        if self.__is_all:
            raise Exception("初始牌池不允许增加牌")
        if not isinstance(card, Card):
            raise Exception('牌池增加牌的类型异常')
        return self.__add_card(card)

    def del_card(self, index: int = 0):
        if index >= len(self._cards):
            return None
        return self._cards.pop(index)

    def show_cards(self):
        return [] if self.__is_all else self._cards

    def show_cards_attr(self):
        return ' , '.join([card.attr for card in self.show_cards()])


def disarrange_array(array):
    """随机打乱数组"""
    new_array = random.sample(array, len(array))
    return new_array
