# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class ScrapyMeijuPipeline(object):
    def process_item(self, item, spider):
        return item
class Meijupipeline(object):
    def __init__(self):
        self.open = open('meiju.json','w',encoding='utf-8')
    def process_item(self, item, spider):
        #存储为json格式
        json.dump(dict(item), open('meiju.json', 'a', encoding='utf-8'),indent=4, ensure_ascii=False)
    def close_spider(self, spider):
        self.open.close()
