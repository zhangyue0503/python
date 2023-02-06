import scrapy


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/typerank?type_name=剧情&type=11&interval_id=100:90&action=']

    def parse(self, response):
        print(response.text)
