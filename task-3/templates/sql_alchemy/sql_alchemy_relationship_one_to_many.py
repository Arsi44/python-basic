from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///example2.db')
Session = sessionmaker(bind=engine)
my_session = Session()
Base = declarative_base()


# One To Many (bidirectional *-двунаправленная)
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    children_bind = relationship("Address", back_populates="parent_bind")  # link to child element


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    some_text = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))  # link to parent column
    parent_bind = relationship("User", back_populates="children_bind")  # for bidirectionality


Base.metadata.create_all(engine)

# add users
my_session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy')])

wendy = my_session.query(User).filter_by(name="wendy").first()
mary = my_session.query(User).filter_by(name="mary").first()
fred = my_session.query(User).filter_by(name="fred").first()

# add bind info for users
my_session.add_all([
    Address(user_id=wendy.id, some_text='addr1'),
    Address(user_id=mary.id, some_text='addr2'),
    Address(user_id=fred.id, some_text='addr3')])

print(dir(wendy))
print(wendy.children_bind)

my_session.commit()
