import chardet
import scrapy
from loguru import logger

from my_spider.items import GushiciItem


class BaidutiebaSpider(scrapy.Spider):
    name = 'poetry'
    allowed_domains = ['gushici.net']
    start_urls = ['https://www.gushici.net/']

    def parse(self, response):

        item = GushiciItem()
        div_list = response.xpath("//div[@class='left']/div[@class='gushici']")
        for div in div_list:
            title = div.xpath(".//p[@class='tit']//b/text()").get()
            dynasty = div.xpath(".//p[@class='source']/a/text()").getall()[0]
            author = div.xpath(".//p[@class='source']/a/text()").getall()[1]
            content = div.xpath(".//div[@class='gushici-box-text']//a/text()").getall()
            print(title, dynasty, author, content)
            with open('gushi.txt', 'a', encoding='utf-8') as f:
                f.write(title + ':' + dynasty + author + str(content) + '\n')

        next_url = response.xpath("//a[@class='amore']/@href").get()
        print('next_url:', 'https://www.gushici.net/' + next_url)
        if next_url:
            yield scrapy.Request(url='https://www.gushici.net/' + next_url, callback=self.parse)

        # file_name = response.split('/')[-1]
        # with open(file_name + '.txt', 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s.' % file_name)
