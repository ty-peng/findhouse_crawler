# -*- coding: utf-8 -*-
from urllib import parse
import re

import requests
import scrapy
from scrapy import Request, Selector

from findhouse_crawler.enums.crawler_enum import Mode, SourceSiteType
from findhouse_crawler.items import HouseForRent
from findhouse_crawler.settings import CATEGORIES, TYPES, CITY, MODE, IS_TEST, TEST_URL
from findhouse_crawler.utils.parse_util import handle_58font


class House58Spider(scrapy.Spider):
    """ 58房产房源信息爬虫.

    ## 已支持
        * 个人房产出租出售

    ## 待支持
        * ……

    ## 链接分析
        https://{city_code}.58.com/{category}/{source_type}/pn{page}/

        * city_code:   如 yili: 伊犁
        * category:    房源类型，如 chuzu: 租房
        * source_type: 发布来源类型，如 0: 个人房源
        * page:        页数，如 1

        ps: 注意列表第一页前 5 项是广告
    """
    name = '58house'

    allowed_domains = ['58.com']
    start_urls = ('http://58.com/',)
    URL_TEMPLATE = 'https://{city_code}.58.com/{category}/{source_type}/pn{page}/'

    def start_requests(self):
        for category_enum in CATEGORIES:
            for source_type_enum in TYPES:
                start_page = 1
                start_url = self.URL_TEMPLATE.format(city_code=CITY, category=category_enum.value['url_str'],
                                                     source_type=source_type_enum.value, page=start_page)
                if IS_TEST:
                    start_url = TEST_URL
                if MODE is Mode.INCREMENTAL_MODE:
                    # 异步请求
                    request = Request(url=start_url, callback=self.parse, dont_filter=True)
                    request.meta['category'] = category_enum
                    request.meta['source_type'] = source_type_enum
                    yield request
                elif MODE is Mode.FULL_MODE:
                    response = requests.get(start_url)
                    selector = Selector(response)
                    # 解析最后一页页数
                    end_page = int(
                        selector.css('.house-list > li > .pager a span')[2].css('::text').extract_first())
                    for i in range(start_page, end_page):
                        url = self.URL_TEMPLATE.format(city_code=CITY, category=category_enum.value['url_str'],
                                                       source_type=source_type_enum.value, page=i)
                        request = Request(url=url, callback=self.parse, dont_filter=True)
                        request.meta['category'] = category_enum
                        request.meta['source_type'] = source_type_enum
                        yield request

    def parse(self, response):
        selector = Selector(response)
        base64_str = re.findall(r"charset=utf-8;base64,(.*?)'\)", response.text)[0]
        to_parse_list = selector.css('.house-list > li')[:-1]
        category = response.meta['category']
        source_type = response.meta['source_type']
        # self.parse_list(to_parse_list, category, source_type, base64_str)

        # def parse_list(cls, to_parse_list, category, source_type, base64_str):
        """ 解析房源信息列表. """
        for to_parse in to_parse_list:
            house_info = HouseForRent()
            house_info['source_site_type'] = SourceSiteType.HOUSE_58.value
            house_info['category'] = category.value['code']
            house_info['publish_source_type'] = source_type.value
            img_src = to_parse.css('div.img-list img::attr(src)').extract_first()
            if img_src:
                house_info['pictures'] = img_src
            else:
                house_info['pictures'] = to_parse.css('div.img-list img::attr(lazy_src)').extract_first()
            des_div = to_parse.css('div.des')
            # url 中包含了一些信息 target lego_ts shangquan shangquanId dataSource
            house_info['source_url'] = des_div.css('a::attr(href)').extract_first()
            logr = to_parse.css('li.house-cell::attr(logr)').extract_first()
            url_query = parse.parse_qs(parse.urlparse(house_info['source_url']).query)
            house_info['source_id'] = int(logr.split("_")[3])
            des_div_first = des_div.css('a::text').extract_first().strip()
            house_info['title'] = des_div_first
            house_info['title'] = handle_58font(base64_str, house_info['title'])
            house_info['rental_type'] = des_div_first.split('|')[0].strip()
            house_info['business_area_id'] = url_query['shangquanId'][0]
            infor_p = des_div.css('p.infor')
            if infor_p.css('a::attr(href)').__len__() > 1:
                house_info['community_url'] = infor_p.css('a::attr(href)')[1].extract()
                house_info['community_id'] = house_info['community_url'].split('/')[-3]
                house_info['community_title'] = infor_p.css('a::text')[1].extract()
            else:
                house_info['community_url'] = None
                house_info['community_id'] = None
                house_info['community_title'] = None
            house_info['business_area'] = infor_p.css('a::text')[0].extract() + ' ' + url_query['shangquan'][0]
            house_info['rent'] = to_parse.css('div.money').css('b.strongbox::text').extract_first()
            house_info['rent'] = handle_58font(base64_str, house_info['rent'])
            house_info['room_amount'] = des_div.css('p.room::text').extract_first().split(' ')[0]
            house_info['room_amount'] = handle_58font(base64_str, house_info['room_amount'])
            # 注意这里 split 的分隔符不是空格，是特殊字符
            house_info['size'] = des_div.css('p.room::text').extract_first().split(' ')[-1]
            house_info['size'] = handle_58font(base64_str, house_info['size'])
            print(house_info)
            house_info['update_at'] = to_parse.css('.house-cell::attr(sortid)').extract_first()
            # TODO(me) 异步查询详情更新
            house_info['rent_info'] = ''
            house_info['publish_source'] = None
            house_info['publish_source_contact'] = None
            house_info['floor_info'] = None
            house_info['orientation'] = None
            house_info['province_id'] = None
            house_info['city_id'] = None
            house_info['area_id'] = None
            house_info['address'] = None
            yield house_info
