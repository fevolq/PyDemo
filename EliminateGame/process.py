#!-*- coding:utf-8 -*-
# python3.7
# CreateTime: 2023/6/9 16:59
# FileName:

from typing import List

from cardPool import CardPool
from user import User
import constant
from utils import colors


class Process:

    def __init__(self, users: List[User]):
        self.users = users
        self._card_pool = CardPool()
        self._show_pool = CardPool(is_all=False)

        self.__inflate()

    def __inflate(self):
        # 初始化用户牌组
        for user in self.users:
            for _ in range(constant.USER_CARD_NUMBER):
                card = self._card_pool.del_card()
                user.add_card(card)

        # 初始化展示牌组
        for _ in range(constant.MAX_SHOW_CARD_NUMBER):
            card = self._card_pool.del_card()
            self._show_pool.add_card(card)

        pass

    @staticmethod
    def gen_users(names=None):
        names = ['a', 'b', 'c'] if names is None else names
        return [User(name) for name in names]

    def _system_action(self):
        """系统动作"""
        card = self._card_pool.del_card()
        if card is None:
            return
        self._show_pool.add_card(card)

    def _action(self, user: User):
        card_index = user.action(self._show_pool)
        card = self._show_pool.del_card(card_index)
        user.add_card(card)
        self._system_action()

    def out_info(self):
        # 存活者
        alive_users = [user for user in self.users if user.is_alive]
        if alive_users:
            print(f'\n存活：{", ".join([user.name for user in alive_users])}')

        # 排行榜
        rank_users = {}
        for user in self.users:
            rank_users.setdefault(user.eliminate_num, []).append(user)
        rank_keys = list(rank_users.keys())
        rank_keys.sort(reverse=True)
        rank = 1
        print('---------排行---------')
        for key in rank_keys:
            print(f'\n第{colors.red(rank)}名：{", ".join([user.name for user in rank_users[key]])}，'
                  f'消除次数：{colors.normal_magenta(rank_users[key][0].eliminate_num)}')
            rank += 1

    def run(self):
        while len(self._show_pool.cards) > 0 and len(list(filter(lambda user_: user_.is_alive, self.users))) > 0:  # 牌池还有，且还有用户存活
            for index, user in enumerate(self.users):
                if not user.is_alive:
                    continue

                self._action(user)

                if len(self._show_pool.cards) == 0:
                    break

        self.out_info()
        pass
