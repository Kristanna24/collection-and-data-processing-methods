# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from pymongo import MongoClient

class CastoramaPPipeline:
    def __init__(self):
        client = MongoClient('mongodb://localhost:27017')
        self.mongo_db = client.parse_castorama

    def process_item(self, item, spider):
        collection = self.mongo_db[spider.name]
        collection.insert_one(item)
        return item


class PhotosPipeline(ImagesPipeline):

    @staticmethod
    def add_url(link):
        return 'https://www.castorama.ru' + link

    def get_media_requests(self, item, info):
        if item['photo']:
            if isinstance(item['photo'], str):
                try:
                    yield Request(PhotosPipeline.add_url(item['photo']))
                except Exception as e:
                    print(e)
            elif isinstance(item['photo'], list):
                for img in (item['photo']):
                    try:
                        yield Request(PhotosPipeline.add_url(img))
                    except Exception as e:
                        print(e)



