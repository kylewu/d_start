
import json
import scrapy


class MockSpider(scrapy.Spider):
    """
    https://jsonplaceholder.typicode.com/todos
    """
    name = "mock"
    allowed_domains = ["jsonplaceholder.typicode.com"]
    start_urls = ['https://jsonplaceholder.typicode.com/todos']

    def start_requests(self):
        # get args
        # keyword = getattr(self, 'keyword', None)
        yield scrapy.Request(self.start_urls[0])

    def parse(self, response):
        j = json.loads(response.body_as_unicode())
        # print(j[0])
        for t in j:
            yield scrapy.Request(f'https://jsonplaceholder.typicode.com/todos/{t["id"]}', self.parse_todo, meta={'todo': t})
    
    def parse_todo(self, response):
        todo = response.meta['todo']
        j = json.loads(response.body_as_unicode())
        print(j)
