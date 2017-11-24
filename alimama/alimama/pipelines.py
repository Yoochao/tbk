# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib

from sql.sqlpool import MysqlTBK
from decimal import *


class AlimamaPipeline(object):
    def process_item(self, item, spider):
        try:
            db = MysqlTBK()
            keys = item.keys()
            if 'prom_short_url' not in keys:
                return
            url = item['url']
            img = item['img']
            title = item['title']
            getcontext().prec = 6
            price = Decimal(item['price'].replace(',', ''))
            monthly_sales = item['monthly_sales']
            commission_rate = Decimal(item['commission_rate'])
            commission = Decimal(item['commission'].replace(',', ''))
            shop_prom_url = item['shop_prom_url']
            prom_short_url = item['prom_short_url']
            prom_long_url = item['prom_long_url']
            prom_taotoken_url = item['prom_taotoken_url']
            if 'coupon' in keys:
                coupon = item['coupon'].replace(',', '')
                prom_short_ull_c = item['prom_short_ull_c']
                prom_long_url_c = item['prom_long_url_c']
                prom_taotoken_url_c = item['prom_taotoken_url_c']
            else:
                coupon = 0
                prom_short_ull_c = ''
                prom_long_url_c = ''
                prom_taotoken_url_c = ''
            url_md5 = hashlib.md5(url).hexdigest()
            exist = db.select("select id from t_alimama where url_md5=%s", {url_md5})
            if exist:
                # 更新
                db.update(
                    'update t_alimama set img=%s,title=%s,coupon=%s,price=%s,monthly_sales=%s,'
                    'commission_rate=%s,commission=%s,shop_prom_url=%s,prom_short_url=%s,prom_short_ull_c=%s,'
                    'prom_long_url=%s,prom_long_url_c=%s,prom_taotoken_url=%s,prom_taotoken_url_c=%s where url_md5=%s',
                    (img, title, coupon, price, monthly_sales, commission_rate, commission, shop_prom_url,
                     prom_short_url,
                     prom_short_ull_c, prom_long_url, prom_long_url_c, prom_taotoken_url, prom_taotoken_url_c, url_md5))
            else:
                # 新增
                db.insert('insert into t_alimama(url,img,title,coupon,price,monthly_sales,commission_rate,commission,'
                          'shop_prom_url,prom_short_url,prom_short_ull_c,prom_long_url,prom_long_url_c,prom_taotoken_url,'
                          'prom_taotoken_url_c,url_md5) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                          (url, img, title, coupon, price, monthly_sales, commission_rate, commission, shop_prom_url,
                           prom_short_url,
                           prom_short_ull_c, prom_long_url, prom_long_url_c, prom_taotoken_url, prom_taotoken_url_c,
                           url_md5))
            db.commit()
            db.con_release()
            print "================"
        except Exception, e:
            print item
