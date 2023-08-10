# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from itemadapter import ItemAdapter
from pymongo import MongoClient
import pymongo.errors
import json
from datetime import datetime

# здесь чистим данные, зп, имя и т.д.
class JobparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.vacancy0908

    def process_item(self, item, spider):

        vacancy_info = json.loads(item['general'])
        item['name'] = vacancy_info['title']
        item['city'] = vacancy_info['location']['addressLocality']
        item['url'] = vacancy_info['url']
        try:
            item['min_salary'], item['max_salary'], item[
                'currency'] = self.process_salary(vacancy_info['baseSalary'],
                                                  spider.name)
        except KeyError as er:
            item['min_salary'], item['max_salary'], item[
                'currency'] = None, None, None

        del item['general']
        collection = self.mongo_base[item.get('city')]
        collection.insert_one(item)
        return item

    def process_salary(self, salary, spider_name):
        currency = salary.get('currency')
        min_salary = salary['value'].get('minValue')
        max_salary = salary['value'].get('maxValue')
        if spider_name == 'hhru' and not min_salary:
            max_salary = salary['value'].get('value')
        return min_salary, max_salary, currency


