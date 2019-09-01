# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import requests
import threading
import os
import time
from xc_spider.settings import PHOTO_ROOT
class XcSpiderPipeline(object):
    def convent_dirname(self,name):
        ban_char = ["?","/","\\",">","<","|","*",'"',"*"]
        for i in ban_char:
           name =  name.replace(i,"")
        return name +"#"+str(time.time())
    def download_thread(self,item):
        path_name = PHOTO_ROOT+XcSpiderPipeline.convent_dirname(self,item["img_name"])+".jpg"
        if os.path.exists(path_name):
            print(path_name+"已存在")
            return
        r = requests.get(item["img_url"], stream=True)
        if r.status_code == 200:
            if(not os.path.exists(PHOTO_ROOT)):
                os.mkdir(PHOTO_ROOT)
            open(path_name, 'wb').write(r.content) 
        del r
    def process_item(self, item, spider):
        #XcSpiderPipeline.download_thread(self,item)
        t1 = threading.Thread(target=XcSpiderPipeline.download_thread,args=(self,item,))
        t1.start()
        while True:
            if (len(threading.enumerate()) < 200):
                break
            time.sleep(0.3)
        
        return item
