# -*- coding: utf-8 -*-
from unittest import TestCase

from findhouse_crawler.enums.crawler_enum import SourceSiteType, Category
from findhouse_crawler.items import HouseForRent
from findhouse_crawler.pipelines import FindhouseCrawlerPipeline


class TestFindhouseCrawlerPipeline(TestCase):
    def test_process_item(self):

        test = HouseForRent()
        test['source_site_type'] = SourceSiteType.HOUSE_58.value
        test['category'] = Category.RENTAL.value
        test['source_id'] = 123
        test['title'] = '测试修改123'
        test['source_url'] = ''
        pipeline = FindhouseCrawlerPipeline()
        pipeline.process_item(test, None)
