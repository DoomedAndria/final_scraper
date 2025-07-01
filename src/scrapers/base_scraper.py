from urllib.parse import urlparse, urljoin

import requests
from bs4 import BeautifulSoup


class BaseScraper:
    def __init__(self, url, name):
        self._URL = url
        self._NAME = name


    @classmethod
    def fetch_and_parse_page(cls,url):
        try:
            html = requests.get(url).text
            try:
                soup = BeautifulSoup(html, 'lxml')
                return soup
            except Exception as e:
                print(f'error while parsing content, {e}')

        except requests.exceptions.RequestException:
            print(f'error while accessing page. url: {url}')
        except Exception as e:
            print(f'unexpected error. {e}')


    @staticmethod
    def validate_url(self, url):
        parsed_url = urlparse(url)
        if parsed_url.netloc:
            if self._URL.replace('https://', '').replace('http://', '').strip('/') in parsed_url.netloc:
                return url
        return urljoin(self._URL, url)