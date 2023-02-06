# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class XiaoshuoSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class XiaoshuoDownloaderMiddleware:


    def process_request(self, request, spider):

        cs = "GUID=af645c2c-8313-4e56-85e7-18d3026db787; Hm_lvt_9793f42b498361373512340937deb2a0=1674977725; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F08%252F28%252F22%252F99942228.jpg-88x88%253Fv%253D1674977850000%26id%3D99942228%26nickname%3Dzyblog%26e%3D1690529998%26s%3D090843ecf4d5290a; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2299942228%22%2C%22%24device_id%22%3A%22185fc73c669b85-03573f78622cea-16525635-2073600-185fc73c66a207%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22af645c2c-8313-4e56-85e7-18d3026db787%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1675386019".split(";")
        cookies = {}
        for c in cs:
            # print(c)
            a = c.split("=")
            cookies[a[0].strip()] = a[1].strip()

        # print(cookies)

        request.cookies = cookies


