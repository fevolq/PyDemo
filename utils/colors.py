#!-*- coding:utf-8 -*-
# python3.7
# CreateTime: 2022/11/4 18:06
# FileName: 颜色

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(30, 38)

# 加颜色函数
colorfy = lambda bold, color, target: "\033[%d;%dm%s\033[0m" % (bold, color, target)

# 高亮颜色函数
black = lambda target: colorfy(1, BLACK, target)
red = lambda target: colorfy(1, RED, target)
green = lambda target: colorfy(1, GREEN, target)
yellow = lambda target: colorfy(1, YELLOW, target)
blue = lambda target: colorfy(1, BLUE, target)
magenta = lambda target: colorfy(1, MAGENTA, target)
cyan = lambda target: colorfy(1, CYAN, target)
white = lambda target: colorfy(1, WHITE, target)

# 普通颜色函数
normal_black = lambda target: colorfy(0, BLACK, target)
normal_red = lambda target: colorfy(0, RED, target)
normal_green = lambda target: colorfy(0, GREEN, target)
normal_yellow = lambda target: colorfy(0, YELLOW, target)
normal_blue = lambda target: colorfy(0, BLUE, target)
normal_magenta = lambda target: colorfy(0, MAGENTA, target)
normal_cyan = lambda target: colorfy(0, CYAN, target)
normal_white = lambda target: colorfy(0, WHITE, target)


if __name__ == '__main__':
    print(black('black'))
    print(red('red'))
    print(green('green'))
    print(yellow('yellow'))
    print(blue('blue'))
    print(magenta('magenta'))
    print(cyan('cyan'))
    print(white('white'))

    print(normal_black('normal_black'))
    print(normal_red('normal_red'))
    print(normal_green('normal_green'))
    print(normal_yellow('normal_yellow'))
    print(normal_blue('normal_blue'))
    print(normal_magenta('normal_magenta'))
    print(normal_cyan('normal_cyan'))
    print(normal_white('normal_white'))
    pass
