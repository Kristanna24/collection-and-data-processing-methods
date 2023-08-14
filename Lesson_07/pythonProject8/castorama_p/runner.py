from scrapy.crawler import CrawlerProcess
from scrapy.utils.reactor import install_reactor  # для автоматизации
from scrapy.utils.log import configure_logging # импорт системы логирования
from scrapy.utils.project import get_project_settings # подтягивает настройки
# импортируем проект.spiders:
from castorama_p.spiders.castoramaru import CastoramaruSpider

if __name__ == '__main__':
    install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')
    configure_logging()
    process = CrawlerProcess(get_project_settings())
    # category = input()
    process.crawl(CastoramaruSpider, section='плитка', category='керамогранит')
    process.start()

# from twisted.internet import reactor
# from scrapy.crawler import CrawlerRunner
# from scrapy.utils.log import configure_logging
# from scrapy.utils.project import get_project_settings
# from spiders.casto_p import CastoPSpider
# from sys import argv
# #
# if __name__ == '__main__':
    """
    По умолчанию секция поиска - gardening-and-outdoor, параметр -  pochtovye-jaschiki
    Для поиска других товаров в командной строке укажите раздел товаров и через пробел категорию
    """
    # section = 'gardening-and-outdoor'
    # category = 'pochtovye-jaschiki'
    # if len(argv) != 1:
    #     section = argv[1]
    #     category = argv[2]
    # print(argv)
    # configure_logging()
    # settings = get_project_settings()
    # runner = CrawlerRunner(settings)
    # runner.crawl(CastoPSpider, section=section, category=category)
    # reactor.run()