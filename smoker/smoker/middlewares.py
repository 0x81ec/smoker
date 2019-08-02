# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from fake_useragent import UserAgent
import random

from  requests_html import HTMLSession
class SmokerSpiderMiddleware(object):
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

        # Should return either None or an iterable of Response, dict
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

# 获取代理ip列表
def get_proxyips():
    session = HTMLSession()
    r = session.get("http://www.89ip.cn/")
    trs = r.html.xpath("//tr")
    ips = []
    for t in trs:
        # print(t)
        d1 = t.xpath(".//td[1]/text()")
        d2 = t.xpath(".//td[2]/text()")
        ipt = "".join(d1).strip()+":"+"".join(d2).strip()
        ips.append(ipt)
    return ips
    # session = HTMLSession()
    # r = session.get("https://www.xicidaili.com/")
    # trs = r.html.xpath("//tr[@class='odd']")
    # ips = []
    # for t in trs:
    #     d1 = t.xpath(".//td[2]/text()")
    #     d2 = t.xpath(".//td[3]/text()")
    #     ipt = "".join(d1) + ":" + "".join(d2)
    #     ips.append(ipt)
    # return ips


class SmokerDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def __init__(self, *args, **kwargs):
        self.ips = get_proxyips()
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        usa = UserAgent()
        ip = random.choice(self.ips)
        print("proxy-ip: "+ip)
        request.meta['proxy'] = "http://"+ip
        request.headers.setdefault("User-Agent", usa.random)


    def process_response(self, request, response, spider):
        
        return response

    def process_exception(self, request, exception, spider):
        
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
