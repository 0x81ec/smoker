# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FuckSpider(CrawlSpider):
    name = 'fuck'
    allowed_domains = ['www.uupm4.net']
    start_urls = ['https://www.uump4.net/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print("ok")
