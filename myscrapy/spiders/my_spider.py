# -*- coding: utf-8 -*-
import scrapy
from abc import abstractmethod
from myscrapy.items import MyscrapyItem


class Myspider(scrapy.Spider):
    name = 'jianshuspider'
    base_url='www.jianshu.com'
    allowed_domains = ['www.jianshu.com']
    start_urls = []
    category_code=''
    common_url=''
    url=''

    @abstractmethod
    def parse_more(self):
        pass

    def get_full_url(self,url):
        return self.base_url+url

    def parse(self,response):
        # print("请求："+response.xpath("//ul[@class='note-list']/li").extract()[0])
        for i in response.xpath("//ul[@class='note-list']/li"):
            print("数量："+str(len(response.xpath("//ul[@class='note-list']/li").extract())))
            item = MyscrapyItem()
            try:
                item['_id']=i.xpath("./@id").extract()[0]
            except Exception as e:
                print(e)
                return
            try:
                # text()
                item['blog_title']=i.xpath(".//div[@class='content']/a/text()").extract()[0]
            except Exception as e:
                print(e)
                return
            try:
                item['content_url'] =self.get_full_url(i.xpath(".//div[@class='content']/a/@href").extract()[0])
            except Exception as e:
                    item['content_url'] = ''

            try:
                    item['content_summary'] =i.xpath(".//div[@class='content']/p/text()").extract()[0]

            except Exception as e:
                item['content_summary'] = ''
            try:
                item['content_figure_url'] =self.get_full_url(i.xpath("./a/img/@src").extract()[0])
            except Exception as e:
                item['content_figure_url'] = ''
            try:
                item['author'] =i.xpath(".//div[@class='author']/div/a/text()").extract()[0]
            except Exception as e:
                item['author'] = ''
            try:
                item['date'] = i.xpath(".//div[@class='author']/div/span/@data-shared - at").extract()[0]
            except Exception as e:
                item['date'] = ''
            try:
                item['author_icon_url'] =self.get_full_url(i.xpath(".//div[@class='author']/a/@href")
                              .extract()[0])
            except Exception as e:
                item['author_icon_url'] = ''
            yield item


class ITSpider(Myspider):
    name = 'ITSpider'
    page=0
    category_code = 'v2Cqjw'
    common_url = 'https://www.jianshu.com'
    url = common_url
    start_urls = [url]

    def parse_more(self):
        self.page +=1
        if self.page>20:
            return
        return scrapy.Request(self.common_url+str(self.page),
                              callback=self.parse)