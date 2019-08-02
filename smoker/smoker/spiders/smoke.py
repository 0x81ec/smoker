# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from smoker.items import SmokerItem
from scrapy_redis.spiders import RedisCrawlSpider
class SmokeSpider(RedisCrawlSpider):
    name = 'smoke'
    allowed_domains = ['www.uump4.net']
    redis_key = "uump:start_urls"


    rules = (
        Rule(LinkExtractor(allow=r'.*/index-[\d]*.htm'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'.*/thread-[\d]*.htm'), callback='parse_detail', follow=False),
    )

    def parse_item(self, response):
        print(response.text)
        base_url = "https://www.uump4.net/"
        title = response.xpath("//li/div/a[last()]/text()").getall()
        href  = response.xpath("//li/div/a/@href").getall()
        for h in href:
            url = base_url+h
            # print(url)
            scrapy.Request(url)
        # for t in title:
        #     # print(t)
    def parse_detail(self,response):

        base_url = "https://www.uump4.net/"

        name = response.xpath("//ol/li[last()]/a/text()").get()
        if not response.xpath("//ul[@class='attachlist']/li/a/@href"):
            pass
        else:

            url = response.xpath("//ul[@class='attachlist']/li/a/@href").get()

            down_url= base_url + url

            it = SmokerItem(name=name,url=down_url)

            return it

            print(name, url)
