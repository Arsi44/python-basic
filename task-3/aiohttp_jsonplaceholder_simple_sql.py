import aiohttp
import asyncio
import asyncpg
from aiohttp import ClientSession
import inspect

from dotenv import dotenv_values

config_dotenv = dotenv_values(".env")

# Ссылки, откуда будут парситься данные - последовательность важна
links = ['https://jsonplaceholder.typicode.com/users',
         'https://jsonplaceholder.typicode.com/posts',
         'https://jsonplaceholder.typicode.com/comments', ]


# составляем карутины и ВОЗВРАЩАЕМ значения
async def create_task(link):
    async with ClientSession() as session:
        async with session.get(link) as resp:
            return await resp.json()


# ожидание завершения всех карутин (asyncio.wait)
async def main():
    conn = await asyncpg.connect(user=config_dotenv["pg_user"], password=config_dotenv["pg_pwd"],
                                 database='example', host='127.0.0.1', port="5432")

    processed_coros = []
    done, pending = await asyncio.wait([create_task(link) for link in links])
    while len(processed_coros) != len(done) + len(pending):
        for d in done:
            res = d.result()
            # проверяем, что это пользователи
            is_user = res[0].get('username')
            # проверяем, что это пост
            is_post = res[0].get('postId')
            # проверяем, что это коммент - во всех остальных случаях
            print(is_user)
            print(is_post)
            # Нарушается очередность прихода ссылок, пожтому мы обрабатываем все исключениями
            if d not in processed_coros:
                if is_user:
                    try:
                        await conn.execute("INSERT INTO users(name, username, email) VALUES('{0}', '{1}', '{2}')"
                                           .format(res[0]['name'], res[0]['username'], res[0]['email'] + '1'))
                        await conn.execute("INSERT INTO users(name, username, email) VALUES('{0}', '{1}', '{2}')"
                                           .format(res[1]['name'], res[1]['username'], res[1]['email'] + '2'))
                        await conn.execute("INSERT INTO users(name, username, email) VALUES('{0}', '{1}', '{2}')"
                                           .format(res[2]['name'], res[2]['username'], res[2]['email'] + '3'))
                    except Exception as e:
                        print(e)
                elif is_post:
                    try:
                        await conn.execute("INSERT INTO posts(user_id, title) VALUES({0}, '{1}')"
                                           .format('1', res[0]['title']))
                    except Exception as e:
                        print(e)
                else:
                    try:
                        await conn.execute("INSERT INTO comments(post_id, text, sender_email) VALUES({0}, '{1}', '{2}')"
                                           .format('1', 'some_text', 'Sincere@april.biz'))
                    except Exception as e:
                        print(e)

                processed_coros.append(d)

    # # тут будет пусто, нет ожидаемых задач
    # for p in pending:
    #     print(p)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
