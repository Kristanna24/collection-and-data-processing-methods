# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, Compose

class AvitoparserItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field(input_processor=Compose(clean_name), output_processor=TakeFirst())
    price = scrapy.Field(output_processor=TakeFirst())
    photo = scrapy.Field()
    product_link = scrapy.Field()