#!-*- coding:utf-8 -*-
# python3.7
# CreateTime: 2023/6/9 12:10
# FileName:

from typing import List

from card import Card
import constant


class User:

    def __init__(self, name: str):
        self._name = name

        self._cards: List[Card] = []

    def __repr__(self):
        return self._name

    def show(self):
        info = f"""当前用户：{self._name}\n剩余卡牌：{', '.join(self.__cards_attr())}"""
        print(info)

    def __cards_attr(self):
        return [card.attr for card in self._cards]

    def __sort_cards(self):
        self._cards.sort(key=lambda item: item.attr)

    def select_standard_card(self) -> Card:
        attr = input(f'请指明卡牌[{", ".join(constant.CARD_ATTR_POOL)}]: ')
        if attr not in constant.CARD_ATTR_POOL:
            print('请确认后重新选择')
            return self.select_standard_card()
        return Card(attr)

    def add_cards(self, cards: List[Card]):
        self._cards.extend(cards)
        self.__sort_cards()

    def select_cards(self) -> [Card]:
        # 使用卡牌属性来进行选择
        attrs = input(f'请选择手牌：')
        split_attr = ' '
        if attrs.find(',') >= 0:
            split_attr = ','
        attrs = attrs.split(split_attr)

        result = []
        for attr in attrs:
            attr = attr.strip()
            if not attr:
                continue
            if attr not in self.__cards_attr():
                if len(result) > 0:     # 把已删除的重新添加
                    self.add_cards(result)
                    print('---手牌选择异常，请重新选择---')
                return self.select_cards()

            card = self.__del_cards_attr(attr)
            if card is not None:
                result.append(card)
        return result

    def __del_cards_attr(self, attr) -> Card:
        result = None
        for card in self._cards:
            if card.attr == attr:
                result = card
                self._cards.remove(card)
                break
        return result

    def select_action(self,):
        action = input('请选择操作（1-pass、2-翻牌、3-追加）：')
        try:
            assert int(action) in Action.all_actions()
        except:
            print('请确认后重新选择')
            return self.select_action()
        else:
            return int(action)

    @property
    def name(self):
        return self._name

    @property
    def cards(self):
        return self._cards


class Action:

    pass_turn = 1
    turn_over = 2
    add_again = 3

    @classmethod
    def all_actions(cls):
        return [cls.pass_turn, cls.turn_over, cls.add_again]
