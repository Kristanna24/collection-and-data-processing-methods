import scrapy
from scrapy_splash import SplashRequest

from scrapy.http import HtmlResponse
from avitoparser.items import AvitoparserItem
from scrapy.loader import ItemLoader

class AvitoSpider(scrapy.Spider):
    name = "avito"
    allowed_domains = ["avito.ru"]
    start_urls = ["https://www.avito.ru/volgograd?q=%D0%BA%D0%BE%D1%82%D1%8F%D1%82%D0%B0"]


    def start_requests(self):
        if not self.start_urls and hasattr(self, "start_url"):
            raise AttributeError(
                "Crawling could not start: 'start_urls' not found "
                "or empty (but found 'start_url' attribute instead, "
                "did you miss an 's'?)"
            )
        for url in self.start_urls:
            yield SplashRequest(url)

    def parse(self, response:HtmlResponse):
        links = response.xpath("//a[@data-marker='item-title']/@href").getall()
        for link in links:
            yield SplashRequest("https://avito.ru/" + link, callback=self.parse_ads)

    def parse_ads(self, response:HtmlResponse):
        pass
        loader = ItemLoader(item=AvitoparserItem(), response=response)
        loader.add_xpath('name', "//h3/text()")
        loader.add_xpath('photos', )
        loader.add_xpath('price', )
        loader.add_value('product_link', response.url)
        yield loader.load_item()
        name = response.xpath("//h3/text()").get()
        photos =response.xpath("//ul[@class='images-preview-previewImageWrapper-']/li/img/@src").getall()
        price = response.xpath("//span/span[@data-marker='item-view/item-price']/text()").get()