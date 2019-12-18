# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import redis

class ZibScrapyPipeline(object):
    def __init__(self):
        self.pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, decode_responses=True)
        self.conn = redis.Redis(connection_pool=self.pool)

    def process_item(self, item, spider):
        if spider == "tmall_spider":
            name = 'tmall_' + str(item['index'])
            del item['index']
            for key,value in item.keys(),item.values():
                self.conn.hset(name, key, value)
        return item
