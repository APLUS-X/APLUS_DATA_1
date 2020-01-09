# !/usr/bin/env python

import os
from time import sleep


repeat_num = 100

print('刷金脚本运行···')
def aplus(x, y):
    os.system('adb shell input tap {} {}'.format(x, y))

if __name__ == '__main__':
    for i in range(repeat_num):
        if(i > 0):
            aplus(1880, 990)  # 再次挑战
            print("再次")
            sleep(2)
        aplus(1660, 900)#闯关加载
        print("闯关")
        sleep(18)
        aplus(1800,50)#跳过
        sleep(2)
        aplus(1800, 50)#自动
        print("点击自动")
        sleep(190)
        aplus(500,500)#点击屏幕继续
        print("测试点击")
        sleep(2)
        print(f'执行次数{i+1}')
