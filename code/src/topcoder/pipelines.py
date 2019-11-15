# -*- coding: utf-8 -*-

import json
import requests

from scrapy.utils.project import get_project_settings

class TopcoderPipeline(object):
    def __init__(self):
        settings = get_project_settings()
        self.target_url = settings.get('SITEMAP_API_URL')

    def process_item(self, item, spider):
        res = requests.post(
            f'{self.target_url}/leafs',
             data=json.dumps(dict(item)),
             headers={'Content-Type': 'application/json'},
             )
        return item
