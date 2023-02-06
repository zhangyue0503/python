import scrapy


class XiaoSpider(scrapy.Spider):
    name = 'xiao'
    allowed_domains = ['4399.com']
    start_urls = ['https://www.4399.com/flash/']

    def parse(self, response):
        # print(response.text)
        # txt = response.xpath("//ul[@class='n-game cf']/li/a/b/text()").extract()
        # print(txt)
        li_list = response.xpath("//ul[@class='n-game cf']/li")
        for li in li_list:
            name = li.xpath("./a/b/text()").extract_first()
            category = li.xpath("./em/a/text()").extract_first()
            date = li.xpath("./em/text()").extract_first()

            dic = {
                "name": name,
                "category":category,
                "date":date
            }

            yield dic

