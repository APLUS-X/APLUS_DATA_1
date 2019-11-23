# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import os
import random
import csv
import time
urls=[]
urlls=[]
datas=[]
i=0
def Download(name,url,dirname):
    dir=dirname+"//"
    path=os.path.join(dir,name)
    response=requests.get(url)
    try:
        with open(path,"wb") as f:
            f.write(response.content)
            f.close()
            global i
            i=i+1
    except Exception as e:
        print(e)
#获取每一个分类的URL和名字
def Geturl():
    resp=requests.get("http://www.27270.com/ent/meinvtupian/")
    resp.encoding="gbk"  #设置网页编码
    html=resp.text
    soup=BeautifulSoup(html,"html.parser")
    divSoup1=soup.find("div",attrs={"id":"NewTagListBox"})
    aas=divSoup1.find_all("a")
    for a in aas:
        tup=(a['href'],a.string)
        urls.append(tup)  #将主页面的各个分栏的链接和名字加入urls元组中
def GetImages(url,dirname):
    print("*"*50)
    if os.path.exists(dirname):
        pass
    else:
        os.mkdir(dirname)   #创建目录
    try:
        resp=requests.get(url)
        resp.encoding="gbk"  #设置网页编码
        html=resp.text
        soup=BeautifulSoup(html,"html.parser")
        divSoup=soup.find("ul",attrs={'class':'w110 oh Tag_list'})
        lis=divSoup.find_all("li")
        fp=open("meinv.csv","a",newline="")
        csv_writer=csv.writer(fp)
        for li in lis:
            img=li.find("img")
            alt=img['alt']
            name=alt+".jpg"      #图片的名字
            src=img['src']       #图片的下载地址
            tup=(name,src,dirname)
            Download(name,src,dirname)
            csv_writer.writerow(tup)
            print(tup)
            datas.append(tup)            #Download(data[0],data[1],dirname)
        fp.close()
    except Exception as e:
        print(e)
def GetUrls():
    Geturl()  #获取所有分栏的页面
    for url in urls:
        ur=url[0][:-5]    #将每个分栏的url链接去除最后的 .html
        for i in range(11):
            i+=1
            if i==1:
                uuu=ur+".html"
                a=(uuu,url[1])
                urlls.append(a)
            else:
                uuu=ur+"_"+str(i)+".html"
                a=(uuu,url[1])
                urlls.append(a)
def main():
    GetUrls()  #获取所有页面的url
    for ur in urlls:
        print(ur[0],ur[1])
        GetImages(ur[0],ur[1])
        time.sleep(3)  #没抓取一个页面延时3秒
if __name__=='__main__':
    start=time.time()
    main()
    end=time.time()
    print("一共爬去了%s张照片，一共花费了%s的时间"%(str(i),(end-start)))
