# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class QiluSpider(CrawlSpider):
    name = 'qilu'
    allowed_domains = ['qlu.edu.cn']
    start_urls = ['http://www.qlu.edu.cn/38/list.htm']
    #/38/list880.htm
    pagelink = LinkExtractor(allow=r'(/38/list\d*.htm)')
    #href="/2019/0417/c38a124357/page.htm"
    #/2019/0416/c38a124324/page.htm
    contentlink = LinkExtractor(allow=r'(.*/page.htm)')
    rules = [
        Rule(pagelink,follow=True),
        Rule(contentlink,follow=True,callback='parse_item')
    ]
    def parse_item(self, response):
        print(response.url)
