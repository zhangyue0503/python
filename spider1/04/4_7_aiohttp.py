import asyncio
import aiohttp

urls = [
    "https://www.umei.cc/d/file/20230106/a4aa8c4f151d481bd493ef36243418a6.jpg",
    "https://www.umei.cc/d/file/20230106/da393de020f5797da64ebffd977e6d43.jpg",
    "https://www.umei.cc/d/file/20230106/a627ce8b697f093c8e15fcd022891198.jpg"
]

async def aiodownload(url):
    name = url.rsplit("/", 1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open(name, mode="wb") as f:
                f.write(await resp.content.read())



async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(aiodownload(url)))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())