#!-*- coding:utf-8 -*-
# python3.7
# CreateTime: 2023/6/9 12:11
# FileName:

import random
from typing import List

from cardPool import CardPool
from user import User, Action
from card import Card
import constant
from utils import colors


class Process:

    def __init__(self, users: List[User]):
        self.users: List[User] = users
        self._card_pool = CardPool()

        self.__inflate()

    def __inflate(self):
        # 初始化用户牌组
        cards = []
        for _ in range(constant.EVERY_CARD_NUMBER):
            for attr in constant.CARD_ATTR_POOL:
                card = Card(attr)
                cards.append(card)
        cards = disarrange_array(cards)

        index = -1
        while cards:
            card = cards.pop()
            index = self.__get_next_user_index(index)
            user = self.users[index]
            user.add_cards([card])

    def __get_next_user_index(self, current_index):
        user_num = len(self.users)
        if current_index == user_num - 1:
            return 0
        else:
            return current_index + 1

    def select_standard_card(self, user):
        user.show()
        card = user.select_standard_card()
        self._card_pool.set_standard_card(card)

    def run(self):
        new_round = True            # 是否新的一轮
        end = False

        user_index = 0  # 当前用户的索引
        last_user_index = 0  # 上次出牌用户的索引
        while not end:
            user = self.users[user_index]

            if new_round:
                new_round = False
                self.select_standard_card(user)
                last_user_index = user_index
            else:
                self._card_pool.show_info()
                user.show()

                action = user.select_action() if last_user_index != user_index else Action.add_again
                if action == Action.pass_turn:
                    user_index = self.__get_next_user_index(user_index)
                elif action == Action.turn_over:
                    new_round = True
                    if self._card_pool.is_consistent():
                        user.add_cards(self._card_pool.clear_cards())
                        user_index = last_user_index
                    else:
                        self.users[last_user_index].add_cards(self._card_pool.clear_cards())
                else:
                    cards = user.select_cards()
                    self._card_pool.add_cards(cards)
                    last_user_index = user_index
                    user_index = self.__get_next_user_index(user_index)
            print('')

            # 当前用户牌组出完
            if len(user.cards) == 0:
                new_round = True
                if self._card_pool.is_consistent():
                    end = True
                    print(f'\n结束，{colors.magenta(user.name)}获胜')
                else:
                    user.add_cards(self._card_pool.clear_cards())

            # 一轮都pass
            if user_index == last_user_index and len(self._card_pool.cards) > 0:
                new_round = True
                self._card_pool.clear_cards()


def disarrange_array(array):
    """随机打乱数组"""
    new_array = random.sample(array, len(array))
    return new_array
