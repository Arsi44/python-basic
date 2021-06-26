В этом задании изучаю asyncio.
Работаю с aiohttp, выгружаю данные с https://jsonplaceholder.typicode.com/
Также создаю шаблоны для SQL-запросов (SQL, SQLAlchemy, Gino)
Храню данные с помощью Redis, Postgres (через asyncpg).

*Заметки:
-----------
- asyncio -
-----------

asyncio.gather() - запускает все задачи одновременно, но предоставляет мало контроля над задачами
asyncio.shield() - защищает такс от отмены
asyncio.wait_for() - ждем таймаута на выполнение задачи или же вызываем исключение (комбинируется с функцией shield())
asyncio.wait() - возвращает значение в виде (done, pending), также есть условия выхода и таймаут.
Отличие от wait_for(): не вызывает исключений
Отличие от gather(): более гибкое управление тасками
asyncio.as_completed() - возвращает итератор корутин по завершению

Важный момент: мы создаем карутины, а не таски!!! - Почти во всех функциях есть данное пояснение:
"If any awaitable in aws is a coroutine, it is automatically scheduled as a Task"

to_thread() - для задач  IO-bound, но в некоторых пакетах (где это отдельно реализовано может использоваться для CPU-bound)
run_coroutine_threadsafe(coro, loop) - практически тоже самое, что и to_thread(), НО, указывается конкретный луп для обработки

asyncio.create_task() и loop.create_task() - это разные вещи

--------------
- SqlAlchemy -
--------------
Определение Метадаты:
https://docs.sqlalchemy.org/en/14/glossary.html#term-table-metadata
