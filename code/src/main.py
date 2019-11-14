# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from topcoder.spiders.mock import MockSpider

settings = get_project_settings()
process = CrawlerProcess(settings)

process.crawl(MockSpider, keyword='test')

process.start()