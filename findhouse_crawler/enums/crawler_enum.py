# -*- coding: utf-8 -*-

from enum import Enum


class SourceSiteType(Enum):
    """ 房源来源网站类型. """

    HOUSE_58 = 1
    """ 58房产 """


class Category(Enum):
    """ 房源分类. """

    RENTAL = 1
    """ 出租房 """


class PublishSourceType(Enum):
    """ 发布来源类型. """

    PERSON = 0
    """ 个人房源 """
    MIDDLEMAN = 1
    """ 经纪人 """
