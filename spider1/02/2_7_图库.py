import requests
from bs4 import BeautifulSoup

domain = "https://www.umei.cc/"
url = "https://www.umei.cc/bizhitupian/weimeibizhi/"
resp = requests.get(url)
resp.encoding='utf-8'
# print(resp.text)

main_page = BeautifulSoup(resp.text, "html.parser")
resp.close()

adiv = main_page.find("div", attrs={
    "class":"listlbc_cont_l"
}).find_all("div", class_="item_b clearfix")

alist = []
for d in adiv:
    alist.append(d.find("a"))


for a in alist:
    u = domain + a.get('href').strip("/")
    child_page_resp = requests.get(u)
    child_page_resp.encoding='utf-8'
    child_page_text = child_page_resp.text

    child_page = BeautifulSoup(child_page_text, "html.parser")
    child_page_resp.close()

    img = child_page.find("div", class_="big-pic").find("img")
    src = img.get("src")
    # print(src)


    img_name = src.split("/")[-1]
    with open("img/"+img_name,mode="wb") as f:
        f.write(requests.get(src).content)
    print("over!!",img_name)

    # print(u)
# print(alist)

