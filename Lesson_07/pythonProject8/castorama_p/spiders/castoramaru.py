import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
# импортируем проект.items:
from castorama_p.items import CastoramaPItem

URL = 'https://www.castorama.ru'

class CastoramaruSpider(scrapy.Spider):
    name = "castoramaru"
    allowed_domains = ["castorama.ru"]
    start_urls = ["https://www.castorama.ru/tile/granite/?PAGEN_3=2"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.page = 1
        self.start_urls = [f"https://www.castorama.ru/{kwargs.get('section')}/{kwargs.get('category')}/?PAGEN_3={self.page}"]

    def parse(self, response: HtmlResponse):
        product_links = response.xpath("//a[@class='product-card__img-link']/@href").getall()
        for link in product_links:
            yield response.follow(URL + link, callback=self.parse_page)

    def parse_page(self, response: HtmlResponse):
        loader = ItemLoader(item=CastoramaPItem(), response=response)
        loader.add_xpath('name', "//h1/text()")
        loader.add_xpath('photo', "//ul[@class='swiper-wrapper']/li[1]/span/@content")
        loader.add_xpath('price', "//span[@class='price']/span/span/text()")
        loader.add_value('product_link', response.url)
        yield loader.load_item()

