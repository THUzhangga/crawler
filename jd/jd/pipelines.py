# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
from jd.spiders.JdSpider import JdSpider

class JdPipeline(object):
    # def __init__(self):
    def process_item(self, item, spider):
        for i, link in enumerate(item['img']):
            img = requests.get('http:' + link)
            name = item['name']
            key_eng = item['key_eng'].strip()
            img_path = f'img/{key_eng.strip()}'
            if os.path.exists(img_path) == False:
                os.mkdir(img_path)
            file_num = len(os.listdir(img_path))
            with open(f'{img_path}/{key_eng}_{file_num}.jpg', 'wb') as file:
                file.write(img.content)
        return item
