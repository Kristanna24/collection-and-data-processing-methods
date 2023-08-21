# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from scrapy_splash import SplashRequest
from pymongo import MongoClient


#
# class AvitoparserPipeline:
#     def process_item(self, item, spider):
#         print()
#         return item

class AvitoPhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for photo in item['photos']:
                try:
                    yield scrapy.Request(photo)
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):
        if results:
            item['photos'] = [itm[1] for itm in results if itm[0]]
        return item

    # @staticmethod
    # def add_url(link):
    #     return "https://avito.ru/" + link
    #
    # def get_media_requests(self, item, info):
    #     if item['photos']:
    #         if isinstance(item['photos'], str):
    #             try:
    #                 yield scrapy.Request(AvitoPhotosPipeline.add_url(item['photos']))
    #             except Exception as e:
    #                 print(e)
    #         elif isinstance(item['photos'], list):
    #             for img in (item['photos']):
    #                 try:
    #                     yield scrapy.Request(AvitoPhotosPipeline.add_url(img))
    #                 except Exception as e:
    #                     print(e)

class AvitoparserPipeline:

    def __init__(self):
        client = MongoClient('mongodb://localhost:27017')
        self.mongo_db = client.avitoparser

    def process_item(self, item, spider):
        collection = self.mongo_db[spider.name]
        collection.insert_one(item)
        return item