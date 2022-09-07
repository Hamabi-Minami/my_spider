import scrapy


class BaidutiebaSpider(scrapy.Spider):
    name = 'baidutieba'
    allowed_domains = ['baidu.com']
    start_urls = ['http://tieba.baidu.com/hello']

    def parse(self, response):
        pass
