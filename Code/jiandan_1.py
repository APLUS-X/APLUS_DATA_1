#! /usr/bin/python3
# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import random


def get_ua():
    first_num = random.randint(55, 78)
    third_num = random.randint(0, 3200)
    fourth_num = random.randint(0, 140)
    os_type = [
        '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)', '(X11; Linux x86_64)',
        '(Macintosh; Intel Mac OS X 10_12_6)'
    ]
    chrome_version = f'Chrome/{first_num}.0.{third_num}.{fourth_num}'
    ua = ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
                   '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
                  )
    return ua


index = 0
headers = {'referer': 'http://jandan.net/',
           'user-agent': get_ua()}


# 保存图片
def save_jpg(res_url):
    global index
    html = BeautifulSoup(requests.get(res_url, headers=headers).text)#'features="lxml"
    for link in html.find_all('a', {'class': 'view_img_link'}):
        with open('{}.{}'.format(index, link.get('href')[len(link.get('href'))-3: len(link.get('href'))]), 'wb') as jpg:
            jpg.write(requests.get("http:" + link.get('href')).content)
        print(f"正在抓取第{index}张图片")
        index += 1


#  抓取煎蛋妹子图片
if __name__ == '__main__':
    url = 'http://jandan.net/ooxx'
    num = int(input('输入需要下载的页数：'))
    for i in range(0, num):
        save_jpg(url)
        url = "http:" + BeautifulSoup(requests.get(url, headers=headers).text).find('a', {'class': 'previous-comment-page'}).get('href')
        # 'features="lxml"


