# -*- coding: utf-8 -*-
import base64

import scrapy
from scrapy_splash import SplashRequest


class CouponSpider(scrapy.Spider):
    name = 'Coupon'
    super_search_url = 'http://pub.alimama.com/promo/search/index.htm?spm=a219t.7900221%2F1.1998910419.de727cf05.5084e76bAknneX&toPage=CURRENT_PAGE&queryType=2&perPageSize=50'
    start_urls = [
        'https://login.taobao.com/member/login.jhtml?style=mini&newMini2=true&css_style=alimama&from=alimama&redirectURL=http%3A%2F%2Fwww.alimama.com&full_redirect=true&disableQuickLogin=true']
    pro_script = """
               function main(splash)
                  splash:init_cookies(splash.args.cookies)
                  splash:autoload("http://code.jquery.com/jquery-1.12.4.min.js")
                  splash:autoload([[
                     var productInfo = []

                     function promote(index){
                        productInfo[index-1]={}
                        $("#J_search_results > div > div:nth-child("+index+") > div.box-btn-group > a.box-btn-left").click();
                     }

                     function config(){
                        $("#J_global_dialog > div > div.dialog-ft > button.btn.btn-brand.w100.mr10").click();
                     }
                     
                     function baseInfo(index){
                        productInfo[index-1].url = $("#J_search_results > div > div:nth-child("+index+") > div.pic-box > a").attr("href");
                        var img = $("#J_search_results > div > div:nth-child("+index+") > div.pic-box > a > img");
                        if(typeof(img.attr("data-src"))=="undefined"){
                            productInfo[index-1].img = 'http:' + img.attr("src");
                        }else{
                            productInfo[index-1].img = 'http:' + img.attr("data-src");
                        }
                        productInfo[index-1].title = $("#J_search_results > div > div:nth-child("+index+") > div.box-content > div:nth-child(1) > p > a").attr("title");
                        var coupon = $("#J_search_results > div > div:nth-child("+index+") > div.box-content > div.content-line.tags-container > span.tag.tag-coupon > span.money > span");
                        if(coupon.length > 0){
                           productInfo[index-1].coupon = coupon.html();
                        }
                        var price1 = $("#J_search_results > div > div:nth-child("+index+") > div.box-content > div.content-line.clearfix.mt5 > span.fl.number > span.integer").html();
                        var price2 = $("#J_search_results > div > div:nth-child("+index+") > div.box-content > div.content-line.clearfix.mt5 > span.fl.number > span.decimal").html();
                        productInfo[index-1].price = price1 + '.' + price2;
                        productInfo[index-1].monthly_sales = $("#J_search_results > div > div:nth-child("+index+") > div.box-content > div.content-line.clearfix.mt5 > span.fr > span.color-d > span").html();
                        rate1 = $("#J_search_results > div > div:nth-child("+index+") > div.box-content > div:last-child > span.fl.color-brand > span.number.number-16 > span.integer").html();
                        rate2 = $("#J_search_results > div > div:nth-child("+index+") > div.box-content > div:last-child > span.fl.color-brand > span.number.number-16 > span.decimal").html();
                        productInfo[index-1].commission_rate = rate1 + '.' + rate2;
                        commission1 = $("#J_search_results > div > div:nth-child("+index+") > div.box-content > div:last-child > span.fr > span.number.number-thin.number-16 > span.integer").html();
                        commission2 = $("#J_search_results > div > div:nth-child("+index+") > div.box-content > div:last-child > span.fr > span.number.number-thin.number-16 > span.decimal").html();
                        productInfo[index-1].commission = commission1 + '.' + commission2;
                        productInfo[index-1].shop_prom_url = 'http://pub.alimama.com' + $("#J_search_results > div > div:nth-child("+index+") > div.box-shop-info > div.shop-title > span > a").attr('href');
                     }

                     function shortUrl(index){
                        if($("#clipboard-target").length > 0){
                            productInfo[index-1].prom_short_url =  $("#clipboard-target").val();
                        }else{
                            productInfo[index-1].prom_short_url =  $("#clipboard-target-1").val();
                            productInfo[index-1].prom_short_ull_c =  $("#clipboard-target-2").val();
                        }
                        $("#magix_vf_code > div > div.dialog-hd > ul > li:nth-child(2)").click();
                     }

                     function longUrl(index){
                        if($("#clipboard-target").length > 0){
                            productInfo[index-1].prom_long_url =  $("#clipboard-target").val();
                        }else{
                            productInfo[index-1].prom_long_url =  $("#clipboard-target-1").val();
                            productInfo[index-1].prom_long_url_c =  $("#clipboard-target-2").val();
                        }
                        $("#magix_vf_code > div > div.dialog-hd > ul > li:nth-child(4)").click();
                     }

                     function taoToken(index){
                        if($("#clipboard-target").length > 0){
                            productInfo[index-1].prom_taotoken_url =  $("#clipboard-target").val();
                        }else{
                            productInfo[index-1].prom_taotoken_url =  $("#clipboard-target-1").val();
                            productInfo[index-1].prom_taotoken_url_c =  $("#clipboard-target-2").val();
                        }
                        $("#magix_vf_code > div > div.dialog-ft > button").click();
                     }

                     function getProductInfo(){
                        return productInfo;
                     }
                  ]])
                  assert(splash:go{
                    splash.args.url,
                    headers=splash.args.headers,
                    http_method=splash.args.http_method,
                    body=splash.args.body,
                  })
                  splash:wait(1)
                  for i=1,50 do
                     splash:evaljs("promote("..tostring(i)..")")
                     splash:wait(1)
                     splash:evaljs("config()")
                     splash:wait(1)
                     splash:evaljs("baseInfo("..tostring(i)..")")
                     splash:wait(1)
                     splash:evaljs("shortUrl("..tostring(i)..")")
                     splash:wait(1)
                     splash:evaljs("longUrl("..tostring(i)..")")
                     splash:wait(1)
                     splash:evaljs("taoToken("..tostring(i)..")")
                     splash:wait(1)
                  end
                  productInfo = splash:evaljs("getProductInfo()")
                  local entries = splash:history()
                  local last_response = entries[#entries].response
                  return {
                     url = splash:url(),
                     headers = last_response.headers,
                     http_status = last_response.status,
                     cookies = splash:get_cookies(),
                     html = splash:html(),
                     pic = splash:png(),
                     productInfo = productInfo
                  }
               end
            """

    def start_requests(self):
        login_script = """
           function main(splash)
              splash:init_cookies(splash.args.cookies)
              splash:autoload("http://code.jquery.com/jquery-1.12.4.min.js")
              splash:autoload([[
                  function quick2Static(){
                      $("#J_QRCodeLogin > div.login-links > a.forget-pwd.J_Quick2Static").click();
                  }
                  
                  function loginAlimama(){
                      $("#TPL_username_1").val('andrewdamai');
                      $("#TPL_password_1").val('y');
                      $("#TPL_password_1").val('ya');
                      $("#TPL_password_1").val('yao');
                      $("#TPL_password_1").val('yaoc');
                      $("#TPL_password_1").val('yaoch');
                      $("#TPL_password_1").val('yaocha');
                      $("#TPL_password_1").val('yaochao');
                      $("#TPL_password_1").val('yaochao9');
                      $("#TPL_password_1").val('yaochao91');
                      $("#TPL_password_1").val('yaochao910');
                      $("#TPL_password_1").val('yaochao9103');
                      $("#TPL_password_1").val('yaochao910329');
                      $("#J_SubmitStatic").click();
                  }
              ]])
              assert(splash:go{
                 splash.args.url,
                 headers=splash.args.headers,
                 http_method=splash.args.http_method,
                 body=splash.args.body,
              })
              splash:wait(1)
              splash:evaljs("quick2Static()")
              splash:wait(2)
              splash:evaljs("loginAlimama()")
              splash:wait(2)
              local entries = splash:history()
              local last_response = entries[#entries].response
              return {
                url = splash:url(),
                headers = last_response.headers,
                http_status = last_response.status,
                cookies = splash:get_cookies(),
                html = splash:html(),
                pic = splash:png()
              }
           end
        """

        for url in self.start_urls:
            yield SplashRequest(url, callback=self.parse_login, endpoint='execute', args={'lua_source': login_script})

    def parse_login(self, response):
        png_bytes = base64.b64decode(response.data['pic'])
        file = open('E:\\1.png', "wb")
        file.write(png_bytes)
        file.close()
        url = self.super_search_url.replace('CURRENT_PAGE', str(1))
        yield SplashRequest(url, callback=self.parse, endpoint='execute',
                            args={'lua_source': self.pro_script, 'timeout': 500})

    def parse(self, response):
        productInfo = response.data['productInfo']
        for i in range(len(productInfo)):
            yield productInfo[i]
        rate = response.xpath(
            '//*[@id="J_sort_filter"]/div/div[1]/div/span[4]/span/div/div/ul/li[2]/span/text()').extract()
        currentPage = response.xpath(
            '//div[@id="J_item_list"]/div[2]/div/div[1]/a[@class="btn btn-xlarge btn-current"]/text()').extract()
        if len(rate) > 0 and len(currentPage) > 0:
            count = int(rate[0].split('/')[1])
            currentPage = int(currentPage[0])
            if currentPage < count:
                url = self.super_search_url.replace('CURRENT_PAGE', str(currentPage + 1))
                yield SplashRequest(url, callback=self.parse, endpoint='execute',
                                    args={'lua_source': self.pro_script, 'timeout': 500})
