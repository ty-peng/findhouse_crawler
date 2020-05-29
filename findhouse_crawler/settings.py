# -*- coding: utf-8 -*-

from findhouse_crawler.enums.crawler_enum import Mode, Category, PublishSourceType

# Scrapy settings for findhouse_crawler project

BOT_NAME = 'findhouse_crawler'

SPIDER_MODULES = ['findhouse_crawler.spiders']
NEWSPIDER_MODULE = 'findhouse_crawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
# USER_AGENT = [
#     'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; LCTE; rv:11.0) like Gecko',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
#     'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 '
#     'Safari/537.36',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 '
#     'Safari/537.36 Edge/14.14393',
#     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
#     'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0',
#     'Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11',
#     'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1',
# ]

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Retry
RETRY_ENABLED = True
RETRY_TIMES = 20

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'findhouse_crawler.middlewares.FindhouseCrawlerSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#     'findhouse_crawler.middlewares.FindhouseCrawlerRandomUAMiddleware': 542,
#     'findhouse_crawler.middlewares.FindhouseCrawlerProxyMiddleware': 543,
#     'findhouse_crawler.middlewares.FindhouseCrawlerDownloadRetryMiddleware': 544,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'findhouse_crawler.pipelines.FindhouseCrawlerPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Mode
# See findhouse_crawler.enums.settings_enum.Mode
MODE = Mode.INCREMENTAL_MODE

# Prefix of city url
CITY = 'yili'

# Categories to be crawled
# See findhouse_crawler.enums.settings_enum.Category
CATEGORIES = [Category.RENTAL]

# Types to be crawled
# See findhouse_crawler.enums.settings_enum.Type
TYPES = [PublishSourceType.PERSON]

# Http proxy
PROXY_SERVER = ''
PROXY_USER = ''
PROXY_PASSWORD = ''

# MongoDB
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_USER = ''
MONGO_PASSWORD = ''
MONGO_DB_NAME = 'findhouse'
MONGO_DB_COLLECTION = 'house_58'

# Test
IS_TEST = True
TEST_URL = 'http://127.0.0.1:9090/58_list.html'
