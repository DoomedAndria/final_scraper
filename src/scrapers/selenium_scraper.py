from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class SeleniumScraper:

    # mixture of strategy and template method design pattern
    @staticmethod
    def scrape(url, callback: callable = None):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(options=chrome_options)

        try:
            driver.get(url)
            time.sleep(2)
            if callback:
                callback(driver)
            result = driver.page_source
            return BeautifulSoup(result, 'lxml')

        finally:
            driver.quit()
