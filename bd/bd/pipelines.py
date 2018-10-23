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
        img_path = f'img/{key}'
        print(url, key)
        if os.path.exists(img_path) == False:
            os.mkdir(img_path)

        # 不知道为啥百度图片这里不能调用request保存图片，否则停不下来...
        with open(f'{img_path}/urls.txt', 'a') as file:
            file.write(item['IMG_URL'] + '\n')
        # img = requests.get(url)
        # num = 0
        # if os.path.exists(f'{img_path}/num.txt') == False:
        #     num_file = open(f'{img_path}/num.txt', 'w')
        #     num_file.close()
        # else:
        #     with open(f'{img_path}/num.txt', 'r') as num_file:
        #         for i in num_file:
        #             num = int(i.strip())
        # with open(f'{img_path}/{1}.jpg', 'wb') as file:
        #     file.write(img.content)
            # num += 1
            # with open(f'{img_path}/num.txt', 'w') as num_file:
            #     num_file.write(str(num))
        return item

