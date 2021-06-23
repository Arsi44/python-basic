# https://docs.aiohttp.org/en/stable/client_quickstart.html
import aiohttp
import asyncio


# создаём асинхронного клиента
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://jsonplaceholder.typicode.com/users') as resp:
            print(resp.status)
            print(await resp.json())
            # print(await resp.text())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
