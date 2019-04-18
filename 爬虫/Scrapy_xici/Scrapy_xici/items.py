# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyXiciItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class XiciItem(scrapy.Item):
    country = scrapy.Field()
    ip = scrapy.Field()
    port = scrapy.Field()
    address = scrapy.Field()
    isanonymous = scrapy.Field()
    types = scrapy.Field()
    livetime = scrapy.Field()
    yanzhengtime = scrapy.Field()