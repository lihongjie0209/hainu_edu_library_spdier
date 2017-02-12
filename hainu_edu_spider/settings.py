# -*- coding: utf-8 -*-

# Scrapy settings for hainu_library project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

from scrapy.settings.default_settings import *

BOT_NAME = 'hainu_edu_spider'

SPIDER_MODULES = ['hainu_edu_spider.spiders']
NEWSPIDER_MODULE = 'hainu_edu_spider.spiders'

# 测试时使用缓存以及高并发访问
# HTTPCACHE_ENABLED = True
# CONCURRENT_REQUESTS = 100
# CONCURRENT_REQUESTS_PER_DOMAIN = 100

# Mongodb Setting
Mongo_URI = 'mongodb://127.0.0.1:27017'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False


# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
#    'hainu_edu_spider.pipelines.BookItemPipeline': 300,
   'hainu_edu_spider.pipelines.MongoPipeline' : 400
}







