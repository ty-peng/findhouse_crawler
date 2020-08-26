from unittest import TestCase

import requests
from scrapy import Selector

from findhouse_crawler.spiders.house_58 import House58Spider


class Test58HouseSpider(TestCase):
    def test_58house(self):
        response = requests.get('http://127.0.0.1:9090/58_list.html')
        selector = Selector(response)
        to_parse_list = selector.css('.house-list > li')[:-1]
        House58Spider.parse_list(to_parse_list)
