import requests

session = requests.session()

data = {
    "loginName":13142161653,
    "password":"a123456"
}

url = "https://passport.17k.com/ck/user/login"
session.post(url,data=data)
# print(resp.cookies)


url2 = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"

resp = session.get(url2)
print(resp.json())