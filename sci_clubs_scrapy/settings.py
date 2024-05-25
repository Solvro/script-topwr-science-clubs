BOT_NAME = "sci_clubs_scrapy"

SPIDER_MODULES = ["sci_clubs_scrapy.spiders"]
NEWSPIDER_MODULE = "sci_clubs_scrapy.spiders"

ROBOTSTXT_OBEY = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
