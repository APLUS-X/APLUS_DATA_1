#!/usr/bin/env python3

from wordcloud import WordCloud
import matplotlib.pyplot as plt

#读取文件,返回一个字符串，使用utf-8编码方式读取，该文档位于此python同以及目录下
def word():
        f = open(u'text.txt','r',encoding='utf-8').read()
        wordcloud = WordCloud(
                background_color="white", #设置背景为白色，默认为黑色
                width=1500,               #设置图片的宽度
                height=960,               #设置图片的高度
                margin=10                 #设置图片的边缘
                ).generate(f)
        plt.imshow(wordcloud)   # 绘制图片
        plt.axis("off")         #消除坐标轴
        plt.show()              # 展示图片
        wordcloud.to_file('my_test2.png')# 保存图片
#word()

