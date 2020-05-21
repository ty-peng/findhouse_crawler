# -*- coding: utf-8 -*-
import pymongo
from findhouse_crawler.settings import MONGO_HOST, MONGO_PORT, MONGO_DB_NAME, MONGO_DB_COLLECTION


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FindhouseCrawlerPipeline(object):
    def __init__(self):
        host = MONGO_HOST
        port = MONGO_PORT
        db_name = MONGO_DB_NAME
        table_name = MONGO_DB_COLLECTION
        client = pymongo.MongoClient(host=host, port=port)
        db = client[db_name]
        self.post = db[table_name]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
