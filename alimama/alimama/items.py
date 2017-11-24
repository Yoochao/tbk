# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AlimamaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    img = scrapy.Field()
    title = scrapy.Field()
    coupon = scrapy.Field()
    price = scrapy.Field()
    monthly_sales = scrapy.Field()
    commission_rate = scrapy.Field()
    commission = scrapy.Field()
    shop_prom_url = scrapy.Field()
    prom_short_url = scrapy.Field()
    prom_short_ull_c = scrapy.Field()
    prom_long_url = scrapy.Field()
    prom_long_url_c = scrapy.Field()
    prom_taotoken_url = scrapy.Field()
    prom_taotoken_url_c = scrapy.Field()
    pass
