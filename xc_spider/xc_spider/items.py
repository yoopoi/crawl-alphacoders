# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XcSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    img_path = scrapy.Field()
    img_name = scrapy.Field()
    img_url  = scrapy.Field()