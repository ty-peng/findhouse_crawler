# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FindhouseCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class HouseBase(scrapy.Item):
    """ 房源信息基类. """

    _id = scrapy.Field()
    """ 数据库 ID """
    key = scrapy.Field()
    """ 唯一 key(source_site_type, category, source_id) """
    source_site_type = scrapy.Field()
    """ 来源站点类型 (See findhouse_crawler.enums.crawler_enum.SourceSiteType) """
    source_id = scrapy.Field()
    """ 来源 ID """
    source_url = scrapy.Field()
    """ 源链接 """
    title = scrapy.Field()
    """ 标题 """
    category = scrapy.Field()
    """ 房源分类 (See findhouse_crawler.enums.crawler_enum.Category) """
    publish_source_type = scrapy.Field()
    """ 发布来源类型 (See findhouse_crawler.enums.crawler_enum.PublishSourceType) """
    publish_source = scrapy.Field()
    """ 发布来源信息（个人/中介名称） """
    publish_source_contact = scrapy.Field()
    """ 发布来源联系方式 """
    province_id = scrapy.Field()
    """ 省份 ID """
    city_id = scrapy.Field()
    """ 城市 ID """
    area_id = scrapy.Field()
    """ 区域 ID """
    business_area_id = scrapy.Field()
    """ 商圈 ID """
    community_id = scrapy.Field()
    """ 小区 ID """
    community_title = scrapy.Field()
    """ 小区标题 """
    community_url = scrapy.Field()
    """ 小区 URL """
    floor_info = scrapy.Field()
    """ 楼层信息 """
    orientation = scrapy.Field()
    """ 朝向 """
    room_amount = scrapy.Field()
    """ 房间数量信息 """
    size = scrapy.Field()
    """ 面积 """
    address = scrapy.Field()
    """ 详细地址 """
    pictures = scrapy.Field()
    """ 图片链接 """
    update_at = scrapy.Field()
    """ 页面上的更新时间 """


class HouseForRent(HouseBase):
    """ 房屋出租信息. """

    rental_type = scrapy.Field()
    """ 租赁方式 """
    rent = scrapy.Field()
    """ 租金 """
    rent_info = scrapy.Field()
    """ 租金其他信息 """
