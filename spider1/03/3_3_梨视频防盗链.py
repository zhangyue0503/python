import requests

url = "https://pearvideo.com/video_1720267"
contId = url.split("_")[1]

videoStatus = f"https://pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.07124238756195611"

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Referer": "https://pearvideo.com/video_1720267"
}
resp = requests.get(videoStatus,headers=headers)
srcUrl = resp.json()['videoInfo']['videos']['srcUrl']
systemTime = resp.json()['systemTime']

srcUrl = srcUrl.replace(systemTime,f"cont-{contId}")
print(srcUrl)

with open("a.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)

