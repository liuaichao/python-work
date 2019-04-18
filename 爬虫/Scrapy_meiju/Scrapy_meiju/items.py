# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyMeijuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
#定义数据模型
class MeijuItem(scrapy.Item):
    name = scrapy.Field()#名称
    pingfen = scrapy.Field()#评分
