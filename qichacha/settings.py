# -*- coding: utf-8 -*-

# Scrapy settings for qichacha project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'qichacha'

SPIDER_MODULES = ['qichacha.spiders']
NEWSPIDER_MODULE = 'qichacha.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = True
FEED_EXPORT_ENCODING = 'gbk'
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    ':authority':'www.qichacha.com',
#    ':method':'GET',
#    ':path':'/firm_JS_7ad2b53deb4db8d7e1941d0dc8edd3da.shtml',
#    ':scheme':'https',
#    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#    'accept-encoding':'gzip, deflate, br',
#    'accept-language':'zh-CN,zh;q=0.8',
#    'cache-control':'max-age=0',
#    #'cookie:UM_distinctid=15d2a788dcc8e1-025c8d5bc8b836-8383667-100200-15d2a788dcdc11; _uab_collina=149965613035223206976143; gr_user_id=e60370f9-933f-46ce-82c5-d1ac176db196; hasShow=1; PHPSESSID=850lvp2rq40cds1hsn83nkton5; _umdata=0712F33290AB8A6D951430D1E0117EE1D14231F8130F1C2858BD826A13625AE2FD621DC5C2F9A92DCD43AD3E795C914C09063375D36107DCACBC946225EED311; acw_tc=AQAAAPuEvn89+wwAGAWCd7ZVD5bspHPf; gr_session_id_9c1eb7420511f8b2=d961fa41-6e3e-4632-a548-4256ca09c71a; CNZZDATA1254842228=415804783-1499653268-%7C1499772096
#    'upgrade-insecure-requests':'1',
#    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'qichacha.middlewares.QichachaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    #'qichacha.middlewares.QichachaSpiderMiddleware': 543,
    #'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware': 700
    'qichacha.middlewares.RotateUserAgentMiddleware':500
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'qichacha.pipelines.QichachaPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
