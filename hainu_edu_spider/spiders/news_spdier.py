# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import NewsItem, NewsItemLoader
from scrapy.loader.processors import MapCompose
from urllib.parse import urljoin


class NewsSpider(CrawlSpider):
    name = 'news'
    allowed_domains = ['hainu.edu.cn']
    start_urls = ['http://www.hainu.edu.cn/stm/vnew/shtml_liebiao.asp@bbsid=2439.shtml']

    rules = (
        Rule(LinkExtractor(allow=r'#', restrict_xpaths=['//div[@class="liebiao2"]']), callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths=['//a[text()=">>"]']), follow=True, callback='next_page'),
    )


    # def next_page(self, response):
    #     print(response.url)
    def parse_item(self, response):

        
        l = NewsItemLoader(item=NewsItem(), response=response)
        l.add_xpath('title', '//*[@class="biaoti"]/text()')
        l.add_value('url', response.url)
        l.add_xpath('source', '//*[@class="laiyuan"]/text()', re=r'\[ 来源：(.+)\]')
        l.add_xpath('date', '//*[@class="laiyuan"]/text()', re=r'\d.+')
        l.add_xpath('keywords', '//*[@name="keywords"]/@content')
        l.add_xpath('description', '//*[@name="description"]/@content')
        
        item = l.load_item()
        yield item
        print(item)

        
        


