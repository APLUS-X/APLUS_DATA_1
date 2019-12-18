import scrapy
import re
import json
import urllib.parse
from urllib3.exceptions import ProxyError
# start -- main -- item --- sell
#                        |
#                        |- comment
# primary ver: index

class TmallSpider(scrapy.Spider):

	name = "tmall_spider"

	url_main = "https://list.tmall.com/search_product.htm?q=%s&sort=d&s=%d"
	url_comment = "https://dsr-rate.tmall.com/list_dsr_info.htm?itemId=%s&sellerId=%s"
	headers = {
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
		"Referer": "https://www.tmall.com"
	}
	headers_sell = {
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
		'Referer': 'https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.42.589d6494QFm3nM&id=592423348971&skuId=4253148334166&user_id=2607671235&cat_id=2&is_b=1&rn=6e61d7471c4a732ef04d5c65cc17b089'
	}
	cookies_sell = {
		't': '3f1ea2be5fbca75c6d46ae747282dc15',
		'thw': 'cn',
		'enc': 'XcFY7HDoqkE%2BoU54lan%2Bq%2FLF2qIXiUUcA5KF%2BYvTKpkH4YLygFZpBP6Ct7K%2F22D8dSZ6Ut8eBg5Hscorve%2BfcQ%3D%3D',
		'ucn': 'center',
		'mt': 'ci=0_0',
		'l': 'cBL5ONemqOFofHd-BOfN5Zaza7QT6IdbzsPPhdbiiICP9XADlVPAWZF2d5bkCnGVLse6R3rCLlQpBDY7Ky4EQWrr2D_7XPQl.',
		'isg': 'BFBQQTiCOZGZK-XS5YFO4jvTIZ6oGzSjRg7P_Eog5KtkhfIv8i1U8p_0WQ3AVew7',
		'cookie2': '185e8db441db6b6956af7729bc44915d',
		'_tb_token_': 'eab3b33d653ee'
	}

	def __init__(self, keyword, max_page, **kwargs):
		self.keyword = keyword
		self.max_page = int(max_page)
		super(TmallSpider, self).__init__( **kwargs)

	def start_requests(self):
		for page in range(0, self.max_page):
			request =  scrapy.Request(self.url_main % (urllib.parse.quote(self.keyword, encoding='gb2312'), page*60), callback=self.parse_main, headers=self.headers, cookies=self.cookies_sell)
			request.meta['page'] = page
			yield request

	def parse_main(self, response):
		page = response.meta['page']
		product = dict()
		for index in range(1, 61):
			product['index'] = index + page*60
			href = response.xpath("//div[@id='J_ItemList']/div[%d]/div[@class='product-iWrap']/p[@class='productTitle']/a/@href" % index).get()
			if href is None:
				yield response.request
			else:
				product['href'] = href
				product['price'] = response.xpath(	"//div[@id='J_ItemList']/div[%d]/div[@class='product-iWrap']/p[@class='productPrice']/em/@title" % index).get()
				product['store'] = ''.join(response.xpath("//div[@id='J_ItemList']/div[%d]/div[@class='product-iWrap']/div[@class='productShop']/a//text()" % index).getall()).replace('\n', '')
				yield product

				request = scrapy.Request("https:" + product['href'], callback=self.parse_item, headers=self.headers)
				request.meta['index'] = product['index']
				yield request

	def parse_item(self, response):
		index = response.meta['index']
		product = dict()
		product['index'] = index
		product['skuid'] = response.headers['at_itemid']
		product["title"] = response.xpath("//*[@id='J_DetailMeta']//div[@class='tb-detail-hd']/h1/text()").get().replace('\n', '').replace('\t', '').replace('\r', '')
		javascript = response.xpath('//script[1]/text()').get()
		url_sell = 'http:' + re.search("//mdskip\.taobao\.com/core/initItemDetail\.htm\?.+?\'", javascript).group(0)[:-1]
		request = scrapy.Request(url_sell, callback=self.parse_sell, headers=self.headers_sell, cookies=self.cookies_sell)
		request.meta['index'] = index
		# request.meta['proxy'] = "https://127.0.0.1:8888"
		yield request

		url_comment = self.url_comment % (response.headers['at_itemid'].decode(), response.headers['at_alis'][2:].decode())
		request = scrapy.Request(url_comment, callback=self.parse_comment, headers=self.headers_sell)
		request.meta['index'] = index
		yield request


	def parse_sell(self, response):
		index = response.meta['index']
		content = response.body.decode('gb2312')
		json_string = content[content.find('{'): content.rfind('}') + 1]
		if json_string.strip() == '':
			print(index)
			return
		print('json: ', json_string)
		json_dict = json.loads(json_string)
		product = dict()
		product['index'] = index
		try:
			if json_dict != {}:
				product["monthsell"] = json_dict['defaultModel']['sellCountDO']['sellCount']
				product['original_price'] = list(json_dict['defaultModel']['itemPriceResultDO']['priceInfo'].values())[0]['price']
		except KeyError:
			print("Error: ignore 1 item ")
			return
		yield product

	def parse_comment(self, response):
		index = response.meta['index']
		content = response.body.decode('gb2312')
		json_string = content[content.find('{'): content.rfind('}') + 1]
		print(json_string)
		json_dict = json.loads(json_string)
		product = dict()
		product['index'] = index
		try:
			if json_dict != {}:
				product["totalcomment"] = json_dict['dsr']['rateTotal']
				product['grade'] = json_dict['dsr']['gradeAvg']
		except KeyError:
			print("Error: ignore 1 item ")
			return
		yield product

