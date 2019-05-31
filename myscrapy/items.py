# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrapyItem(scrapy.Item):
    _id = scrapy.Field()
    blog_title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    content_url = scrapy.Field()
    content_summary = scrapy.Field()
    content_figure_url = scrapy.Field()
    author_icon_url = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
