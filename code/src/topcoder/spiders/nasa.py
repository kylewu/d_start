
import json
import scrapy
from scrapy.exceptions import CloseSpider
from scrapy.utils.project import get_project_settings


from topcoder.items import NasaItem

# TODO hardcode for now
URL = 'https://images-api.nasa.gov'

class NasaSpider(scrapy.Spider):
    """
    """
    name = "nasa"

    def start_requests(self):
        # get args
        keyword = getattr(self, 'keyword', None)
        settings = get_project_settings()
        self.asset_url = settings.get('NASA_ASSET_BASE_URL')
        self.start_url = settings.get('AVAIL_API_URL')
        yield scrapy.Request(self.start_url + '/search?q=' + keyword)

    def parse(self, response):
        j = json.loads(response.body_as_unicode())
        print(f"total hits: {j['collection']['metadata']['total_hits']}")
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
        # next page
        for link in j['collection']['links']:
            if link['prompt'] == 'Next':
                yield scrapy.Request(link['href'], self.parse)

        # raise CloseSpider(f'{t["id"]} > 100')

    
    def parse_todo(self, response):
        todo = response.meta['todo']
        j = json.loads(response.body_as_unicode())
        print(j)
