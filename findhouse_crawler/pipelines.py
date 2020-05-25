# -*- coding: utf-8 -*-
import pymongo

from findhouse_crawler.settings import MONGO_HOST, MONGO_PORT, MONGO_DB_NAME, MONGO_DB_COLLECTION, MONGO_USER, \
    MONGO_PASSWORD


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FindhouseCrawlerPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(host=MONGO_HOST, port=MONGO_PORT, username=MONGO_USER, password=MONGO_PASSWORD)
        db = client[MONGO_DB_NAME]
        self.collection = db[MONGO_DB_COLLECTION]

    def process_item(self, item, spider):
        key = '{}_{}_{}'.format(item['source_site_type'], item['category'], item['source_id'])
        item['key'] = key
        self.collection.replace_one({"key": key}, item, True)
        return item
