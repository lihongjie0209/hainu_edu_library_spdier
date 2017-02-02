import scrapy
from scrapy.shell import inspect_response
from scrapy.loader.processors import TakeFirst, MapCompose
import json
from hainu_library.items import BookItem, BookItemLoader

class LibrarySpider(scrapy.Spider):

    name = 'lib_spider'

    def start_requests(self):
        urls =('http://210.37.32.7/opac/search?q=*%3A*&searchType=standard&isFacet=true&view=standard&rows=100&hasholding=1&searchWay0=marc&q0=&logical0=AND&page={}'.format(page) for page in range(1,2))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse) 


    def parse(self, response):
        bookmetas = response.xpath('//div[@class="bookmeta"]')
        for meta in bookmetas:
            l = BookItemLoader(item=BookItem(), selector=meta, response=response)
            l.add_xpath('bookrecno', '@bookrecno')
            l.add_xpath('title', './/span[@class="bookmetaTitle"]/a/text()')
            l.add_xpath('author', './/a[contains(@href, "author")]/text()')
            l.add_xpath('publisher', './/a[contains(@href, "publisher")]/text()')
            l.add_xpath('pub_date', './/a[contains(@href, "publisher")]/following-sibling::text()', re=r'出版日期: (.+)')
            # item = l.load_item()
            yield scrapy.Request(url='http://210.37.32.7/opac/api/holding/'+l.get_output_value('bookrecno'), callback=self.parse_json, meta={'loader':l})

    def parse_json(self, response):
        l = response.meta['loader']
        json_data = json.loads(response.text)
        l.add_value('holding_list', json_data["holdingList"])
        item = l.load_item()
        yield item


            
   

            
                        
        

