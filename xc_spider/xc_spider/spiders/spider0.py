import scrapy
from xc_spider.items import XcSpiderItem
import os 
from bs4 import BeautifulSoup
class spider0(scrapy.Spider):
    name = "spider0"
    allowed_domains = ["wall.alphacoders.com"]
    start_urls = ['https://wall.alphacoders.com/by_resolution.php?w=3840&h=2160&lang=Chinese&tdsourcetag=s_pctim_aiomsg']
    max_path = 100
    cur_path = 1
    def parse(self,response):
        for _ in range(500):
            parse1_path = "https://wall.alphacoders.com/by_resolution.php?w=3840&h=2160&lang=Chinese&page="+str(spider0.cur_path)
            spider0.cur_path +=1
            if spider0.cur_path>spider0.max_path:
                return 
            else:
                yield scrapy.Request(url = parse1_path, callback = self.parse1) 
        
    def parse1(self,response):
        html = response.text 
        soup = BeautifulSoup(html,'lxml')
        #print(soup)
        thumbs = soup.find_all("div",class_="thumb-container-big")
        for thumb in thumbs:
            item = XcSpiderItem()
            parse2_path = "https://wall.alphacoders.com/" + thumb.find("div",class_="boxgrid").find("a").get('href')
            #print(parse2_path)
            img_name = thumb.find("div",class_="boxgrid").find("a").get('title')
            item["img_name"] = img_name
            #print(img_name)
            yield scrapy.Request(url = parse2_path,meta = {'item':item}, callback = self.parse2) 
    def parse2(self,response):
        item = response.meta['item']
        html = response.text 
        soup = BeautifulSoup(html,'lxml')
        img_url = soup.find("div",class_="img-container-desktop").find("a").get("href")
        #print(img_path)
        item["img_url"] = img_url
        yield item