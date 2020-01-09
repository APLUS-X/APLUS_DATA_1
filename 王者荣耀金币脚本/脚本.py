# !/usr/bin/env python

import os
from time import sleep


num = 100
print('刷金脚本运行···')


def aplus(x, y):
    os.system('adb shell input tap {} {}'.format(x, y))

def a_plus():
    for i in range(num):
        if(i > 0):
            print(f'再次开始，共{num}次')
        aplus(500, 500)   # 点击屏幕继续
        print("点击继续",end='->')
        sleep(1)
        aplus(1900, 990)  # 再次挑战
        print("点击再次",end='->')
        sleep(1)
        aplus(1600, 888)  # 闯关加载
        print("点击闯关",end='->')
        sleep(14)
        aplus(2100, 20)  # 跳过
        print('点击跳过动画',end='->')
        sleep(210)
        a_plus()

if __name__ == '__main__':
    a_plus()
