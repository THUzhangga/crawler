# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from bd.spiders.BdSpider import BdSpider
import requests

class BdPipeline(object):
    def process_item(self, item, spider):
        url = item['IMG_URL']
        key = item['key']
        key_eng = item['key_eng']
        img_path = f'img/{key_eng}'
        if os.path.exists(img_path) == False:
            os.makedirs(img_path)
        file_num = len(os.listdir(img_path))
        img = requests.get(url)
        with open(f'{img_path}/{key_eng}_{file_num}.jpg', 'wb') as file:
            file.write(img.content)
        return item