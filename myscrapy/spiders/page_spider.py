# -*- coding: utf-8 -*-
import scrapy
import time
from myscrapy.items import MyscrapyItem

class PageSpider(scrapy.Spider):
    name = 'page_spider'
    allowed_domains = ['www.jianshu.com']
    viewed=[]
    start_urls = ['https://www.jianshu.com/p/779c10b4ccbd?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation']
    base_url='https://www.jianshu.com'
    url=''
    viewed.append('p/779c10b4ccbd')
    page_order=0


    def parse(self, response):
        i=0
        for item in response.xpath("//div[@class='seo-recommended-notes']/div"):
            i=i+1
            myItem=MyscrapyItem()
            myItem['author'] = item.xpath("./a[@class='author']/span/text()").extract()[0]
            print("作者：" + myItem['author'])
            myItem['author_icon_url'] = item.xpath("./a[@class='author']/@href").extract()[0]
            myItem['blog_title'] = item.xpath("./a[@class='title']/text()").extract()[0]
            print("标题：" + myItem['blog_title'])
            myItem['content_summary'] = item.xpath("./p/text()").extract()[0]
            print("内容：" + myItem['content_summary'])
            myItem['content_url'] = item.xpath("./a[@class='title']/@href").extract()[0]
            print("url:" + self.base_url + myItem['content_url'])
            time.sleep(1)
            if myItem['content_url'] not in self.viewed:
                self.url = myItem['content_url']
                self.viewed.append(self.url)
                if(i==len(response.xpath("//div[@class='seo-recommended-notes']/div"))):
                    self.page_order=self.page_order+1
                    yield self.parse_more()


    def parse_more(self):
        new_url=self.base_url+self.viewed[self.page_order]
        return scrapy.Request(new_url,callback=self.parse)
