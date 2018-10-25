from scrapy import cmdline
from bd.spiders import BdSpider
if __name__ =="__main__":
    cmdline.execute("scrapy crawl bd".split())