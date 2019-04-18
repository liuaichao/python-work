# -*- coding: utf-8 -*-
import scrapy
from 爬虫.Scrapy_xici.Scrapy_xici.items import XiciItem

class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/']



    def parse(self, response):
        data_1 = response.xpath('//tr[@class="odd"]')
        data_2 = response.xpath('//tr[@class=""]')
        datas = data_1+data_2
        item = XiciItem()
        for data in datas:
            try:
                country = data.xpath('./td[@class="country"]/img/@alt').extract()[0]
                if country == 'Cn':
                    country = '中国'
                else:
                    country = '外国'
            except:
                country = '未知'

            try:
                ip = data.xpath('./td[2]/text()').extract()[0]
            except:
                ip = '未知'
            try:
                port = data.xpath('./td[3]/text()').extract()[0]
            except:
                port = '未知'
            try:
                address = data.xpath('./td[4]/text()').extract()[0]
            except:
                address = '未知'
            try:
                isanonymous = data.xpath('./td[5]/text()').extract()[0]
            except:
                isanonymous = '未知'
            try:
                types = data.xpath('./td[6]/text()').extract()[0]
            except:
                types = '未知'
            try:
                livetime = data.xpath('./td[7]/text()').extract()[0]
            except:
                livetime = '未知'
            try:
                yanzhengtime = data.xpath('./td[8]/text()').extract()[0]
            except:
                yanzhengtime = '未知'

            # print(type(country), type(ip), type(port), type(address), type(isanonymous), type(types), type(livetime), type(yanzhengtime))

            item['country'] = country
            item['ip'] = ip
            item['port'] = port
            item['address'] = address
            item['isanonymous'] = isanonymous
            item['types'] = types
            item['livetime'] = livetime
            item['yanzhengtime'] = yanzhengtime
            yield item
