import redis


pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, decode_responses=True)
conn = redis.Redis(connection_pool=pool)
conn.delete('proxy_set')
with open('./zib_scrapy/spiders/proxy_list', 'r') as f:
	proxy_list = f.read().split('\n')
	[conn.sadd('proxy_set', ip) for ip in proxy_list if len(ip) > 2]
print("success!")