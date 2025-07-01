from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class SeleniumScraper:
    _instance = None

    def __init__(self):
        self.chrome_options = Options()
        self.driver = webdriver.Chrome(options=self.chrome_options)

    # using singleton design pattern
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    # mixture of strategy and template method design patterns
    def scrape(self, url, callback: callable = None):
        # chrome_options.add_argument("--headless")
        try:
            self.driver.get(url)
            time.sleep(1)
            if callback:
                callback(self.driver)
            result = self.driver.page_source
            return BeautifulSoup(result, 'lxml')

        finally:
            self.driver.quit()

    def synthetic_click(self, element):
        # simulating more realistic click with synthetic click
        # for inherently not clickable element
        self.driver.execute_script("""
                      arguments[0].dispatchEvent(new MouseEvent('click', {
                        bubbles: true,
                        cancelable: true,
                        view: window
                      }));
                    """, element)
