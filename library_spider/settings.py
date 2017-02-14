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

BOT_NAME = 'library_spider'

SPIDER_MODULES = ['library_spider.spiders']
NEWSPIDER_MODULE = 'library_spider.spiders'

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
    'library_spider.pipelines.BookItemPipeline': 300,
    'library_spider.pipelines.MongoPipeline': 400
}
