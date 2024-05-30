from scrapy import signals
from scrapy.crawler import CrawlerProcess

from sci_clubs_scrapy.spiders.sci_clubs_spider import SciClubsSpider


class MySpiderRunner:
    def __init__(self, output: str):
        self.items = []
        self.process = CrawlerProcess(
            settings={
                "FEEDS": {
                    output: {"format": "jsonl"},
                },
            }
        )
        self.crawler = self.process.create_crawler(SciClubsSpider)
        self.crawler.signals.connect(self._parse_results, signal=signals.item_scraped)

    def _parse_results(self, item):
        self.items.append(item)
        return item

    def run_spider(self):
        self.process.crawl(self.crawler)
        self.process.start()
        return self.items
