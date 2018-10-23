from scrapy import cmdline
from jd.spiders.JdSpider import JdSpider
import pandas as pd

def creat_url(chn):
    return [f"https://search.jd.com/Search?keyword={chn}"+"&enc=utf-8&suggest=3.his.0.0&pvid=3c0df64a9a3544c0aea06d3f5c3a30a8"]


if __name__ =="__main__":
    trans = pd.read_excel('trans.xlsx')
    ENG = trans['eng'].values
    CHN = trans['chn'].values
    urls = [creat_url(chn) for chn in CHN]
    JdSpider.keyword = ENG
    JdSpider.keyword_chn = CHN
    JdSpider.start_urls = [urls]
    cmdline.execute("scrapy crawl jd".split())