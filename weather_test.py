#!/usr/bin/env python3

import urllib.request
import json
import pickle

pickle_file = open('data.pkl','rb')
city = pickle.load(pickle_file)
password = input('城市:')
name = city[password]
file1 = urllib.request.urlopen('http://www.weather.com.cn/data/sk/'+name+'.html')
weather_html = file1.read().decode('utf-8')
weather_json = json.JSONDecoder().decode(weather_html)
weather_info = weather_json['weatherinfo']
print('城市：',weather_info['city'])
print('时间：',weather_info['time'])
print('温度：',weather_info['temp'])
print('风向：',weather_info['WD'])
print('风速：',weather_info['WSE'])
print('湿度：',weather_info['SD'])
print('APM值：',weather_info['AP'])
print('njd：',weather_info['njd'])



