# -*- coding: utf-8 -*-
import scrapy


class XiciProxySpider(scrapy.Spider):
    """西刺代理地址爬取.

    可用率不高，据说只有 10% 左右，且共用人数多。
    """

    name = 'xici_proxy'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://www.xicidaili.com/nn']

    def parse(self, response):
        pass
