#!-*- coding:utf-8 -*-
# python3.7
# CreateTime: 2023/6/9 12:14
# FileName:

import copy
from typing import List

from card import Card


class CardPool:

    def __init__(self):
        self._cards: List[Card] = []
        self._last_cards: List[Card] = []

        self._standard_card: Card = None

    def set_standard_card(self, card):
        self._standard_card = card

    def add_cards(self, cards: List[Card]):
        self._cards.extend(cards)
        self._last_cards = cards

    def show_info(self):
        print(f'当前标准为：{self._standard_card.attr}，牌池数量：{len(self._cards)}')

    def show_cards(self):
        print('最后的牌组：', ', '.join([card.attr for card in self._last_cards]))

    def is_consistent(self):
        self.show_cards()
        consistent = True
        for card in self._last_cards:
            if not card.is_consistent(self._standard_card):
                consistent = False
                break
        return consistent

    def clear_cards(self):
        cards = copy.deepcopy(self._cards)
        self.__re_init()
        return cards

    def __re_init(self):
        """重新初始化属性"""
        self._cards.clear()
        self._last_cards.clear()
        self._standard_card = None

    @property
    def cards(self):
        return self._cards
