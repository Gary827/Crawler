import time

from urllib import response
from taiwan_business.items import TaiwanBusinessItem
import scrapy
import lxml


class BusinessSpider(scrapy.Spider):
    name = 'business'
    allowed_domains = ['twincn.com']

    # overwrite start_requests method
    def start_requests(self):
        for i in range(301,365):
            time.sleep(1)
            url = "http://rank.twincn.com/default.aspx?q=&page={}".format(i)
            headers = {'User-Agent' :'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
                       'scheme':'https',
                       'referer':'https://rank.twincn.com/'}
            yield scrapy.Request(url, method="GET",  headers= headers, callback=self.parse)
            
    def parse(self, response):
        item = TaiwanBusinessItem()
        try:
            trs_list = response.xpath('//div[@class="table-responsive"]/table/tbody/tr')
            for i in range(0,len(trs_list)):
                item['id'] = trs_list[i].xpath('.//td/text()').get()
                item['name'] = trs_list[i].xpath('.//td/a[contains(@href,"https")]/text()').get()
                item['capital'] = trs_list[i].xpath('.//td[3]/text()').get()
                yield item    
        except Exception as e:
            print("Error",e)
            