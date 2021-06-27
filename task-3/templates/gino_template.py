#  https://python-gino.org/docs/en/1.0/tutorials/tutorial.html
import psycopg2.extras
import asyncio
from gino import Gino

db = Gino()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    nickname = db.Column(db.Unicode(), default='noname')

    def __str__(self):
        values = [f"{n}={getattr(self, n)}" for n in ("id", "nickname")]
        return f"{self.__class__.__name__}({', '.join(values)})"

    __repr__ = __str__


async def main():
    await db.set_bind('postgresql://postgres:Hrieleght2@localhost/gino')
    await db.gino.create_all()  # Обязательно, если таблицы не созданы

    # создать пользователя способ 1
    user_1 = await User.create(nickname='fantix')

    # создать пользователя способ 2 (заранее резервируем место в памяти и изменим его)
    user_2 = User(nickname='fantix2')
    user_2.nickname += ' (founder)'
    await user_2.create()

    # получить пользователя по первичному ключу
    received_user = await User.get(2)
    # print(received_user)

    # получить всех пользователей
    all_users_1 = await db.all(User.query)
    # или
    all_users_2 = await User.query.gino.all()
    # print(all_users_1 == all_users_2)  # False

    # найти по условию
    founding_users = await User.query.where(User.id < 10).gino.all()
    # print(founding_users)

    # Другие примеры выборки данных
    user = await User.query.where(User.nickname == 'fantix').gino.first()
    name = await User.select('nickname').where(User.id == 1).gino.scalar()
    population = await db.func.count(User.id).gino.scalar()

    # UPDATE Обновление данных (пример) - тут мы создаем нового пользователя и меняем его имя
    user = await User.create(nickname='fantix')
    name = await User.select('nickname').where(
        User.id == user.id).gino.scalar()
    assert name == user.nickname
    await user.update(nickname='daisy').apply()

    await User.update.values(nickname='Founding Member ' + User.nickname).where(
        User.id < 10).gino.status()

    # DELETE
    user = await User.create(nickname='fantix444')
    await user.delete()

    await User.delete.where(User.id > 5).gino.status()

    await db.pop_bind().close()
    # users = await db.all(User.query)
    # print(users)
    # user_2 = await User.get(4)
    # print(user_2)
    # new_user = await User.create(name="Sam", username='Luka', email='Luka@ggail.com')
    # print(new_user)

    # further code goes here

    # await db.pop_bind().close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
    # asyncio.run(main())
