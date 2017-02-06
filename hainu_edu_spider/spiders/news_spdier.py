# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import NewsItem, NewsItemLoader
from scrapy.loader.processors import Compose


class NewsSpider(CrawlSpider):
    name = 'news'
    allowed_domains = ['hainu.edu.cn']
    start_urls = ['http://www.hainu.edu.cn/stm/vnew/shtml_liebiao.asp@bbsid=2439.shtml']

    rules = (
        Rule(LinkExtractor(allow=r'@bbsid=\d+\.shtml'), follow=True, callback='parse_item'),
        Rule(LinkExtractor(allow=r'pa='), callback='parse_item', follow=True), 
    )

    def parse_item(self, response):
        for li in response.xpath('//div[contains(@class, "news_list")]//li'):
            l = NewsItemLoader(item=NewsItem(), response=response, xpath=li)
            l.add_xpath('title', 'a/text()')
            l.add_xpath('url', 'a/@href', Compose(response.urljoin))
            l.add_xpath('date', 'span/text()')

        
        


