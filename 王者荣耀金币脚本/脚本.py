# !/usr/bin/env python

import os
from time import sleep


repeat_num = 100

print('刷金脚本运行···')
def aplus(x, y):
    os.system('adb shell input tap {} {}'.format(x, y))


def a_plus():
    aplus(500, 500)  # 点击屏幕继续
    print("点击继续")
    sleep(2)
    aplus(1800, 990)  # 再次挑战
    print("点击再次",end='->')
    sleep(2)
    aplus(1660, 900)  # 闯关加载
    print("点击闯关",end='->')
    sleep(15)
    aplus(1900, 10)  # 跳过
    print('点击跳过',end='->')
    sleep(2)
    aplus(1800, 50)  # 自动
    print("点击自动",end='->')
    sleep(200)
    print(f'结束····以执行{i + 1}次')
    a_plus()

if __name__ == '__main__':
    a_plus()
