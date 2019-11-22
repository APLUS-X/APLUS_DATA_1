#! /usr/bin/python3
# -*- coding: UTF-8 -*-
#name:---XZY---



import requests
from lxml import etree

i = 0
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Referer": "https://www.mzitu.com/xinggan/"
        }

def start_request():
    num = int(input('输入抓取的页面数：'))
    for i in range(1, num):
        print("==========正在抓取%s页==========" % i)
        response = requests.get("https://www.mzitu.com/page/"+ str(i) + "/", headers=headers)
        html = etree.HTML(response.content.decode())
        xpath_data(html)

def xpath_data(html):
    global i
    src_list = html.xpath('//ul[@id="pins"]/li/a/img/@data-original')
    alt_list = html.xpath('//ul[@id="pins"]/li/a/img/@alt')
    for src, alt in zip(src_list, alt_list):
        file_name = str(i) + ".jpg"
        response = requests.get(src, headers=headers)
        print("正在抓取图片：" + file_name)
        try:
            path = str(r'E:\python_test_3\jiandan\27270\meizi\reptile\\'+file_name)
            with open(path, "wb") as f:
                f.write(response.content)
            i += 1
        except:
            print("==========文件名有误！==========")
if __name__ == '__main__':
    start_request()
