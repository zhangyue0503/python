import json

import requests
from Crypto.Cipher import AES
from base64 import b64encode

# https://music.163.com/weapi/comment/resource/comments/get?csrf_token=

# params P3hCkN2ModKmS3zWXqeFriZI7XsPrnmFeP80yAAkHKfZh79yF/koj64N24SuMR1ICIlGTJQeD1S5NmzM03WIi8WHEQZTxSoAnTgRnxFd++h02Veguh2YpiB65LfJcfrNtqw6WP1pBuL0ezFY/sSFYMCbkCAB0QcDwtHh8qUUKAOprzvFQFTeBVudXiZt5bEPeGswrsSJBiVU4jb8ZOpqmjLbSHUDxFjtxqNmoV3KrKc7SwrEB44sX6JPMIhVFFeKhe+gzWh1zB4wZnaUy3D9ywdCtdI6D1+iC4ZUMJV/E0U=
# encSecKey ca77d129f29f4bc1822acf7bdf32aabddf5498b28192ed5175990b98841f3a53dda6e0adb911c11648b597f45a27b5b45521d964e50f7b8bcb182028a17333f1755101e47907d7784d00e60596abb6189ab2c0d542a495d6d6f077a001ea3350efc1eaa7e8ac9e61ab17dacc0b4d79c92bb0654a9463b0fd0a1540f472efea5d

data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_484058025",
    "threadId": "R_SO_4_484058025"
}
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
e = "010001"
i = "vPWXYCJUyIPjHu7k"
def get_encSecKey():
    return "1e8b79a0338ee55472dd4b878e26f3152f090eb372811a5c27ec1dcc503bccf74cfb65eaa67cb122032011468e0fce7bf8e1edcd2a514042e7cfd9ace6ea71ebfbb6a337808e037020b88064658511a93fb435565f121798975fcd05a05f6bf262b7ec2886c4be2fb729ac172776331ae6eee8c4613717bf64924dbd481a8396"

def to_16(data):
    pad = 16-len(data)%16
    data += chr(pad)*pad
    return data

def get_params(data):
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second

def enc_params(data, key):
    aes = AES.new(key=key.encode('utf-8'), IV="0102030405060708".encode('utf-8'), mode=AES.MODE_CBC)
    data = to_16(data)
    bs = aes.encrypt(data.encode('utf-8'))
    return str(b64encode(bs), "utf-8")

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
resp  = requests.post(url, data={
    "params":get_params(json.dumps(data)),
    "encSecKey":get_encSecKey()
})
print(resp.text)
resp.close()

'''
function a(a) {
    var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
    for (d = 0; a > d; d += 1)
        e = Math.random() * b.length,
        e = Math.floor(e),
        c += b.charAt(e);
    return c
}
function b(a, b) {
    var c = CryptoJS.enc.Utf8.parse(b)
      , d = CryptoJS.enc.Utf8.parse("0102030405060708")
      , e = CryptoJS.enc.Utf8.parse(a)
      , f = CryptoJS.AES.encrypt(e, c, {
        iv: d,   0102030405060708
        mode: CryptoJS.mode.CBC
    });
    return f.toString()
}
function c(a, b, c) {
    var d, e;
    return setMaxDigits(131),
    d = new RSAKeyPair(b,"",c),
    e = encryptedString(d, a)
}
function d(d, e, f, g) {
    var h = {}
      , i = a(16);
    return h.encText = b(d, g),
    h.encText = b(h.encText, i),
    h.encSecKey = c(i, e, f),
    h
}
'''


# requests.get()
