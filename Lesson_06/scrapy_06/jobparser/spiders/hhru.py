import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem
# transilate


class HhruSpider(scrapy.Spider):
    name = "hhru"
    allowed_domains = ["hh.ru"]
    start_urls = ["https://volgograd.hh.ru/search/vacancy?text=Python&salary=&ored_clusters=true&area=24",
                  "https://volgograd.hh.ru/search/vacancy?text=Python&salary=&ored_clusters=true&area=1"]

    def parse(self, response: HtmlResponse, **kwargs):
        next_page = response.xpath("//a[@data-qa = 'pager-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath("//a[@class ='serp-item__title']/@href").getall()
        print()
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):
        general = response.xpath(
            '//script[@type="application/ld+json"]//text()').extract_first()
        name = response.xpath("//h1/text()").get()
        city = response.xpath("//p[@data-qa = 'vacancy-view-location']//text()").getall()
        salary = response.xpath("//div[@data-qa = 'vacancy-salary']/span//text()").getall()
        url = response.url
        yield JobparserItem(general=general, name=name, city=city, salary=salary, url=url)

