from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from quotes_selenium.spiders.quotes_spider import QuotesSeleniumSpider  # Import your spider class

def run_quotes_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl(QuotesSeleniumSpider)
    process.start()  # Blocks until finished

##just example !!!!!!!!!!!!!!!!!
