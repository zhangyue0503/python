import asyncio


async def func():
    print("你好呀")

if __name__ == '__main__':
    g = func()
    asyncio.run(g)

