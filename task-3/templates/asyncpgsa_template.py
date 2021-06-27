import asyncio

from asyncpgsa import pg
from sqlalchemy import MetaData, Table, Column, Integer, String, Date
from dotenv import dotenv_values

config_dotenv = dotenv_values("../.env")
metadata = MetaData()


users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("birth_date", Date, nullable=False),
)


def left_pad(text: str, min_length: int) -> str:
    if len(text) < min_length:
        text = " " * (min_length - len(text)) + text
    return text


async def main():
    await pg.init(
        host='127.0.0.1',
        port="5432",
        database='example',
        user=config_dotenv["pg_user"],
        password=config_dotenv["pg_pwd"],
        min_size=5,
        max_size=10
    )


    users_query = users_table.select()
    results = await pg.query(users_query)
    for index, row in enumerate(results):
        if index == 0:
            print(" | ".join([left_pad(name, 13) for name in row.keys()]))
        print(" | ".join([left_pad(str(value), 13) for value in row.values()]))

    james = await pg.fetchrow(users_query.where(users_table.c.name == "James"))
    print()
    print(james)


if __name__ == '__main__':
    asyncio.run(main())