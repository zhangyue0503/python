import scrapy

from boss.request import SeleniumRequest


class ZhipinSpider(scrapy.Spider):
    name = 'zhipin'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/web/geek/job?query=&city=101250100&position=100103']

    def start_requests(self):
        yield SeleniumRequest(
            url=self.start_urls[0],
            callback=self.parse
        )

    def parse(self, response):
        # print(response.text)
        pass
