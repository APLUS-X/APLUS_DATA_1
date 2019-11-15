# !/usr/bin/env python
# coding: utf-8
import urllib.request
import urllib.parse
import json
from tkinter import *
from tkinter import messagebox



def get_data(words):
    data = {}
    data["type"] = "AUTO"
    data["i"] = words
    data["doctype"] = "json"
    data["xmlVersion"] = "1.8"
    data["keyfrom:fanyi"] = "web"
    data["ue"] = "UTF-8"
    data["action"] = "FY_BY_CLICKBUTTON"
    data["typoResult"] = "true"
    data = urllib.parse.urlencode(data).encode('utf-8')
    return data


def url_open(url, data):
    req = urllib.request.Request(url, data)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0")
    response = urllib.request.urlopen(req)
    html = response.read()
    html = html.decode("utf-8")
    return html


def get_json_data(html):
    result = json.loads(html)
    result = result['translateResult']
    result = result[0][0]['tgt']
    return result


def main():
    content = entry.get()
    if content == '':
        messagebox.showinfo('提示','请输入要翻译的内容')
    else:
        # url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict.top"
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        data = get_data(content)
        html = url_open(url, data)
        result = get_json_data(html)
        res.set(result)
        print(result)


#def application():
root = Tk()
root.wm_attributes('-topmost',1)
root.title('翻译控件')
root.geometry('310x100')
root.geometry('+500+300')
label = Label(root,text='输入翻译的文字')
label.grid(row=0,column=0)
label1 = Label(root,text='翻译之后的结果:')
label1.grid(row=1,column=0)
entry = Entry(root,font=('微软雅黑',13))
entry.grid(row=0,column=1)
res = StringVar()
entry1 = Entry(root,font=('微软雅黑',13),textvariable=res)
entry1.grid(row=1,column=1)
button = Button(root,text="翻译",width=8,command=main)
button.grid(row=2,column=0,sticky=W)
button1 = Button(root,text='退出',width=8,command=root.quit)
button1.grid(row=2,column=1,sticky=E)
root.mainloop()

