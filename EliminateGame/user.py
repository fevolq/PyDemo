#!-*- coding:utf-8 -*-
# python3.7
# CreateTime: 2023/6/12 15:56
# FileName:

from typing import List

from cardPool import CardPool
from card import Card
import constant
from utils import colors


class User:

    def __init__(self, name):
        self.name = name

        self._cards: List = []
        self._cards_dict = {}  # {card.attr: count}

        self._is_alive = True
        self._eliminate_num = 0

    def __repr__(self):
        return self.name

    @property
    def is_alive(self):
        return self._is_alive

    @property
    def eliminate_num(self):
        return self._eliminate_num

    def add_card(self, card: Card):
        if len(self._cards) >= constant.MAX_USER_CARDS:
            self._is_alive = False
            # raise Exception(f"{self._name}的牌池已达最大数量，不可再添加")
            return
        self.__add_card(card)
        self.__eliminate_card(card)

    def __add_card(self, card: Card):
        self._cards.append(card)

    def show_cards(self):
        return ', '.join([card.attr for card in self._cards]) if self._cards else '空'

    def __eliminate_card(self, card: Card):
        self._cards_dict[card.attr] = self._cards_dict.get(card.attr, 0) + 1
        if self._cards_dict[card.attr] >= constant.ELIMINATE_CARD_NUMBER:
            self._cards = list(filter(lambda item: item.attr != card.attr, self._cards))
            del self._cards_dict[card.attr]
            self._eliminate_num += 1
            print(f'消除卡牌：{colors.normal_magenta(card.attr)}')
            print(f'余下牌组：{self.show_cards()}')
        elif len(self._cards) >= constant.MAX_USER_CARDS:
            self._is_alive = False
            print(colors.normal_red('失败'))

    def action(self, card_pool: CardPool) -> int:
        def select(max_number):
            index = input('选第几张牌：')
            try:
                int(index)
            except:
                print(colors.red('请输入正整数：'))
                return select(max_number)
            if int(index) > max_number or int(index) <= 0:
                print(colors.red('请选择正确的数：'))
                return select(max_number)
            return int(index)

        print('\n当前用户：', colors.blue(self.name))
        print('当前卡池：', colors.white(card_pool.show_cards()))
        print('当前牌组：', colors.cyan(self.show_cards()))
        card_index = select(len(card_pool.cards)) - 1
        return card_index
