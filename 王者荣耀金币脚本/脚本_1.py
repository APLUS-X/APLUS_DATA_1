# !/usr/bin/env python


import os
from time import sleep

def enter(x,y):
    os.system('adb shell input tap {} {}'.format(x, y))

def a_plus():
    enter(1659, 783)
    sleep(2)
    #进入冒险
    enter(1350, 400)
    sleep(2)
    #进入冒险模式
    enter(1200, 390)
    sleep(2)
    #进入挑战
    enter(450, 780)
    sleep(2)
    #选择废都
    enter(1200, 600)
    sleep(2)
    #选择地图
    enter(1660, 700)
    sleep(2)
    #选择级别
    enter(1660, 900)
    sleep(2)
    #下一步
    enter(1660, 900)
    sleep(2)
    #进入
    enter(1600, 888)
    sleep(15)
    #闯关
    sleep(180)
    #开始
    enter(950, 1000)
    sleep(1)
    #点击继续
    # 闯关按钮坐标范围（1920X1080）: x: 1316 - 1560，y: 842 - 908
    # 自动按钮坐标范围（1920X1080）：x: 1730 - 1824，y: 0 - 84
    # 跳过按钮坐标范围（1920X1080）：x: 1782 - 1894，y: 26 - 64
    # 再次挑战按钮坐标范围（1920X1080）：x: 1508 - 1758，y: 962 - 1030

def aplus():
    sleep(5)
    enter(1880, 990)
    #agane
    sleep(5)
    enter(1660, 900)
    #闯关
    sleep(180)
    enter(950, 1000)
    #点击继续
    aplus()

if __name__ == '__main__':
    a_plus()
    aplus()