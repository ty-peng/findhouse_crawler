# -*- coding: utf-8 -*-

from enum import Enum


class Mode(Enum):
    """ 数据抓取模式. """

    INCREMENTAL_MODE = 1
    """ 增量模式 """
    FULL_MODE = 2
    """ 全量模式 """


class SourceSiteType(Enum):
    """ 房源来源网站类型. """

    HOUSE_58 = 1
    """ 58房产 """


class Category(Enum):
    """ 房源分类. """

    RENTAL = {'url_str': 'chuzu', 'code': 1}
    """ 出租房 """


class PublishSourceType(Enum):
    """ 发布来源类型. """

    PERSON = 0
    """ 个人房源 """
    MIDDLEMAN = 1
    """ 经纪人 """
