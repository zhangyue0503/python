from lxml import etree
import requests

url = "https://changsha.zbj.com/search/service/?l=0&kw=saas&r=2"
resp = requests.get(url)
# print(resp.text)

html = etree.HTML(resp.text)
divs = html.xpath("/html/body/div[1]/div/div/div[3]/div/div[4]/div[4]/div[1]/div")
# /html/body/div[2]/div/div/div[3]/div/div[4]/div[4]/div[1]/div[3]
print(divs)
for div in divs:
    price = div.xpath('./div//div[@class="price"]/span/text()')[0].strip('￥')
    title = "saas".join(div.xpath('./div//div[@class="name-pic-box"]/a/text()'))
    com_name = div.xpath('./div/a/div[2]/div[1]/div/text()')[0]
    print(price, title, com_name)


resp.close()


# etree.HTML()

