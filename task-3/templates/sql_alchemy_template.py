from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# engine = create_engine('sqlite:///:memory:', echo=True)
# движок, на котором все пишется
engine = create_engine('sqlite:///example.db')
# создаём объект сессии
Session = sessionmaker(bind=engine)
# создаём экземпляр, чтобы работать в текущей сессии
my_session = Session()

# Прописываем базовый класс, от которого будем наследовать все остальные, чтобы использовать средства ORM
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)


# print(repr(User.__table__))
# create tables if not exists
Base.metadata.create_all(engine)

ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
# add one
my_session.add(ed_user)
# find one
our_user = my_session.query(User).filter_by(name='ed').first()
# change one
ed_user.nickname = 'eddie'
# add many
my_session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy')])
# modified objects
print(my_session.dirty)
# pending objects
print(my_session.new)

# commit the transaction
# my_session.commit()

# rollback can be userd before commit
# my_session.rollback()
