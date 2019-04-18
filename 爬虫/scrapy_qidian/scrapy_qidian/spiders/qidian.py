# -*- coding: utf-8 -*-
import scrapy
from 爬虫.scrapy_qidian.scrapy_qidian.items import scrapyQidianItem

class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['https://www.qidian.com']
    # start_urls = ['https://www.qidian.com/free']
    def start_requests(self):
        start_urls = ['https://www.qidian.com/free/all?orderId=&page=1&vip=hidden&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=1']
        for start_url in start_urls:
            yield scrapy.Request(url=start_url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        titles = response.xpath('//div[@class="book-mid-info"]/h4/a/text()').extract()
        infos = response.xpath('//div[@class="book-mid-info"]/h4/a/@href').extract()
        for i in range(len(titles)):
            title = titles[i]
            info = 'https:'+infos[i]
            print(title, info)
            yield scrapy.Request(url=info, callback=self.parse_next, dont_filter=True, meta={'title':title,'info':info})

    def parse_next(self, response):
        author = response.xpath('//div[@class="book-info "]/h1/span/a/text()').extract()[0]
        print(author)
        refer = response.xpath('//p[@class="intro"]/text()').extract()[0]

        item = scrapyQidianItem()
        item['title'] = response.meta['title']
        item['info'] = response.meta['info']
        item['author'] = author
        item['refer'] = refer
        yield item