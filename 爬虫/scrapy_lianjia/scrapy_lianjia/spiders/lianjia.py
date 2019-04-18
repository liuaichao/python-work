# -*- coding: utf-8 -*-
import scrapy
from 爬虫.scrapy_lianjia.scrapy_lianjia.items import ScrapylianjiaItem
from 爬虫.scrapy_lianjia.scrapy_lianjia.settings import DEFAULT_REQUEST_HEADERS as headers
class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['https://jn.lianjia.com']
    # start_urls = ['http://jn.lianjia.com/']
    def start_requests(self):
        start_urls = ['https://jn.lianjia.com/zufang/changqing/','https://jn.lianjia.com/zufang/changqing/pg2']
        for start_url in start_urls:
            yield scrapy.Request(url=start_url, callback=self.parse, dont_filter=True, headers=headers)
    def parse(self, response):

        names = response.xpath('//div[@class="content__list--item--main"]/p[1]/a/text()').extract()
        prices = response.xpath('//span[@class="content__list--item-price"]/em/text()').extract()
        urls = response.xpath('//div[@class="content__list--item--main"]/p[1]/a/@href').extract()
        for i in range(len(names)):
            name = names[i].strip().replace(' ','')
            price = prices[i].strip()
            url = 'https://jn.lianjia.com'+urls[i].strip()
            # print(url)
            yield scrapy.Request(url=url, callback=self.two_parse, dont_filter=True, headers=headers,
                                 meta={'name':name,'price':price,'url':url})

    def two_parse(self, response):
        search_name = response.xpath('//div[@class="content__aside__list--title oneline"]/span/@title').extract()
        if len(search_name) == 0:
            search_name.append('无')
        # print(search_name)
        item = ScrapylianjiaItem()
        item['name'] = response.meta['name']
        item['price'] = response.meta['price']
        item['url'] = response.meta['url']
        item['search_name'] = search_name
        yield item



