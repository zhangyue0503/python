import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['17k.com']
    start_urls = ['https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919']

    def parse(self, response):
        print(response.text)
