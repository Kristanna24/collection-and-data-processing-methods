# pip install scrapy

# https://github.com/scrapy-plugins/scrapy-splash?ysclid=lldmrf3k92988801580

# pip install scrapy-splash
# scrapy startproject avitoparser .
# scrapy genspider avito avito.ru

# вставляем в настройки из https://github.com/scrapy-plugins/scrapy-splash?ysclid=lldmrf3k92988801580:
#
# SPLASH_URL = 'http://192.168.59.103:8050'
# SPLASH_URL = 'http://localhost:8050'
#
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy_splash.SplashCookiesMiddleware': 723,
#     'scrapy_splash.SplashMiddleware': 725,
#     'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
# }
#
# SPIDER_MIDDLEWARES = {
#     'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
# }
#
# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
# HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

# все коды из файлов middle...

# в паука и функцию:
# from scrapy_splash import SplashRequest

# with open("cat1.html", 'wb') as f:
#     f.write(response.body)