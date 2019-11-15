# -*- coding: utf-8 -*-
import scrapy


class NasaItem(scrapy.Item):
    nasaId = scrapy.Field()
    loc = scrapy.Field()
    created = scrapy.Field()
    mediaType = scrapy.Field()
    keywords = scrapy.Field()