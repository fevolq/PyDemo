#!-*- coding:utf-8 -*-
# python3.7
# CreateTime: 2023/6/8 23:46
# FileName: 2048

import random


class Game:

    def __init__(self):

        # self.data = [
        #     [0, 0, 0, 0],
        #     [0, 0, 0, 0],
        #     [0, 0, 0, 0],
        #     [0, 0, 0, 0],
        # ]
        # self.row_num = len(self.data)
        # self.col_num = len(self.data[0])

        self.row_num = 4
        self.col_num = 4
        # self.data = [[0] * self.col_num] * self.row_num       # 会导致重复引用
        self.data = [[0 for _ in range(self.col_num)] for _ in range(self.row_num)]

        self.hint = False
        self.is_invalid_direction = False       # 方向移动是否有效
        self.add_new_num(num=2, init=True)

    def pretty_print(self):
        """
        s = 'abc'
        print(f'{s:5}')   # 左侧填充空格
        print(f'{s:<5}')  # 右侧填充空格
        print(f'{s:^5}')  # 两侧填充空格
        :return:
        """
        max_width = [max([len(str(self.data[i][j])) for i in range(self.row_num)]) for j in range(self.col_num)]    # 每列的最大长度
        for i in range(self.row_num):
            for j in range(self.col_num):
                print(f'{self.data[i][j]:^{max_width[j]}}', end=' '*2)
            print()

    def add_new_num(self, num=None, init=False):
        def gen_num():
            nums = [
                {'num': 2, 'weight': 27},
                {'num': 4, 'weight': 9},
                {'num': 8, 'weight': 3},
                {'num': 16, 'weight': 1},
            ]
            weighted_list = [item['num'] for item in nums for _ in range(item["weight"])]

            return random.choice(weighted_list)

        zero_positions = []
        for i in range(self.row_num):
            for j in range(self.col_num):
                if self.data[i][j] == 0:
                    zero_positions.append((i, j))

        if len(zero_positions) == 0:
            return

        i, j = random.choice(zero_positions)
        new_num = gen_num() if num is None else num
        self.data[i][j] = new_num

        if not init:    # 初始化时不再另外展示
            print('-' * 10)
            print(f'new: {new_num}')
            self.pretty_print()

    def is_over(self):
        """
        1. 相邻数字没有相等的
        2. 不存在为0的数字
        :return:
        """
        has_adjacent_equal = lambda items: any(list(map(lambda item1, item2: item1 == item2, items[:-1], items[1:])))
        result = []
        for i in range(self.row_num):
            result.append(has_adjacent_equal(self.data[i]))
        for j in range(self.col_num):
            result.append(has_adjacent_equal([self.data[i][j] for i in range(self.row_num)]))
        return not any(result) and all([i for row in self.data for i in row])

    def get_direction(self):
        """从键盘输入获取方向"""
        command = input('输入方向：')
        directions_command = {
            'up':    ['w', 8],      # 上
            'down':  ['s', 5],      # 下
            'left':  ['a', 4],      # 左
            'right': ['d', 6],      # 右
        }
        directions = {}
        for k, values in directions_command.items():
            for value in values:
                value = str(value).lower()
                if value in directions:
                    raise Exception('重复定义命令')
                directions[value] = k

        # 提示
        if str(command.lower()) in ('/help', '/h'):
            print('方位：[键盘命令]\n-------------')
            print(f'上：{directions_command["up"]}\n'
                  f'下：{directions_command["down"]}\n'
                  f'左：{directions_command["left"]}\n'
                  f'右：{directions_command["right"]}')
            return self.get_direction()

        return directions.get(str(command).lower(), 'down')

    @staticmethod
    def get_next_position(direction):
        def get_position(i, j):
            positions = {
                'up': (i + 1, j),
                'down': (i - 1, j),
                'left': (i, j + 1),
                'right': (i, j - 1),
            }
            return positions[direction]
        return get_position

    def handle(self, next_position, i_, j_):

        def loop(i, j):
            next_i, next_j = next_position(i, j)
            while i < self.row_num:
                init = self.data[i][j]
                if next_i > self.row_num - 1 or next_i < 0 or next_j > self.col_num - 1 or next_j < 0:
                    break

                next_value = self.data[next_i][next_j]
                if next_value == 0:
                    next_i, next_j = next_position(next_i, next_j)
                    continue

                if init == next_value or init == 0:
                    self.data[i][j] = init + next_value
                    self.data[next_i][next_j] = 0
                    next_i, next_j = next_position(next_i, next_j)
                    self.hint = True
                    self.is_invalid_direction = True
                    continue

                return loop(*next_position(i, j))

        loop(i_, j_)
        while self.hint:
            self.hint = False
            loop(i_, j_)

    def action(self, direction):
        next_position = self.get_next_position(direction)

        init_option = {
            'up': {'position': [0, 0], 'loop_direction': 1},  # 左上
            'down': {'position': [self.row_num - 1, 0], 'loop_direction': 1},  # 左下
            'left': {'position': [0, 0], 'loop_direction': 0},  # 左上
            'right': {'position': [0, self.col_num - 1], 'loop_direction': 0},  # 右上
        }
        init_position = init_option[direction]['position']
        loop_direction = init_option[direction]['loop_direction']
        loop_max = self.col_num if loop_direction else self.row_num

        while init_position[loop_direction] < loop_max:
            self.handle(next_position, *init_position)
            init_position[loop_direction] += 1

    def run(self):
        self.pretty_print()

        while True:
            self.action(self.get_direction())
            self.pretty_print()

            if self.is_invalid_direction:
                self.add_new_num()
                self.is_invalid_direction = False
            if self.is_over():
                print('游戏结束！！！')
                break


if __name__ == '__main__':
    Game().run()
