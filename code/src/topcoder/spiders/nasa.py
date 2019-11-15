import math
import json
import scrapy
from scrapy.exceptions import CloseSpider
from scrapy.utils.project import get_project_settings


from topcoder.items import NasaItem

# DONE
# duplication detect
# start with keyword list
# 

# TODO 
# dynamically extend keyword list
# POST /mulitple-leafs

class NasaSpider(scrapy.Spider):
    name = "nasa"

    def start_requests(self):
        # get args
        keyword = getattr(self, 'keyword', None)
        settings = get_project_settings()
        self.asset_url = settings.get('NASA_ASSET_BASE_URL')
        self.start_url = settings.get('AVAIL_API_URL')
        print('starting ' + self.start_url + '/search?q=' + keyword)
        yield scrapy.Request(self.start_url + '/search?q=' + keyword, meta={'keyword': keyword})

    def parse(self, response):
        j = json.loads(response.body_as_unicode())
        # print(f"total hits: {j['collection']['metadata']['total_hits']}")

        for item in j['collection']['items']:
            for data in item['data']:
                ni = NasaItem()
                # TODO
                # getting first data only
                try:
                    ni['nasaId'] = data['nasa_id']
                    ni['loc'] = self.asset_url + data['nasa_id']
                    ni['created'] = data['date_created']
                    ni['mediaType'] = data['media_type']
                    ni['keywords'] = data.get('keywords', [])
                    yield ni
                except KeyError:
                    print(data)

        # handle total hits
        
        total_hits = j['collection']['metadata']['total_hits']

        page = response.meta.get('page', 1)
        keyword = response.meta['keyword']

        if page + 1 <= math.ceil(1.0 * total_hits / 100):
            link = f"{self.start_url}/search?q={keyword}&page={page+1}"
            # print(link)
            yield scrapy.Request(link, self.parse, meta={'keyword': keyword, 'page': page + 1})