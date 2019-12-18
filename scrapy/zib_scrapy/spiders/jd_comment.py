# -*- coding: utf-8 -*-
import scrapy
import re
import json
import urllib.parse
import redis

class JDComment(scrapy.Spider):
	name = 'jd_comment'
	keyword = '小天才电话手表'
	url_main = 'https://search.' \
	           'jd.com/Search?keyword=%s&psort=3&s=0&enc=utf-8'
	url_comment = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv4040&productId=%s&score=0&sortType=5&page=%d&pageSize=10&isShadowSku=0&fold=1"
	# item_id = '100003437575'
	headers = {
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
		"Referer": "https://item.jd.com/100003437575.html"
	}
	def __init__(self, **kwargs):
		self.pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, decode_responses=True)
		self.conn = redis.Redis(connection_pool=self.pool)
		self.conn.delete("jd_comment")
		super(JDComment, self).__init__(kwargs)

	def start_requests(self):
		yield scrapy.Request(self.url_main % urllib.parse.quote(self.keyword, encoding='utf8'), callback=self.parse_main , headers=self.headers)

	def parse_main(self, response):
		for index in range(1, 11):
			href = response.xpath("//div[@id='J_goodsList']/ul[@class='gl-warp clearfix']/li[%d]//div[@class='p-name p-name-type-2']/a/@href" % index).get()
			if href is None:
				break
			title = ''.join([selector.get() for selector in response.xpath(	"//div[@id='J_goodsList']/ul[@class='gl-warp clearfix']/li[%d]//div[@class='p-name p-name-type-2']/a/em//text()" % index)])
			item_id = re.search('\d+', href).group(0).strip()
			urls = [self.url_comment % (item_id, page) for page in range(100)]
			self.conn.hset('jd_id_mapping', item_id, title)
			for url_comment in urls:
				request = scrapy.Request(url_comment, callback=self.parse_comment, headers=self.headers)
				request.meta['id'] = item_id
				request.meta['title'] = title
				yield request


	def parse_comment(self, response):
		content = response.body.decode('gbk')
		json_string = content[content.find('{'): content.rfind('}') + 1]
		item_id = response.meta['id']
		title = response.meta['title']
		# if len(json_string) < 20:
		# 	yield response.request
		#
		json_dict = json.loads(json_string)
		comments = json_dict['comments']
		if comments != []:
			for comment in comments:
				result = {"content": comment['content'], "score": comment['score'], "time": comment['referenceTime'], 'color': comment['productColor'], 'itemid': item_id, 'item': title}
				print(result)
				self.conn.lpush('jd_comment', json.dumps(result))
