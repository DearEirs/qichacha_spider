# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose
from w3lib.html import remove_tags


def get_data(value):
    '''
    获取value值 并去除str收尾的空格和换行符,返回值
    :param value: str
    :return: str
    '''
    b = value.replace('\n','').strip(' ')
    if not value:
        value = '-'
    return value

class QichachaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company = scrapy.Field()#公司名
    email = scrapy.Field()#邮箱
    web_site = scrapy.Field()#官网
    phone = scrapy.Field()#电话
    address = scrapy.Field()#地址
    credit_code = scrapy.Field()#统一社会信用代码
    taxpayer_code = scrapy.Field()#纳税人识别号
    registered_code = scrapy.Field()#注册号
    organization_code = scrapy.Field()#组织机构代码
    representative = scrapy.Field()#法定代表人
    registered_capital= scrapy.Field()#注册资本
    state = scrapy.Field()#经营状态
    create_date = scrapy.Field()#成立日期
    type = scrapy.Field()#公司类型
    scale = scrapy.Field()#人员规模
    limit_date = scrapy.Field()#营业期限
    registration_authority = scrapy.Field()#登记机关
    approved_date = scrapy.Field()#核准日期
    english_name = scrapy.Field()#英文名
    area = scrapy.Field()#所属地区
    industry = scrapy.Field()#所属行业
    used_name = scrapy.Field()#曾用名
    address = scrapy.Field()#企业地址
    business_scope = scrapy.Field()#经营范围
    main_staff = scrapy.Field()#主要人员


