import scrapy
from scrapy.linkextractors import LinkExtractor


class ErshoucheSpider(scrapy.Spider):
    name = 'ershouche'
    allowed_domains = ['che168.com', "autohome.com.cn"]
    start_urls = ['http://www.che168.com/changsha/list/#pvareaid=100945']

    def parse(self, response, **kwargs):
        # li_list = response.xpath("//ul[@class='viewlist_ul']/li")
        # # print(li_list)
        # for li in li_list:
        #     title = li.xpath("./a/div[2]/h4/text()").extract_first()
        #     href = li.xpath("./a/@href").extract_first()
        #     # print(title,href)
        #     yield scrapy.Request(
        #         url = response.urljoin(href),
        #         callback=self.parse_detail
        #     )
        print(response.text)
        le = LinkExtractor(restrict_xpaths=("//ul[@class='viewlist_ul']/li/a",))
        links = le.extract_links(response)
        # print(links)
        for link in links:
            print(link.url)
            yield scrapy.Request(
                url=link.url,
                callback=self.parse_detail
            )

        page_le = LinkExtractor(restrict_xpaths=("//div[@id='listpagination']/a",))
        page_links = page_le.extract_links(response)
        for page in page_links:
            # print(page.url)
            yield  scrapy.Request(
                url=page.url,
                callback=self.parse
            )

    def parse_detail(self, response, **kwargs):
        # print(1,response.url)
        pass

