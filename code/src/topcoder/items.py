# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NasaItem(scrapy.Item):
    # define the fields for your item here like:
    nasaId = scrapy.Field()
    loc = scrapy.Field()
    created = scrapy.Field()
    mediaType = scrapy.Field()
    keywords = scrapy.Field()