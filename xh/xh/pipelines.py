# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import urllib.request
class XhPipeline(object):
    def process_item(self, item, spider):
        item1 = dict(item)
        str1 = json.dumps(item1,ensure_ascii=False)
        with open('xh.json','a',encoding='utf-8')as pf:
            pf.write(str1)
        return item
class ImgPipeline(object):
    def process_item(self,item,spider):
        src = item['img']
        suffix = src.split('.')[-1]
        name = item['name']
        file_name = name + '.'+ suffix
        urllib.request.urlretrieve(url = src, filename='../xiaohua/' + file_name)
        return item