# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from topcoder.spiders.mock import MockSpider

settings = get_project_settings()
process = CrawlerProcess(settings)

for keyword in settings['KEYWORDS']:
    print(keyword)
    for spider in SPIDERS:
        process.crawl(spider, keyword=keyword)

process.start()

process.start()