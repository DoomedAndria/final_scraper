from abc import ABC, abstractmethod
from typing import Dict
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from src.scrapers.base_scraper import BaseScraper
from src.scrapers.selenium_scraper import SeleniumScraper


# strategy design pattern
class CategoryStrategy(ABC):
    # can be extended with additional methods to support scraping different categories
    @abstractmethod
    def get_brand_links(self) -> None:
        pass


class ZoomerStrategy(CategoryStrategy, BaseScraper):
    def __init__(self):
        super().__init__('https://zoommer.ge/', 'Zoommer')
        self.ss = SeleniumScraper.get_instance()
        self.smartphones_page_url = BaseScraper.validate_url(self, '/mobiluri-telefonebi-c855')

    def get_brand_links(self):
        def click_see_more_button(driver: WebDriver):
            button = driver.find_element(By.CSS_SELECTOR, 'p.sc-bfc82784-1')
            self.ss.synthetic_click(button)

        soup = self.ss.scrape(self.smartphones_page_url, click_see_more_button)

        brand_container = soup.select_one('div.sc-b97309d4-5')
        if not brand_container:
            raise ValueError("Brand container not found")
        brands = [span.get_text(strip=True) for span in brand_container.find_all('span')
                  if span.get_text(strip=True)]
        links = {
            brand: f'{self.smartphones_page_url}/brand={brand.lower()};-c855'
            for brand in brands
        }
        print(links)
        return links


class AltaStrategy(CategoryStrategy, BaseScraper):
    def __init__(self):
        super().__init__('https://alta.ge/', 'Alta')
        self.ss = SeleniumScraper.get_instance()
        self.smartphones_page_url = (
            BaseScraper.validate_url(self, '/mobiluri-telefonebi-da-aqsesuarebi/mobiluri-telefonebi-c16s'))

    def get_brand_links(self):
        def click_brands_dropdown(driver: WebDriver):
            button = driver.find_element(By.CSS_SELECTOR, 'div.sc-d7590353-9 > :nth-child(2) p')
            self.ss.synthetic_click(button)

        soup = self.ss.scrape(self.smartphones_page_url, click_brands_dropdown)
        brand_container = soup.select_one('ul.sc-d7590353-11')
        brands = [b.get_text(strip=True) for b in brand_container.find_all('p')
                  if b.get_text(strip=True)]
        links = {
            brand: f'{self.smartphones_page_url.replace('-c16s', '')}/brendi={brand.lower()};-c16s'
            for brand in brands
        }
        print(links)
        return links
