# -*- coding: utf-8 -*-
import scrapy
from xh.items import XhItem
'''
img = "//div[@class='item masonry_brick']//div/a/img/@src"
name = //div[@class='item masonry_brick']//div/a/img/@alt
'''
class XhwSpider(scrapy.Spider):
    name = 'xhw'
    allowed_domains = ['www.xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/list-1-0.html/']
    page = 0
    url = 'http://www.xiaohuar.com/list-1-'

    def parse(self, response):
        div_list = response.xpath("//div[@class='item masonry_brick']/div/div[@class='img']")
        # name = response.xpath("//div[@class='item masonry_brick']//div/a/img/@alt")
        for div in div_list:

            img = div.xpath('./a/img/@src').extract_first()
            if img.startswith('/d/'):
                img = 'http://www.xiaohuar.com'+ img
            name = div.xpath('./span/text()').extract_first()
            school = div.xpath('./div/a/text()').extract_first()
            item = XhItem(img = img, name = name,school = school)
            yield item
        self.page += 1
        if self.page <= 5:
            url = self.url + str(self.page) + '.html'
            yield scrapy.Request(url=url, callback=self.parse)
        else:
            print('爬到头了')






