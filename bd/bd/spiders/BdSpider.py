import scrapy
from bd.items import BdItem
import json
from urllib.parse import unquote
import requests

keyword = ['江泽民','习近平']

class BdSpider(scrapy.Spider):
    name = 'bd'
    allowed_domains = ["www.baidu.com", 'www.image.baidu.com']
    # start_urls = ['https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%s&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%s&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=%d' % (keyword, keyword, i) for i in range(0, 10, 1)]
    #
    # def parse(self, response):
    #     imgs = json.loads(response.body)['data']
    #     for img in imgs:
    #         item = BdItem()
    #         try:
    #             item['IMG_URL'] = [img['middleURL']]
    #             yield item
    #         except Exception as e:
    #             print('error')
    start_urls = []
    for key in keyword:
        for i in range(0, 10, 1):
            start_urls.append('https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%s&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%s&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=%d' % (
                key, key, i))
    def parse(self, response):
        imgs = json.loads(response.body)['data']
        queryenc = json.loads(response.body)['queryEnc']
        for img in imgs:
            item = BdItem()
            try:
                item['IMG_URL'] = img['middleURL']
                item['key'] = unquote(queryenc)
                yield item
            except Exception as e:
                print('error')