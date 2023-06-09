#!-*- coding:utf-8 -*-
# python3.7
# CreateTime: 2023/6/8 23:40
# FileName: 改变字符串顺序进行加密

from typing import Union
import random
import string
import unittest


# 加密
def encrypt(value: Union[str, int], space: int) -> str:
    """
    加密
    :param value:
    :param space: 间隔
    :return:
    """
    assert isinstance(space, int) and space > 0
    value = str(value)
    result = ''
    for i in range(0, space):
        for j in range(i, len(value), space):
            result += value[j]
    return result


# 解密
def decrypt(value: Union[str, int], space: int) -> str:
    assert isinstance(space, int) and space > 0
    value = str(value)
    result = ''

    min_group = len(value) // space
    remainder = len(value) % space
    group = min_group if remainder == 0 else min_group + 1
    for i in range(group):
        j = i
        step = group
        num = 0
        # 需要动态更改步长，故使用while
        while j < len(value):
            num += 1
            result += value[j]

            j += step
            if num == remainder:    # 表明剩余循环已不满足最大分组值
                step = min_group
            if i == group - 1 and remainder and step == min_group:
                break
    return result


def generate_random_string(length: int) -> str:
    """生成指定长度的随机字符串"""
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for _ in range(length))
    return result_str


def gen_random_int(min_num: int, max_num: int) -> int:
    """随机生成整数"""
    return random.randint(min_num, max_num)


class TestCrypt(unittest.TestCase):

    def test_crypt(self):
        for _ in range(100):
            test_string = generate_random_string(gen_random_int(20, 50))
            test_space = gen_random_int(3, 5)
            encrypt_result = encrypt(test_string, test_space)
            self.assertEqual(test_string, decrypt(encrypt_result, test_space))


if __name__ == '__main__':
    unittest.main()
