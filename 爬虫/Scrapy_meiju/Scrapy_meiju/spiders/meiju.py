# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from 爬虫.Scrapy_meiju.Scrapy_meiju.items import MeijuItem
class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['https://www.meijutt.com/alltop_hit.html']

    def parse(self, response):
        html = etree.HTML(response.text)
        datas = html.xpath('//ul[@class="top-list fn-clear"]//li')
        for data in datas:
            name = data.xpath('./h5/a/@title')
            pingfen1 = data.xpath('./div[@class="lasted-time fn-right"]/strong/text()')
            pingfen2 = data.xpath('./div[@class="lasted-time fn-right"]/span/text()')

            pingfen = pingfen1[0]+pingfen2[0]
            item = MeijuItem()
            item['name'] = name
            item['pingfen'] = pingfen
            yield item