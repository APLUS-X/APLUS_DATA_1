# !/usr/bin/env python

import os
from time import sleep

user_x, user_y = 2160, 1080
play_num = 99
print('刷金脚本运行···')


def aplus(x, y):
    base_x, base_y = 1920, 1080
    real_x = int(x / base_x * user_x)
    real_y = int(y / base_y * user_y)
    os.system('adb shell input tap {} {}'.format(real_x, real_y))

def a_plus(num):
    for i in range(num):
        if i < num:
            aplus(500, 500)  # 点击屏幕继续
            print("点击继续", end='->')
            sleep(1)
            aplus(1690, 990)  # 再次挑战
            print("点击再次", end='->')
            sleep(1)
            aplus(1422, 888)  # 闯关加载
            print("点击闯关", end='->')
            sleep(15)
            aplus(1866, 20)  # 跳过
            print('点击跳过动画', end='->')
            sleep(150)
            print(f'结束，已执行{i+1}次')

if __name__ == '__main__':
    a_plus(play_num)

# 再次挑战按钮坐标范围（1920X1080）：x: 1508 - 1758，y: 962 - 1030
# 闯关按钮坐标范围（1920X1080）: x: 1316 - 1560，y: 842 - 908
# 自动按钮坐标范围（1920X1080）：x: 1730 - 1824，y: 0 - 84
# 跳过按钮坐标范围（1920X1080）：x: 1782 - 1894，y: 26 - 64
