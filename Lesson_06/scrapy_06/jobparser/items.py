# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobparserItem(scrapy.Item):
    # define the fields for your item here like:

    name = scrapy.Field()  # наименование вакансии
    city = scrapy.Field()  # наименованигорода
    min_salary = scrapy.Field()  # минимальная зарплата
    max_salary = scrapy.Field()  # максимальная зарплата
    currency = scrapy.Field()  # валюта
    url = scrapy.Field()  # ссылка на вакансию
    _id = scrapy.Field()  # поле для уникального ID MongoDB




