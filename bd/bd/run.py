from scrapy import cmdline
from bd.spiders import BdSpider
if __name__ =="__main__":
    BdSpider.keyword = '江泽民'
    cmdline.execute("scrapy crawl bd".split())