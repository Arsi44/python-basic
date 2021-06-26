import asyncio
import asyncpg

from dotenv import dotenv_values

config_dotenv = dotenv_values(".env")


async def run():
    conn = await asyncpg.connect(
        user=config_dotenv["pg_user"],
        password=config_dotenv["pg_pwd"],
        database='new_db',
        host='127.0.0.1',
        port="5432"
    )
    # values = await conn.fetch()
    await conn.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
