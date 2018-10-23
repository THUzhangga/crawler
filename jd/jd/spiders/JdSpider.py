import scrapy
from jd.items import JdItem
import pandas as pd
trans = pd.read_excel('trans_3.xlsx')
ENG = trans['eng'].values
CHN = trans['chn'].values
class JdSpider(scrapy.Spider):
    name = "jd"
    allowed_domains = ["www.jd.com"]
    start_urls = ['http://www.jd.com/']
    search_url1 = 'https://search.jd.com/Search?keyword={key}&enc=utf-8&page={page}'
    search_url2 = 'https://search.jd.com/s_new.php?keyword={key}&enc=utf-8&page={page}&s=26&scrolling=y&pos=30&tpl=3_L&show_items={goods_items}'
    shop_url = 'http://mall.jd.com/index-{shop_id}.html'

    def start_requests(self):
        for key, key_eng in zip(CHN, ENG):
            for num in range(1, 3):
                page1 = str(2 * num)
                page2 = str(2 * num - 1)
                yield scrapy.Request(url=self.search_url1.format(key=key, page=page1), callback=self.parse,
                                     meta={'key': key, 'key_eng': key_eng}, dont_filter=True)
                yield scrapy.Request(url=self.search_url1.format(key=key, page=page1), callback=self.get_next_half,
                                     meta={'page2': page2, 'key': key, 'key_eng': key_eng}, dont_filter=True)
                # 这里一定要加dont_filter = True，不然scrapy会自动忽略掉这个重复URL的访问

    def get_next_half(self, response):
        try:
            items = response.xpath('//*[@id="J_goodsList"]/ul/li/@data-pid').extract()
            key = response.meta['key']
            key_eng = response.meta['key_eng']
            page2 = response.meta['page2']
            goods_items = ','.join(items)
            yield scrapy.Request(url=self.search_url2.format(key=key, page=page2, goods_items=goods_items),
                                 callback=self.next_parse,
                                 meta={'key': key, 'key_eng': key_eng},
                                 dont_filter=True)
        except Exception as e:
            print('没有数据')

    def parse(self, response):
        for sel in response.xpath('//ul[@class="gl-warp clearfix"]/li/div[@class="gl-i-wrap"]'):
            item = JdItem()
            item['name'] = sel.xpath('.//div[@class="p-name p-name-type-2"]//em/text()').extract()
            item['price'] = sel.xpath('.//div[@class="p-price"]/strong/i/text()').extract()
            item['img'] = sel.xpath('.//div[@class="p-img"]/a/img/@source-data-lazy-img').extract()
            item['key'] = response.meta['key']
            item['key_eng'] = response.meta['key_eng']
            yield item

    def next_parse(self, response):
        for sel in response.xpath('//ul[@class="gl-warp clearfix"]/li/div[@class="gl-i-wrap"]'):
            item = JdItem()
            item['name'] = sel.xpath('.//div[@class="p-name p-name-type-2"]//em/text()').extract()
            item['price'] = sel.xpath('.//div[@class="p-price"]/strong/i/text()').extract()
            item['img'] = sel.xpath('.//div[@class="p-img"]/a/img/@source-data-lazy-img').extract()
            item['key'] = response.meta['key']
            item['key_eng'] = response.meta['key_eng']
            yield item