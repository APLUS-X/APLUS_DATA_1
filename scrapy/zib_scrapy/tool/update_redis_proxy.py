# -*- coding: utf-8 -*-

import requests
import json
import redis
import re
import random
from lxml import etree
import urllib.parse
import time

def tmall_validation(proxy):
	headers = {
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
		"Referer": "https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.201441acBCakjK&id=597060179425&skuId=4148466284465&user_id=760711426&cat_id=2&is_b=1&rn=fe6b3762a40899d792a93e2ab92141cd"
	}
	cookies = {
		't': "537e3dd0ebe05052b8fd88e6fd2d5e7e",
		'_tb_token_': "f31baefaee3ee",
		'cookie2': "13ed938d65b06a48711ea4c6092e1611"
}
	try:
		protocol = re.findall("(.+?)://", proxy)[0]
		proxy_dict = {protocol : proxy}
		r = requests.get(
			"https://rate.tmall.com/list_detail_rate.htm?itemId=597060179425&spuId=1247468704&sellerId=760711426&order=3&currentPage=%s&content=1&_ksTS=1567048240761_527&callback=jsonp528" % random.randint(0, 30),
			headers=headers, cookies=cookies, proxies = proxy_dict, timeout=10)
		content = r.content.decode('utf8')
		json_string = content[content.find('{'): content.rfind('}') + 1]
		json_dict = json.loads(json_string)

		return (r.status_code == 200 and json_dict['rateDetail']['rateList'] is not [])
	except Exception:
		return False

def jd_validation(proxy):
	# url_test = "https://search.jd.com/Search?keyword=%E5%B0%8F%E5%A4%A9%E6%89%8D%E7%94%B5%E8%AF%9D%E6%89%8B%E8%A1%A8&psort=3&s=0&enc=utf-8"
	url_test = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv4040&productId=47745724918&score=0&" \
	           "sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1" % random.randint(0, 99)
	url_main = 'https://search.jd.com/Search?keyword=%s&psort=3&s=0&enc=utf-8'
	headers = {
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
		"Referer": "https://item.jd.com/100003437575.html"
	}
	protocol = re.findall("(.+?)://", proxy)[0]
	proxy_dict = {protocol: proxy}
	try:
		# response = requests.get(url_main % urllib.parse.quote('小天才电话手表', encoding='utf8'), headers=headers, proxies=proxy_dict, timeout=2)
		# tree = etree.HTML(response.content.decode())
		# href = tree.xpath("//div[@id='J_goodsList']/ul[@class='gl-warp clearfix']/li[1]//div[@class='p-name p-name-type-2']/a/@href")
		# if len(href) == 0:
		r = requests.get(url_test, headers=headers, proxies=proxy_dict, timeout=2)
		print(url_test)
		if(r.status_code == 200 and len(r.content) != 0):
			return True
		else:
			return False
	except Exception:
		return False

def wait(sec):
	print('wait %s second ' % sec)
	for i in range(sec):
		time.sleep(1)
		print('.', )
	print()

def update_proxy():
	pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, decode_responses=True)
	conn = redis.Redis(connection_pool=pool)

	
	json_list = requests.get("http://proxylist.fatezero.org/proxy.list").content.decode('utf8').split('\n')
	json_dict = [json.loads(json_str) for json_str in json_list if len(json_str) > 5]

	start = 147
	total = 0
	counter = 30
	for dict in json_dict:
		if dict["anonymity"] == "high_anonymous":

			total += 1
			if total < start:
				continue
			if total == 1:
				conn.delete('proxy_set')
			counter -= 1
			if counter == 0:
				wait(5)
				counter = random.randint(20, 40)

			proxy = dict["type"] + "://" + dict["host"] + ':' + str(dict["port"])
			if tmall_validation(proxy):
				conn.sadd('proxy_set', proxy)
				print(total, "Success saving", proxy)
			else:
				print(total, "Validation fail to", proxy)
if __name__ == '__main__':
	update_proxy()