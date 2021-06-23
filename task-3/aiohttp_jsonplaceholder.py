import aiohttp
import asyncio
from aiohttp import ClientSession

# Ссылки, откуда будут парситься данные
links = ['https://jsonplaceholder.typicode.com/posts',
         'https://jsonplaceholder.typicode.com/users',
         'https://jsonplaceholder.typicode.com/photos', ]


# составляем карутины
async def create_task(link):
    async with ClientSession() as session:
        async with session.get(link) as resp:
            result = await resp.json()


# ожидание завершения всех карутины (asyncio.wait)
# !! If any awaitable in aws is a coroutine, it is automatically scheduled as a Task
# - сопрограммы автоматически преобразуются в таски !!
async def main():
    done, pending = await asyncio.wait(
    [create_task(link) for link in links]
    )
    for d in done:
        print(d)

    # тут будет пусто, нет ожидаемых задач
    for p in pending:
        print(p)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


# различия asyncio.wait и asyncio.gather:
# https://stackoverflow.com/questions/42231161/asyncio-gather-vs-asyncio-wait