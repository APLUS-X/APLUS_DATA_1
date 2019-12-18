import scrapy
import re
import json
import urllib.parse
import redis

class TmallComment(scrapy.Spider):
	name = "tmall_comment"
	target_items = [
		{
			'item_id': '597060179425',    #id
			'seller_id': '760711426',    #userid
			'title': '小天才电话手表Z6 蜘蛛侠儿童防水定位中小学生4G全网通智能手表前后双摄视频拍照男女孩'
		# }, {
		# 	'item_id': '',
		# 	'seller_id': '',
		# 	'title': ''
		# }, {
		# 	'item_id': '',
		# 	'seller_id': '',
		# 	'title': ''
		}
	]
	url_comment = "https://rate.tmall.com/list_detail_rate.htm?itemId=%s&sellerId=%s&order=3&currentPage=%d&content=1&_ksTS=1567048240761_527&callback=jsonp528"
	headers = {
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
		"Referer": "https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.201441acBCakjK&id=597060179425&skuId=4148466284465&user_id=760711426&cat_id=2&is_b=1&rn=fe6b3762a40899d792a93e2ab92141cd"
	}
	cookies = {
		' cna': "3xExFbf7sQ4CAdxzt4TdqhjT",
		'lid': "davidp001",
		'otherx': "e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0",
		'x': "__ll%3D-1%26_ato%3D0",
		'enc': "XcFY7HDoqkE%2BoU54lan%2Bq%2FLF2qIXiUUcA5KF%2BYvTKpkH4YLygFZpBP6Ct7K%2F22D8dSZ6Ut8eBg5Hscorve%2BfcQ%3D%3D",
		'hng': "CN%7Czh-CN%7CCNY%7C156",
		'_m_h5_tk': "d0401549f40bcc4325987ae8077f1835_1566968777179",
		'_m_h5_tk_enc': "d4d3ee814e8aa2f40d90ccffcd0db36e",
		't': "3f1ea2be5fbca75c6d46ae747282dc15",
		'_tb_token_': "faeb00ef7be11",
		'cookie2': "135cf2b29ceed1555d1976f0a76bf345",
		'l': "cBrOZjRqqOFonb4FBOCiIZZP5N7TtIRfguWba1fXi_5Bv_Y6XtQOkum5REv6cjWhT3Lv4JuaUM2tVFTbJs70xZyCwTvQb",
		'isg': "BLS06dxtVYCIkcEu4YwtmS4ghXIsjdUaOdUpN04VCT_HuVUDe5_yB30_PbHEQRDP"
	}
	
	def __init__(self, **kwargs):
		self.pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, decode_responses=True)
		self.conn = redis.Redis(connection_pool=self.pool)
		self.conn.delete("tmall_comment")
		super(TmallComment, self).__init__(kwargs)
		
	def start_requests(self):
		for item in self.target_items:
			url = self.url_comment % (item['item_id'], item['seller_id'], 1)
			# TODO: get item title automatically
			request = scrapy.Request(url, headers=self.headers, cookies=self.cookies, callback=self.parse_item)
			request.meta['item'] = item
			yield  request

	def parse_item(self, response):
		item = response.meta['item']
		content = response.body.decode('utf8')
		json_string = content[content.find('{'): content.rfind('}') + 1]
		json_dict = json.loads(json_string)
		if json_dict.get('rateDetail', None) is None:
			yield response.request
		else:
			max_page = (int(json_dict['rateDetail']['rateCount']['total']) // 20) + 1
			for page in range(1, max_page + 1):
				url = self.url_comment % (item['item_id'], item['seller_id'], page)
				request = scrapy.Request(url, headers=self.headers, cookies=self.cookies, callback=self.parse_page)
				request.meta['item'] = item
				yield request

	def parse_page(self, response):
		item = response.meta['item']
		content = response.body.decode('utf8')
		json_string = content[content.find('{'): content.rfind('}') + 1]
		json_dict = json.loads(json_string)
		comment_list = json_dict['rateDetail']['rateList']
		result = dict()
		for comment in comment_list:
			result['content'] = comment.get('rateContent')
			append_comment = comment.get('appendComment')
			result['append'] = append_comment.get('content') if append_comment else None
			result['useful'] = comment.get('useful')
			result['color'] = comment.get('auctionSku')
			result['date'] = comment.get('rateDate')
			result['item_id'] = item['item_id']
			result['item'] = item['title']
			print(result)
			self.conn.lpush('jd_comment', json.dumps(result))


