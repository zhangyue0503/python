import scrapy


class MeinvSpider(scrapy.Spider):
    name = 'meinv'
    allowed_domains = ['tupianzj.com']
    start_urls = ['https://www.tupianzj.com/bizhi/DNmeinv/']

    def parse(self, response):
        li_list = response.xpath("//ul[@class='list_con_box_ul']/li")
        print(response.text)
        for li in li_list:
            href = li.xpath("./a/@href").extract_first()
            print(href)

