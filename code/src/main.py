# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


settings = get_project_settings()
process = CrawlerProcess(settings)

for keyword in settings['KEYWORDS']:
    process.crawl('nasa', keyword=keyword)

process.start()