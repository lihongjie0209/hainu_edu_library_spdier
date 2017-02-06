# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


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
            print(li.xpath('normalize-space()').extract_first())


