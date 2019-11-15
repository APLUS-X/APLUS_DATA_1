#！/usr/bin/env python
# -*-coding:UTF-8-*-

#多态：不同对象对同一方法响应不同的行动
#斐波那契数列/黄金分割数列

def num_1 ():
    a,b = 0,1
    while b < 70:
        print(b,end='  ')
        #print(a)
        a,b = b,a+b
#num_1()
# def fad(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fad(n-1)+fad(n-2)
# result = fad(10)
# if result != -1:
#     print(result)

#变量属性
def number ():
    a,b,c,d,=20,5.5,True,4+3j
    print(type(a),type(b),type(c),type(d))
#number()

def string ():
    s = "Yes,he doesn't"
    print(s*2,type(s),len(s))
#string()

def List1 ():
    a = [1,2,3,4,5]
    b = [6,7,8,9]
    c = [9,8,2,6,5]
    d = c[:]
    f = [9,5,4,6,2,45,6]
    print(list(zip(f,c)))
    # 排序
    d.sort()
    print('d=',d)
    c.sort(reverse=True)
    print('c1=',c)
    # 翻转
    c.reverse()
    print('c=',c)
    #添加
    a.append('555')
    b.extend(['sss','ddd'])
    a.insert(1,'s')
    #删除
    a.remove('555')
    del b[4]
    s = b.pop(4)
    #打印
    print('a=',a)
    print('b=',b)
    print('a+b',a+b)
    #修改第一位数字赋值9
    a[0] = 9
    print(a)
    a[2:5] = []
    print('a=',a)
#List1()

#集合
def sets():
    a = {'tom','jion','tom','jack'}
    print(a)
    print('tom' in a)
    x = {'a','c','s','a','d','x','s'}
    y = {'c','s','k','r'}
    print(x,y)
    print('差集：',x-y)
    print('并集：',x|y)
    print('交集：',x&y)
    print('不同时存在：',x^y)
#sets()

#集合自动去重，可以用集合来去重，不可变集合--frozenset()
def set_1():
    s1 = {1,2,3,4,5,8,6,5,2,1,3,5,8,9,4}
    print(s1)
    s2= [1,2,3,4,5,8,6,5,2,1,3,5,8,9,4]
    s3 = list(set(s2))
    print(s3)
#set_1()

#字典
def dic():
    dic = {}
    tel = {'jack':1557,'tom':1320,'rose':1886}
    print(tel)
    tel['may'] = 4555
    print(tel)
    tel_1 = {'jack':1888}
    print(tel.update(tel_1))
    print(list(tel.keys()))
    x = {z: z**2 for z in (2,4,6,8,10)}
    print ((x))
#dic()
#clear--删除字典 copy--拷贝 fromkeys--键值 pop--栈弹出 get--宽松访问 update--更新
#keys()--返回字典键的应用  values()-- items()--  setdefault--不存在便添加

def counter ():
    sum = 0
    counter = 1
    while counter <=100:
        sum = sum + counter
        counter = counter +1
        print("sum of 1 until 100:%d"%sum)
#counter()

#print( list(range(0,50,3)))

#print([str(round(355/113, i)) for i in range(1, 17)])
#print(355/113)

#遍历
def bianli ():
    A = {'tom':173,'jie':160,'h':155}
    for k,s in A.items():
        print(k,s)
    for i,j in enumerate(A):
        print(i,j)
    #反向遍历
    for i in reversed(range(1,10,2)):
        print(i)
    #要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for f in sorted(set(basket)):
        print(f)
#bianli()

#平方立方表
def lifang ():
    for x in range (1,11):
        print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')
        print(repr(x*x*x).rjust(4))
        print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))
#lifang()

#递归调用自身
def recursion(n):
    print(n)
    recursion(n+1)
#recursion(1)

#二分查找
date = list(range(200))
def search(n,low,high,d):
    mid = int((low+high)/2)
    if low ==high:
        print('not find')
        return
    if d[mid] > n:
        print("go left:",low,high,d[mid])
        search(n,low,mid,d)
    elif d[mid] < n:
        print("go right:",low,high,d[mid])
        search(n,mid+1,high,d)
    else:
        print('find it:',d[mid])
#search(25,0,len(date),date)

import numpy as np
def matrix2():
    a = np.array([
                [1,2,1],
                [3,8,1],
                [0,4,1]
                ])
    print(a[:,1])
    #所有行，列索引为一
    print(a[:,0:2])
    #所有行，列索引为0,1
    print(a[1:3,:])
    #所有列，行是行的所有1,2
    print(a[1:3,0:2])
    #行索引为1,2，列索引为0,1
    print(a==1)
    b = (a[:,1]>=3)
    #在所有行，列为2，大于等于3
    print(b)
    print(a[b,:])
    s = (a[0:1,:])
    print(s.sum())
    #axis=1,计算行值，以列展示
    print(a.sum(axis=1))
    #axis=0，计算列值，结果以行展开
    print(a.sum(axis=0))

    """
    sum():计算数组元素的和；对于矩阵计算的结果为一个一维数组，需要指定行或者列； 
    mean():计算数组元素的平均值；对于举证计算的结果为一个一位数组，需要指定行或者列； 
    max():计算数组元素的最大值；对于矩阵计算结果为一个一维数组，需要指定行或者列。
    用于这些统计方法的数值类型必须是int或者float。
    """
#matrix2()

import time
import datetime
def datetext():
    #24小时制
    a = time.strftime("%Y/%m/%d %A %H:%M:%S")
    print(a)
    #12小时制
    s = time.strftime('%I:%M:%S')
    print(s)
    d = datetime.datetime.now()
    print('当前时间：%s'%d.isoformat())
#datetext()
"""
    %a 星期几的简写       %A 星期几的全称       %b 月分的简写 %B 月份的全称           %c 标准的日期的时间串 
    %C 年份的后两位数字 %d 十进制表示的每月的第几天     %D 月/天/年 %e 在两字符域中，十进制表示的每月的第几天 
    %F 年-月-日        %g 年份的后两位数字，使用基于周的年 %G 年分，使用基于周的年       %h 简写的月份名 
    %H 24小时制的小时     %I 12小时制的小时         %j 十进制表示的每年的第几天         %m 十进制表示的月份 
    %M 十时制表示的分钟数 %n 新行符 %p 本地的AM或PM的等价显示    %r 12小时的时间      %R 显示小时和分钟：hh:mm 
    %S 十进制的秒数   %t 水平制表符 %T 显示时分秒：hh:mm:ss      %u 每周的第几天，星期一为第一天 （值从0到6，星期一为0） 
    %U 第年的第几周，把星期日做为第一天（值从0到53）     %V 每年的第几周，使用基于周的年   %w 十进制表示的星期几（值从0到6，星期天为0） 
    %W 每年的第几周，把星期一做为第一天（值从0到53）     %x 标准的日期串 %X 标准的时间串 
    %y 不带世纪的十进制年份（值从0到99）               %Y 带世纪部分的十制年份 
    %z,%Z 时区名称，如果不能得到时区名称则返回空字符。 %% 百分号
"""

def s2q(s:int)->int:
	input_s = []  # 申请一个入栈
	output_s = []  # 申请一个出栈
	res = []
	for c in s:
		input_s.append(c)  # 压入栈

	while input_s:  # 代码整洁之道
		output_s.append(input_s.pop())  # 不为空就一直往外弹
	while output_s:
		#res = []  # 如果每次都写在里面泽每次循环时都申请一个[]

		res.append(output_s.pop())
		#print(res)
		#print(id(res))  # 打印内存地址可以发现规律
		#return res, id(res)  # 默认只会输出第一次的循环，优先级的概念
	return res
#print(s2q("asdhfkh"))

from wordcloud import WordCloud
import matplotlib.pyplot as plt
#词云
#读取文件,文档位于此python同以及目录下
def word():
        f = open(u'text.txt','r',encoding='utf-8').read()
        f = f.lower()
        wordcloud = WordCloud(
                background_color="white",   #设置背景为白色
                width=800,                 #设置图片的宽度
                height=660,                 #设置图片的高度
                margin=2                   #设置图片的边缘
                ).generate(f)
        plt.imshow(wordcloud)         # 绘制图片
        plt.axis("off")               #消除坐标轴
        plt.show()                    # 展示图片
        wordcloud.to_file('text.png') # 保存图片
#word()

#条件表达式（三元操作符）
def small_text():
    x,y = 4,5
    small = x if x < y else y
    print(small)
    #这两种用法相等
    if x > y:
        small = x
    else:
        small = y
    print(small)
# 语法: x if 条件 else y
#small_text()

'''
assert 3<4 断言
for x in range():
range([strat,] stop,[step=1])
       开始     结束   步数
'''

def continue_text():
    for i in range(1,10):
        if i%2 != 0:
            print(i)
            continue
        i +=2
        print(i)
#continue_text()
#数据过滤，返回True
#print(list(filter(None,[1,0,False,True])))
def odd_1():
    def odd(x):
        return x % 2
    temp = range(10)
    show = filter(odd,temp)
    print(list(show))
#print(list(filter(lambda x :x % 2,range(10))))
#odd_1()
#print(list(map(lambda x : x * 2,range(10))))

#阶乘
# def factorial(n):
#     result = n
#     for i in range(1,n):
#         result *=i
#     return result
# num = int(input('阶乘数字：'))
# re = factorial(num)
# print('%d阶乘是:%d'%(num,re))

#递归
def factor():
    def factorial(n):
        if n ==1:
            return 1
        else:
            return n * factorial(n-1)
    num = int(input('整数：'))
    resu = factorial(num)
    print(resu)
#factor()

#阶乘
def jiecheng():
    num = int(input('阶乘整数：'))
    for i in range(1,num):
        num *= i
    print('结果：',num)
#jiecheng()

#汉诺塔解法
def hannuo():
    def hanoi(n,x,y,z):
        if n ==1:
            print(x,'-->',z)
        else:
            hanoi(n-1,x,z,y)
            print(x,'-->',z)
            hanoi(n-1,y,z,x)
    n = int(input('层数'))
    hanoi(n,'x','y','z')
#hannuo()


# import os
# import time
# a = time.localtime(os.path.getatime("C:\Program Files\Adobe\Adobe Premiere Pro CC 2017"))
# print(a)
# try:
#     file_name = input('>')
#     with open(file_name+'.txt') as f:
#         for i in f:
#             print(i)
# except OSError as a:
#     print(str(a))
#     exit(-1)

#用1234四个数组成的所有不重复的三位数有多少个
def num_2():
    a = 0
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if i != j and i !=k and j != k:
                    a +=1
                    print(str(i) + str(j) + str(k),end=' ')
        print()
    print('共有'+str(a)+'个')
#num_2()

#求两个数的最小公倍数和最大公约数
def gongyueshu():
    a,b = int(input('输入一个数字:')),int(input('输入第二个数字：'))
    for i in range(a,0,-1):
        if a%i==0 and b%i==0:
            print('最大公约数：'+str(i),'最小公倍数：'+str(a*b//i))
            break
#gongyueshu()

#奇偶分离,出栈
def num_4():
    num = [16,448,54,23,56,154,979,1184]
    num.append(51)  # 末尾添加
    num.sort()#排序
    print(num)
    num_1 = []
    num_2 = []
    while len(num)>0:
        nums = num.pop()
        if(nums %2 == 0):
            num_1.append(nums)
        else:
            num_2.append(nums)
    print(num_1)
    print(num_2)
# num_4()

#已知x为非空列表，执行y=x[:]之后，id(x[0])==id(y[0])的值为多少
# x=[5]
# y = x[:]
# print(id(x[0]==id(y[0])))
#
# rq = __import__('requests')
# from bs4 import BeautifulSoup
# url = 'https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/exporters.html'
# hea = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
# html = rq.get(url=url,headers=hea)
# html.encoding='utf-8'
# print(str(html.text))

r = __import__('random')
class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)
    def move(self):
        self.x -=1
        self.y -=2
        print('位置:',self.x,self.y)
class Glodfish(Fish):
    pass
class Carp(Fish):
    pass
class Salomn(Fish):
    pass
class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('eat')
            self.hungry=False
        else:
            print('no')
# a =Fish()
# a.move()
# a.move()
# b = Shark()
# b.eat()
# b.eat()
# c = Salomn()
# c.move()
# c.move()
pass

import datetime

def dayofyear():
	year = input("请输入年份: ")
	month = input("请输入月份: ")
	day = input("请输入天: ")
	date1 = datetime.date(year=int(year),month=int(month),day=int(day))
	date2 = datetime.date(year=int(year),month=1,day=1)
	return (date1-date2).days+1

#print(dayofyear())

# from sys import getrefcount
# s = getrefcount('aa')
# print(s)


from time import time, localtime, sleep


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

# if __name__ == '__main__':
#     main()


class Person(object):
    """人"""
    def __init__(self, name, age):
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        self._age = age
    def play(self):
        print('%s正在愉快的玩耍.' % self._name)
    def watch_av(self):
        if self._age >= 18:
            print('%s正在观看爱情动作片.' % self._name)
        else:
            print('%s只能观看《熊出没》.' % self._name)
class Student(Person):
    """学生"""
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade
    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self, grade):
        self._grade = grade
    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))
class Teacher(Person):
    """老师"""
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        self._title = title
    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))
def main():
    stu = Student('王大锤', 15, '初三')
    stu.study('数学')
    stu.watch_av()
    t = Teacher('骆昊', 38, '老叫兽')
    t.teach('Python程序设计')
    t.watch_av()
# if __name__ == '__main__':
#     main()


from abc import ABCMeta, abstractmethod
class Pet(object, metaclass=ABCMeta):
    """宠物"""
    def __init__(self, nickname):
        self._nickname = nickname
    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass
class Dog(Pet):
    """狗"""
    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)
class Cat(Pet):
    """猫"""
    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)
def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()
# if __name__ == '__main__':
#     main()



#十大排序算法：
#1.冒泡排序：
list_1 = [1,9,84,65,12,48,65,15,35,45,87,16,49,156,45,165]
#print(sorted(list_1))

def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

#2.选择排序：
def selectionSort(arr):
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

#3插入排序：
def insertionSort(arr):
    for i in range(len(arr)):
        preIndex = i-1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex-=1
        arr[preIndex+1] = current
    return arr

#4希尔排序：
def shellSort(arr):
    import math
    gap=1
    while(gap < len(arr)/3):
        gap = gap*3+1
    while gap > 0:
        for i in range(gap,len(arr)):
            temp = arr[i]
            j = i-gap
            while j >=0 and arr[j] > temp:
                arr[j+gap]=arr[j]
                j-=gap
            arr[j+gap] = temp
        gap = math.floor(gap/3)
    return arr

#5归并排序：
def mergeSort(arr):
    import math
    if(len(arr)<2):
        return arr
    middle = math.floor(len(arr)/2)
    left, right = arr[0:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))
def merge(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0));
        else:
            result.append(right.pop(0));
    while left:
        result.append(left.pop(0));
    while right:
        result.append(right.pop(0));
    return result


#6快速排序：
def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left,(int, float)) else left
    right = len(arr)-1 if not isinstance(right,(int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
    return arr
def partition(arr, left, right):
    pivot = left
    index = pivot+1
    i = index
    while  i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index+=1
        i+=1
    swap(arr,pivot,index-1)
    return index-1
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


#7堆排序：
def buildMaxHeap(arr):
    import math
    for i in range(math.floor(len(arr)/2),-1,-1):
        heapify(arr,i)
def heapify(arr, i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1,0,-1):
        swap(arr,0,i)
        arrLen -=1
        heapify(arr, 0)
    return arr

#8计数排序：
def countingSort(arr, maxValue):
    bucketLen = maxValue+1
    bucket = [0]*bucketLen
    sortedIndex =0
    arrLen = len(arr)
    for i in range(arrLen):
        if not bucket[arr[i]]:
            bucket[arr[i]]=0
        bucket[arr[i]]+=1
    for j in range(bucketLen):
        while bucket[j]>0:
            arr[sortedIndex] = j
            sortedIndex+=1
            bucket[j]-=1
    return arr

#将数组中的元素都向前移一个位置
def ahead_one():
    a = [i for i in range(10)]
    b = a.pop(0)
    a.append(b)
    return a
# if __name__ =="__main__":
#     print(ahead_one())


import random

def make_score(num):
    score = [random.randint(0,100) for i in range(num)]
    return score
def less_average(score):
    num = len(score)
    sum_score = sum(score)
    ave_num = sum_score / num
    less_ave = [i for i in score if i < ave_num]
    return len(less_ave)
# if __name__=="__main__":
#     score = make_score(40)
#     print ("the number of less average is:",less_average(score))
#     print ("the every socre is[from big to small]:",sorted(score,reverse=True))

