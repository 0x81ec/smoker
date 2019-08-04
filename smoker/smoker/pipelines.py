# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import redis

class SmokerPipeline(object):
    # def __init__(self):
    #
    #     self.red = redis.Redis(host="127.0.0.1", port=6379, db=1)

    def process_item(self, item, spider):
        # self.red.lpush( item["name"], item["url"])
        return item

    def close_spider(self,item,spider):
        # self.red.close()