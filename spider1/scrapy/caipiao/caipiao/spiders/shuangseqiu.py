import scrapy
from caipiao.items import CaipiaoItem


class ShuangseqiuSpider(scrapy.Spider):
    name = 'shuangseqiu'
    allowed_domains = ['500.com']
    start_urls = ['https://datachart.500.com/ssq/']

    def parse(self, response, **kwargs):
        # print(response.text)
        trs = response.xpath("//tbody[@id='tdata']/tr")
        for tr in trs:
            if tr.xpath("./@class").extract_first() == 'tdbck':
                continue
            red_ball = tr.xpath("./td[@class='chartBall01']/text()").extract()
            # print(red_ball)
            blue_ball = tr.css(".chartBall02::text").extract_first()
            # print(blue_ball)
            qihao = tr.xpath("./td[1]/text()").extract_first().strip()
            # print(qihao)
            # dic = {
            #     "qihao":qihao,
            #     "red_ball":red_ball,
            #     "blue_ball":blue_ball
            # }
            # yield dic
            cai = CaipiaoItem()
            cai['qihao'] = qihao
            cai['red_ball'] = red_ball
            cai['blue_ball'] = blue_ball
            yield cai

