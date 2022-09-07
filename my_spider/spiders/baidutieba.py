import scrapy


class BaidutiebaSpider(scrapy.Spider):
    name = 'baidutieba'
    allowed_domains = ['baidu.com']
    start_urls = ['http://tieba.baidu.com/hello']

    def parse(self, response):
        file_name = response.split('/')[-1]
        with open(file_name + '.txt', 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s.' % file_name)
