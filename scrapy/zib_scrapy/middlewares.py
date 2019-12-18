# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import requests
from scrapy import signals
from scrapy.downloadermiddlewares.retry import RetryMiddleware, response_status_message
import redis
import random

from twisted.internet import defer
from twisted.internet.error import TimeoutError, DNSLookupError, \
	ConnectionRefusedError, ConnectionDone, ConnectError, \
	ConnectionLost, TCPTimedOutError
from urllib3.exceptions import ProtocolError, ProxyError, ProxySchemeUnknown
from twisted.web.client import ResponseFailed
from scrapy.core.downloader.handlers.http11 import TunnelError
from threading import Lock

class RandomProxyMiddleware(object):

	def __init__(self):
		with open('proxy_list', 'r') as f:
			proxies = f.read().split('\n')
			self.proxies = [proxy for proxy in proxies if len(proxy) > 5]
	# def __init__(self):
	# 	self.pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, decode_responses=True)
	# 	self.conn = redis.Redis(connection_pool=self.pool)

	def process_request(self, request, spider):
		exist_proxy = request.meta.get('proxy')
		if not exist_proxy:
			# proxy = requests.get("http://127.0.0.1:5010/get/").content.decode()
			proxy = random.choice(self.proxies)
			print("current proxy ip is " + proxy)
			request.meta['proxy'] = proxy

class RetryRandomProxyMiddleware_file(RetryMiddleware):
	EXCEPTIONS_TO_RETRY = (defer.TimeoutError, TimeoutError, DNSLookupError,
						   ConnectionRefusedError, ConnectionDone, ConnectError,
						   ConnectionLost, TCPTimedOutError, ResponseFailed,
						   IOError, TunnelError, ProtocolError, ProxyError, ProxySchemeUnknown)
	RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 400, 403]

	lock = Lock()

	def __init__(self, settings):
		with open('proxy_list', 'r') as f:
			proxies = f.read().split('\n')
			self.proxies = [proxy for proxy in proxies if len(proxy) > 5]
		super(RetryRandomProxyMiddleware_file, self).__init__(settings)

	def get_proxy(self):
		return random.choice(self.proxies)

	def delete_proxy(self, proxy):
		if proxy in self.proxies:
			self.proxies.remove(proxy)

	def process_request(self, request, spider):
		exist_proxy = request.meta.get('proxy')
		if not exist_proxy:
			proxy = self.get_proxy()
			print("current proxy ip is " + proxy)
			request.meta['proxy'] = proxy

	def process_response(self, request, response, spider):
		fail_proxy = request.meta.get('proxy')
		if not response.body or len(response.body) == 0:
			self.delete_proxy(fail_proxy)
			proxy = self.get_proxy()
			print(fail_proxy + " is failed")
			print("Retry: current proxy ip is " + proxy)
			request.meta['proxy'] = proxy
			return request
		if request.meta.get('dont_retry', False):
			return response
		if response.status in self.retry_http_codes:
			reason = response_status_message(response.status)
			self.delete_proxy(fail_proxy)
			print("Response status exception")
			return self._retry(request, reason, spider) or response
		return response

	def process_exception(self, request, exception, spider):
		if isinstance(exception, self.EXCEPTIONS_TO_RETRY) and not request.meta.get('dont_retry', False):
			fail_proxy = request.meta.get('proxy', False)
			if fail_proxy is not False:
				self.delete_proxy(fail_proxy)
			proxy = self.get_proxy()

			print("ErrorRetry: current proxy ip is " + proxy)
			request.meta['proxy'] = proxy
			return self._retry(request, exception, spider)

class RetryRandomProxyMiddleware_api(RetryMiddleware):
	EXCEPTIONS_TO_RETRY = (defer.TimeoutError, TimeoutError, DNSLookupError,
						   ConnectionRefusedError, ConnectionDone, ConnectError,
						   ConnectionLost, TCPTimedOutError, ResponseFailed,
						   IOError, TunnelError, ProtocolError, ProxyError, ProxySchemeUnknown)
	RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 400, 403]

	proxy_list = []
	lock = Lock()

	def get_proxy(self):
		self.lock.acquire()
		if not self.proxy_list:
			print('proxy pool is empty, getting new ip')
			for i in range(50):
				proxy = 'http://' + requests.get("http://127.0.0.1:5010/get/").content.decode()
				if len(proxy) > 5:
					self.proxy_list.append(proxy)

		proxy_ip = self.proxy_list.pop(0) if self.proxy_list else requests.get("http://127.0.0.1:5010/get/").content.decode()
		self.lock.release()
		if proxy_ip:
			self.proxy_list.append(proxy_ip)
		return proxy_ip

	def delete_proxy(self, proxy):
		proxy = proxy.replace('http://', '')
		requests.get("http://127.0.0.1:5010/delete/?proxy=%s" % proxy)
		if proxy in self.proxy_list:
			self.proxy_list.remove(proxy)

	def process_request(self, request, spider):
		exist_proxy = request.meta.get('proxy')
		if not exist_proxy:
			proxy = self.get_proxy()
			print("current proxy ip is " + proxy)
			request.meta['proxy'] = proxy

	def process_response(self, request, response, spider):
		fail_proxy = request.meta.get('proxy')
		if not response.body or len(response.body) == 0:
			self.delete_proxy(fail_proxy)
			proxy = self.get_proxy()
			print(fail_proxy + " is failed")
			print("Retry: current proxy ip is " + proxy)
			request.meta['proxy'] = proxy
			return request
		if request.meta.get('dont_retry', False):
			return response
		if response.status in self.retry_http_codes:
			reason = response_status_message(response.status)
			self.delete_proxy(fail_proxy)
			print("Response status exception")
			return self._retry(request, reason, spider) or response
		return response

	def process_exception(self, request, exception, spider):
		if isinstance(exception, self.EXCEPTIONS_TO_RETRY) and not request.meta.get('dont_retry', False):
			fail_proxy = request.meta.get('proxy', False)
			if fail_proxy is not False:
				self.delete_proxy(fail_proxy)
			proxy = self.get_proxy()

			print("ErrorRetry: current proxy ip is " + proxy)
			request.meta['proxy'] = proxy
			return self._retry(request, exception, spider)

class RetryRandomProxyMiddleware_redis(RetryMiddleware):
	EXCEPTIONS_TO_RETRY = (defer.TimeoutError, TimeoutError, DNSLookupError,
						   ConnectionRefusedError, ConnectionDone, ConnectError,
						   ConnectionLost, TCPTimedOutError, ResponseFailed,
						   IOError, TunnelError, ProtocolError, ProxyError, ProxySchemeUnknown)
	RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 400, 403]
	proxy_list = []
	lock = Lock()

	def __init__(self, settings):
		self.pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, decode_responses=True)
		self.conn = redis.Redis(connection_pool=self.pool)
		super(RetryRandomProxyMiddleware_redis, self).__init__(settings)


	def get_proxy(self):
		self.lock.acquire()
		if not self.proxy_list:
			print('proxy pool is empty, getting new ip')
			for i in range(30):
				self.proxy_list.append(self.conn.srandmember("proxy_set", 1)[0])

		proxy = self.proxy_list.pop(0) if self.proxy_list else self.conn.srandmember("proxy_set", 1)[0]
		self.lock.release()
		if proxy:
			self.proxy_list.append(proxy)
		return proxy

	def delete_proxy(self, proxy):
		print('delete', proxy)
		if proxy in self.proxy_list:
			self.proxy_list.remove(proxy)
		self.conn.srem("proxy_set", proxy)


	def process_request(self, request, spider):
		exist_proxy = request.meta.get('proxy')
		if not exist_proxy:
			proxy = self.get_proxy()
			print("current proxy ip is " + proxy)
			request.meta['proxy'] = proxy

	def process_response(self, request, response, spider):
		fail_proxy = request.meta.get('proxy')
		if not response.body or len(response.body) == 0:
			self.delete_proxy(fail_proxy)
			proxy = self.get_proxy()
			print(fail_proxy + " is failed")
			print("Retry: current proxy ip is " + proxy)
			request.meta['proxy'] = proxy
			return request
		if request.meta.get('dont_retry', False):
			return response
		if response.status in self.retry_http_codes:
			reason = response_status_message(response.status)
			self.delete_proxy(fail_proxy)
			print("Response status exception")
			return self._retry(request, reason, spider) or response
		return response

	def process_exception(self, request, exception, spider):
		if isinstance(exception, self.EXCEPTIONS_TO_RETRY) and not request.meta.get('dont_retry', False):
			fail_proxy = request.meta.get('proxy', False)
			if fail_proxy is not False:
				self.delete_proxy(fail_proxy)
			proxy = self.get_proxy()

			print("ErrorRetry: current proxy ip is " + proxy)
			request.meta['proxy'] = proxy
			return self._retry(request, exception, spider)

class ZibScrapySpiderMiddleware(object):
	# Not all methods need to be defined. If a method is not defined,
	# scrapy acts as if the spider middleware does not modify the
	# passed objects.

	@classmethod
	def from_crawler(cls, crawler):
		# This method is used by Scrapy to create your spiders.
		s = cls()
		crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
		return s

	def process_spider_input(self, response, spider):
		# Called for each response that goes through the spider
		# middleware and into the spider.

		# Should return None or raise an exception.
		return None

	def process_spider_output(self, response, result, spider):
		# Called with the results returned from the Spider, after
		# it has processed the response.

		# Must return an iterable of Request, dict or Item objects.
		for i in result:
			yield i

	def process_spider_exception(self, response, exception, spider):
		# Called when a spider or process_spider_input() method
		# (from other spider middleware) raises an exception.

		# Should return either None or an iterable of Request, dict
		# or Item objects.
		pass

	def process_start_requests(self, start_requests, spider):
		# Called with the start requests of the spider, and works
		# similarly to the process_spider_output() method, except
		# that it doesn’t have a response associated.

		# Must return only requests (not items).
		for r in start_requests:
			yield r

	def spider_opened(self, spider):
		spider.logger.info('Spider opened: %s' % spider.name)


class ZibScrapyDownloaderMiddleware(object):
	# Not all methods need to be defined. If a method is not defined,
	# scrapy acts as if the downloader middleware does not modify the
	# passed objects.

	@classmethod
	def from_crawler(cls, crawler):
		# This method is used by Scrapy to create your spiders.
		s = cls()
		crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
		return s

	def process_request(self, request, spider):
		# Called for each request that goes through the downloader
		# middleware.

		# Must either:
		# - return None: continue processing this request
		# - or return a Response object
		# - or return a Request object
		# - or raise IgnoreRequest: process_exception() methods of
		#   installed downloader middleware will be called
		return None

	def process_response(self, request, response, spider):
		# Called with the response returned from the downloader.

		# Must either;
		# - return a Response object
		# - return a Request object
		# - or raise IgnoreRequest
		return response

	def process_exception(self, request, exception, spider):
		# Called when a download handler or a process_request()
		# (from other downloader middleware) raises an exception.

		# Must either:
		# - return None: continue processing this exception
		# - return a Response object: stops process_exception() chain
		# - return a Request object: stops process_exception() chain
		pass

	def spider_opened(self, spider):
		spider.logger.info('Spider opened: %s' % spider.name)
